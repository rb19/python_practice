# Use this script to grab the last successful build for a given app.
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
    print PrettyTable(['LAST SUCCESSFUL BUILDS PER APP'])
    table = PrettyTable(['App','App Slug','Build Slug','Build Number','Branch Name','Triggered Workflow','Finished At','Triggered By'])
    for each in app_name['data']:
        app_title = each['title']
        app_slug = each['slug']
        r = requests.get('https://api.bitrise.io/v0.1/apps/%s/builds?limit=1' % (app_slug), headers=request_header)
        s = r.json()
        for each in s['data']:
            if each['status'] == 1:
                build_slug = each['slug']
                branch_name = each['branch']
                build_number = each['build_number']
                triggered_workflow = each['triggered_workflow']
                finished_at = each['finished_at']
                triggered_by = each['triggered_by']
                table.add_row([app_title,app_slug,build_slug,build_number,branch_name,triggered_workflow,finished_at,triggered_by])
            else:
                pass
    table.align['App'] = "l"
    table.sortby = "App"
    print table

getAppList(headers);
