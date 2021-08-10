import flask
#from gevent.pywsgi import WSGIServer
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


#@app.route("/", methods=["GET"])
#def hello():
#    """ Return a friendly HTTP greeting. """
#    return "Hello World!\n"
val = input("Goodafternoon, what can I help you with? ")
selection = input("You need help with \"%s\". Is that correct? (Please type yes or no)" % (val))
if selection == "yes":
    print("Okay, one moment please")
else:
    print("Have a nice day")
quit()
if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)