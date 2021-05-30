import os
import openai
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
  if current_argument in ("-f", "--file"):
    file_name = current_value

try:
  file_name
except:
  file_name = "gtp3Config.json"
  print("Defaulting to gpt3Config.json. To provide a different config file to be uploaded, please use the -f=FILE_NAME argument.")

openai.api_key = api_key
file = openai.File.create(
  file=open("gpt3Config.json"),
  purpose='classifications'
)

print(file)
print("The ID of the file that was uploaded is %s" % (file["id"]))