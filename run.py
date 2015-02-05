#! /usr/bin/env python
from flask import Flask
import os
import time 
import datetime
from flask import render_template
from app import app

app.route("/profile")
def profile():
      return render_template('profile.html', time=timeinfo())

  
def timeinfo():
    now = time.strftime("%a %d %b %Y")
    return now
  
  
app.run(debug=True,host="0.0.0.0",port=8080)

