# Use this script to abort any build that you own on Bitrise that is pending.
import requests
import json
from prettytable import PrettyTable

# Replace token_key with the bitrise api key.
# To grab the API key, go to your account settings, then go to Security.
# Generate a new personal access token and paste it here.
token_key = ''
admin_token = 'token %s' % token_key
headers = {'Authorization': admin_token}

def getAppList(request_header):
    app_r = requests.get('https://api.bitrise.io/v0.1/apps', headers=request_header)
    app_name = app_r.json()
    print PrettyTable(['ALL PENDING BUILDS'])
    table = PrettyTable(['App','App Slug','Build Slug','Triggered At','Triggered By'])
    for each in app_name['data']:
        app_title = each['title']
        app_slug = each['slug']
        r = requests.get('https://api.bitrise.io/v0.1/apps/%s/builds' % (app_slug), headers=request_header)
        s = r.json()
        for each in s['data']:
            if each['status'] == 0:
                build_slug = each['slug']
                triggered_at = each['triggered_at']
                triggered_by = each['triggered_by']
                table.add_row([app_title,app_slug,build_slug,triggered_at,triggered_by])
            else:
                pass
    print table

def abortBuild(request_header):
    getAppList(headers);
    app_input = raw_input("Enter app slug to abort: ")
    build_input = raw_input("Enter build slug to abort: ")
    abort_reason = raw_input("Abort reason (leave empty for none): ")
    abort_url = 'https://api.bitrise.io/v0.1/apps/%s/builds/%s/abort' % (app_input, build_input)
    payload = {"abort_reason":abort_reason}
    abort_request = requests.post(abort_url, headers=request_header, json=payload)
    print abort_request

abortBuild(headers);
