# Code written by Echo Mulder & Nick Lodder
# Code edited & proofread by Gray Lewis

import json
import jsonlines
outputFile = "gpt3Config.json"

#Creating a variable for the exam question.
question = input('Dear teacher, welcome to our smart grading programme!\nPlease enter the exam question to be graded: ')
print(question)
while len(question) == 0:
  print("Empty questions are not valid. Please try again.")
  question = input('Please enter the exam question to be graded: ')
    
#Making the code user friendly.
print('We are off to a great start! Now, in order to help you grade exam answers from students, we will ask you for example answers to this question with different scores.\n')

#Empty list to store example answers in.
example_answers = []

#Loop that allows the teacher to store 5 example answers, ranging in their score from 0/10 to 10/10 in increments of 2. 
for i in range(6):
  score = '%s/10' % (i*2)
  new_answer = input('Example of an %s answer:' % (score))
  while len(new_answer) == 0:
    print("Empty answers are not valid. Please try again.")
    new_answer = input('Example of an %s answer:' % (score))
    
  example_answers.append({
    'text': new_answer,
    'label': score
  })

#Making the code user friendly.
print('Thank you! We have stored the following example answers:', example_answers)

try:
  with jsonlines.open(outputFile, mode="w") as file:
    file.write_all(example_answers)

except Exception as e:
  print("Error while writing to %s" % (outputFile))
  print(e)
finally:
  print("The configuration file has been saved to gpt3Config.json. In order to upload this file to the OpenAI server for use, please use the uploadFile.py utility.")
  file.close()
