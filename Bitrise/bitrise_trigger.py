# Use this script to trigger a bitrise build, with options to filter out the returned list of apps.
import requests
import json
from prettytable import PrettyTable
import yaml

# Replace token_key with the bitrise api key.
# To grab the API key, go to your account settings, then go to Security.
# Generate a new personal access token and paste it here.
token_key = ''
admin_token = 'token %s' % token_key
headers = {'Authorization': admin_token}

def getAppSlug(request_header):
    apps_request = requests.get('https://api.bitrise.io/v0.1/apps', headers=request_header)
    app_names = apps_request.json()
    table = PrettyTable(['App','Slug'])
    app_title_array = []
    app_slug_array = []
    for each in app_names['data']:
        app_title = each['title']
        app_slug = each['slug']
        # Optionally use this logic below if you have multiple apps and want to filter out certain apps.
        # if app_title == '':
        #     table.add_row([app_title, app_slug])
        # else:
        #     pass
        table.add_row([app_title, app_slug])
    table.align["App"] = "l"
    table.sortby = "App"
    print table

def buildTrigger(request_header, app_slug, branch, tag, commit_hash, workflow, message):
    payload = {"hook_info":{"type":"bitrise"},"build_params":{"branch":branch,"tag":tag,"workflow_id":workflow,"commit_hash":commit_hash,"commit_message":message}}
    trigger_url = 'https://api.bitrise.io/v0.1/apps/%s/builds' % app_slug
    build_request = requests.post(trigger_url, headers=request_header, json=payload)
    print "SUCCESS!"
    print json.dumps(build_request.json(), indent=4, sort_keys=True)

# Parses the bitrise.yml to read certain fields.
def yamlParse(request_header, app_name):
    apps_request = requests.get('https://api.bitrise.io/v0.1/apps', headers=request_header)

# User does some input to build specific things.
def userInput():
    getAppSlug(headers);
    app_slug = raw_input("Choose an app to build: ")
    yaml_url = 'https://api.bitrise.io/v0.1/apps/%s/bitrise.yml' % app_slug
    yaml_request = requests.get(yaml_url,headers=headers)
    y = yaml.safe_load(yaml_request.text)
    y_workflows = y['workflows']

    branch_name = raw_input("Which branch do you want to build?: ")
    commit_hash = raw_input("Which commit?: ")
    tag_name = raw_input("Which git tag? (If none, leave empty): " )
    table = PrettyTable(['WORKFLOWS'])
    for key in y_workflows.keys():
        table.add_row([key])
    table.align["WORKFLOWS"] = "l"
    table.sortby = "WORKFLOWS"
    print table
    workflow_name = raw_input("Which Bitrise workflow?: ")
    commit_message = raw_input("Enter a message (If none, leave empty): ")
    buildTrigger(headers, app_slug, branch_name, tag_name, commit_hash, workflow_name, commit_message);

userInput();
