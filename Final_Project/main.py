import flask
import random
import os
#from gevent.pywsgi import WSGIServer
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)
done = False
#initial bot message
botResponse = "Hello, I'm the UTSA Helper Bot. I'll be happy to help you!"

#potential user greetings
##'hello', 'hi', and 'good' all count as more than one response
### technically since we just check for those words inside of
### the user greeting
userGreetings = ["hello", "hi", "how are you", "greetings", "howdy", "hey"]

#potential user feelings
##'not' and 'been' could trigger multiple responses such as
###'not bad' or 'been better'
posUserFeelings = ["good", "great", "alright"]
negUserFeelings = ["bad", "ok", "not", "been"]

#services offered to users
userServices = {"uts-vdi" : "https://www.utsa.edu/techsolutions/students/software/vdi.html",
                "uts-vpn" : "https://www.utsa.edu/techsolutions/docs/wireless/WhatUsesVPN.pdf",
                "proctorio" : "https://odl.utsa.edu/digital-tools/assessment/proctorio/",
                "blackboard" : "https://odl.utsa.edu/blackboard-collaborate/",
                "asap" : "https://asap.utsa.edu/#_ga=2.45383021.873935276.1628727794-1874626014.1628727794",
                "degreeworks" : "https://onestop.utsa.edu/registration/degree-planning/degreeworks/",
                "exam schedule": "https://asap.utsa.edu/terms.htm#_ga=2.57415011.873935276.1628727794-1874626014.1628727794",
                "calendar" : "https://www.utsa.edu/calendar/academic/#_ga=2.150027647.873935276.1628727794-1874626014.1628727794",
                "bluebooks" : "https://bluebook.utsa.edu/#_ga=2.212588637.873935276.1628727794-1874626014.1628727794"
                }

#positive random bot responses
posRandResponses = ["That's good to read.",
                   "Glad to read.",
                   "Pleased you are well.",
                   "Good to know.",
                   "Awesome!"]
#negative random responses
negRandResponses = ["Hopefully I can make it better!",
                    "Sorry to hear.",
                    "Wish it weren't so!",
                    "Oh no!",
                    "Look on the bright side!"]

#random confirmation
randConfirm = ["Anytime.", "Awesome!", "Glad I could help!"]
#random apology
randApology = ["Sorry about that", "Let's try again"]

def checkFeeling(inputStr, response):
    #check for a good feeling
    for feeling in posUserFeelings:
        if inputStr.lower() in feeling.lower():
            #ask how they are feeling
            response = posRandResponses[random.randint(0, len(posRandResponses)-1)] + " How can I help you today?"
            for service in userServices:
                print(service)
            return response


    #check for a bad feeling
    for feeling in negUserFeelings:
        if inputStr.lower() in feeling.lower():
            #ask how they are feeling
            response = negRandResponses[random.randint(0, len(negRandResponses))] + " How can I help you today?"
            for service in userServices:
                print(service)
            return response
    return response


#prompt user input using a while loop
while not done:
    #while(true) and break when we get the response that they
    #no longer need help.

    #Output the current bot response and get the user input
    userInput = input(botResponse + "\n")


    #check for a greeting
    for greeting in userGreetings:
        if userInput.lower() in greeting.lower():
            #ask how they are feeling
            botResponse = "How are you feeling today?"
            continue

    botResponse = checkFeeling(userInput.lower(), botResponse)
    #if botResponse != "null":
    #    print(botResponse + " THIS IS A TEST")
    #    continue    
    """
  #check for a good feeling
  for feeling in posUserFeelings:
    if userInput.lower() in feeling.lower():
      #ask how they are feeling
      botResponse = posRandResponses[random.randint(0, len(posRandResponses)-1)] + " How can I help you today?"
      for service in userServices:
          print(service)
      continue
  #check for a bad feeling
  for feeling in negUserFeelings:
    if userInput.lower() in feeling.lower():
      #ask how they are feeling
      botResponse = negRandResponses[random.randint(0, len(negRandResponses))] + " How can I help you today?"
      continue
    """

    #check for a service
    for serv in userServices:
        if userInput.lower() in serv:
            #ask if they wanted this service
            botResponse = "Did you say you wanted to know about " + userInput + "? (yes/no)"
            userInput = input(botResponse + "\n")
            #if they did want it
            if userInput.lower() == "yes":
                #give them the link and see if they still need help
                botResponse = "Please click the following link\n (" + userServices[serv] + ")\n And after reading that, please confirm if I was able to help. (yes/no)"
                userInput = input(botResponse + "\n")
                #if we did help
                if "yes" in userInput.lower():
                    #ask if we can do anything else
                    botResponse = randConfirm[random.randint(0, len(randConfirm)-1)] + " Anything else I can help with? (yes/no)"
                    userInput = input(botResponse + "\n")
                    #if yes
                    if "yes" in userInput.lower():
                        #ask what else we can do for them
                        botResponse = "How can I help you today?"
                        for service in userServices:
                            print(service)
                        continue
                    #if no
                    elif "no" in userInput.lower():
                        #say goodbye
                        print("It has been a pleasure to help you, have a nice day!\n")
                        done = True
                #if we did not help
                elif "no" in userInput.lower():
                    #ask what we can help them with
                    botResponse = randApology[random.randint(0, len(randApology)-1)] + ", how can I help?"
                    for service in userServices:
                        print(service)
                    continue
            #if they did not want this
            elif "no" in userInput.lower():
                botResponse = randApology[random.randint(0, len(randApology)-1)] + ", how can I help?"
                for service in userServices:
                    print(service)
                continue

quit()
if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)