import json
import jsonlines
outputFile = "gpt3Config.json"

#Creating a variable for the exam question.
question = input('Dear teacher, welcome to our smart grading programme! Please fill out the exam question.')

#Making the code user friendly.
print('We are off to a great start! Now, in order to help you grade exam answers from students, we will ask you for example answers to this question with different scores.')

#Empty list to store example answers in.
example_answers = []

#Loop that allows the teacher to store 5 example answers, ranging in their score from 0/10 to 10/10 in increments of 2. 
for i in range(6):
  score = '%s/10' % (i*2)
  new_answers = input('Example of an %s answer:' % (score))
  example_answers.append({
    'text': new_answers,
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
  file.close()    