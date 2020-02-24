from flask import Flask
from flask import request

app = Flask(__name__)   #App Instance created

@app.route("/")         #When URL ends in '/' print "Hello, World!"
def greetings():        #Created 'greetings' method
    return "Hello, World!"
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run flask App Instance


#Route below does not work.
#Run: ps aux | grep hello.py, then kill process to stop server
@app.route("/stop", methods=["POST"]) #When URL ends in '/stop' shutdown server
def shutdown():
    return 'Shutting server down...'
if __name__ == "__main__":
    #app.shutdown_server()
    app.shutdown()
