# Use this this script to generate a report of your builds in bitriseself.
# Modify the limit to adjust percentages.
import requests
import json
from prettytable import PrettyTable

# Replace token_key with the bitrise api key.
# To grab the API key, go to your account settings, then go to Security.
# Generate a new personal access token and paste it here.
token_key = ''
admin_token = 'token %s' % token_key
headers = {'Authorization': admin_token}

# Set number of builds to look back
limit = 20
print "Grabbing Bitrise mobile build health from the last %s builds." % limit

def build_health():

	app_r = requests.get('https://api.bitrise.io/v0.1/apps', headers=headers)
	app_name = app_r.json()
	# Summary table
	table = PrettyTable(['App','Status','Success Rate (%)','Succeeded','Pending','Failed','Aborted'])
	for each in app_name['data']:
		app_title = each['title']
		app_slug = each['slug']

		# Grab all the status codes from last x builds
		r = requests.get('https://api.bitrise.io/v0.1/apps/%s/builds?limit=20' % (app_slug), headers=headers)
		s = r.json()
		i = 1
		# status=0, not finished
		# status=1, build success
		# status=2, build failure
		# status=3, build aborted
		zero = 0
		one = 0
		two = 0
		three = 0
		# Count each status
		for each in s['data']:
			if each['status'] == 0:
				zero += 1
			elif each['status'] == 1:
				one += 1
			elif each['status'] == 2:
				two += 1
			elif each['status'] == 3:
				three += 1
			else:
				raise ValueError('Something went wrong.')
			i += 1

		# Calculate each percentage, display status icon. Aborts and pending don't count
		success_rate = ((float(one) / float(limit-zero-three))*100)
		if 0 <= success_rate <= 50:
			status = u'\u274C'
			success_rate = '%.2f' % success_rate + "%"
		elif 50 < success_rate <= 75:
			status = u'\u26C5'
			success_rate = '%.2f' % success_rate + "%"
		else:
			status = u'\u2705'
			success_rate = '%.2f' % success_rate + "%"
		# Print results in table per app. Comment out if want to keep things clean.
		# t = PrettyTable(['Status', icon])
		# t.add_row(['Success (%)', success_rate])
		# t.add_row(['Success', one])
		# t.add_row(['Failed', two])``
		# t.add_row(['Aborted', three])
		# t.add_row(['Pending', zero])
		# print t
		table.add_row([app_title, status, success_rate, one, zero, two, three])
	print "+-------------------------------+--------+-----SUMMARY------+----------+---------+--------+---------+"
	table.align["App"] = "l"
	#table.sortby = "Success Rate (%)"
	table.sortby = "App"
	print table

build_health();

print "Status icon legend:"
print "Success rate >= 75%: " + u'\u2705' + " => Builds look good"
print "Success rate 50~75%: " + u'\u26C5' + " => Builds are unstable, worth taking a look"
print "Success rate <= 25%: " + u'\u274C' + " => Builds are broken, need to investigate"
