application: hello #identifying name for the app; we are giving the name hello to our web app.
version: 1  #If updated too version: 2, App Engine will keep a copy of version 1 in memory to rollback if necessary
runtime: python27
api_version: 1
threadsafe: false #false means our web app isn’t made to receive multiple requests at once, only one at a time
handlers:
- url: /.*  # /.* means any URL directs to hello.py. /welcome would reserve hello.py for the welcome URL
  script: hello.py
