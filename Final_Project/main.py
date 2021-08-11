import flask
import random
import os
#from gevent.pywsgi import WSGIServer
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


#declare a textfile
text_file = open("responses.txt","r")

#read lines from text file
lines = text_file.readlines()

#initalize an empty array
options = []

#list of possible responses
responses1 = ["Okay, one moment please", "Sure, grabbing some more information"]

#append line to array if it is not empty
for line in lines:
    if line != "\n":
        options.append(line.strip())

print("Goodafternoon, what can I help you with?")

#select random int
random_index = random.randint(0,len(options)-1)

#display 3 random options from the array
options = random.sample(options,3)
for i in range(len(options)):
    print(i+1, ":", options[i])

#take the user's input
choice = input("Choose one of the options above or type other: ")

for i in range(len(options)):
    if choice.isnumeric() == True:
        if int(choice) == i+1:
            choice = options[i]
#if the user types other 
if choice == "other":
    choice = input("okay, what do you need help with?")
selection = input("You need help with \"%s\". Is that correct? (Please type yes or no)" % (choice))
if selection == "yes":
    #print a random response
    print(random.choice(responses1))

    #if the option the user inputed is not in the array don't add
    if choice not in options:
        if choice != "other":
            options.append(choice)
    with open('responses.txt', 'w') as f:
        for item in options:
            f.write("%s\n" % item)
else:
    print("Have a good day")

#plan on creating a loop, exit for now
quit()
if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
