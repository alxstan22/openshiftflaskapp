from flask import Flask
from flask import request

application = Flask(__name__)   #App Instance created

@application.route("/")         #When URL ends in '/' print "Hello, World!"
def greetings():        #Create 'greetings' method
    return "Hello, World!"
#if __name__ == "__main__":        # on running python app.py
#    app.run()                     # run flask App Instance


@application.route("/other")         #When URL ends in '/' print "Hello, World!"
def amessage():        #Create 'greetings' method
    return "This is a different page!"

if __name__ == "__main__":        # on running python app.py
    application.run()                     # run flask App Instance
