# Code written by Gray Lewis
# Code edited by Echo Mulder & Nick Lodder

import requests
import json
import sys, getopt

from decouple import config

api_key = config('api_key', default='')

# BEGIN COMMAND LINE PARSING
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]

short_options="q:f:"
long_options=["query=", "file="]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
  if current_argument in ("-q", "--query"):
    userQuery = current_value
  if current_argument in ("-f", "--file"):
    fileId = current_value

try:
  userQuery
except:
  userQuery = input("Please provide a query: ")
  while len(userQuery) == 0:
    print("An empty query is not valid. Please try again.")
    userQuery = input('Please provide a query: ')
    

try:
  fileId
except:
  fileId = input("Please provide an ID for your config file: ")
  while len(fileId) == 0:
    print("An empty ID is not valid. Please try again.")
    fileId = input('Please provide an ID for your config file: ')
    
# END COMMAND LINE PARSING

# API AUTHENTICATION
headers = {
    'Authorization': 'Bearer %s' % (api_key),
    'Content-Type': 'application/json',
}

print()
# FORM REQUEST
body = {
  "file": fileId,
  "query": userQuery,
  "labels": ["0/10", "1/10", "2/10", "3/10", "4/10", "5/10", "6/10", "7/10", "8/10", "9/10", "10/10"],
  "search_model": "ada",
  "model": "davinci",
}

# SEND REQUEST
r = requests.post('https://api.openai.com/v1/classifications', data=json.dumps(body), headers=headers)

# PARSE RESPONSE
responseBody = r.json();

if responseBody["error"]:
  print("There was a problem with your configuration.")
  print(responseBody["error"]["message"])

else:
  print("Query Submitted: %s \nGrade: %s" % (body["query"], responseBody['label']))