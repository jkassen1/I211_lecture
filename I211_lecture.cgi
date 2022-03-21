#! /usr/local/bin/python3
from wsgiref.handlers import CGIHandler
from I211_lecture import app

if __name__ == '__main__':
   CGIHandler().run(app.app)
