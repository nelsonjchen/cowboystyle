import sys
import praw
import datetime
import difflib
from pprint import pprint
import hashlib
import os
import subprocess
import astral

print("Beginning uploading CSS to Subreddit")

username = os.environ[ "REDDIT_USER" ]
password = os.environ[ "REDDIT_PASSWORD" ]
subreddit = os.environ[ "REDDIT_SUBREDDIT" ]
mode = os.environ[ "REDDIT_STYLESHEET_MODE" ]
compile_scss = bool(os.environ[ "REDDIT_STYLESHEET_COMPILE" ])
sidebar_filename = os.environ[ "REDDIT_SIDEBAR_FILENAME" ]

if (mode == "day"):
    filename = os.environ[ "REDDIT_STYLESHEET_DAY_FILENAME" ]
elif (mode == "night"):
    filename = os.environ[ "REDDIT_STYLESHEET_NIGHT_FILENAME" ]
elif (mode == "auto"):
    filename = os.environ[ "REDDIT_STYLESHEET_DAY_FILENAME" ]
else:
    filename = os.environ[ "REDDIT_STYLESHEET_DAY_FILENAME" ]

if (compile_scss):
    subprocess.call("compass compile", shell=True)

USER_AGENT = "Subreddit SCSS Update Bot for /r/%s" % subreddit
print(USER_AGENT)

print("Uploading %s" % filename)

with open(filename, 'r') as file:
    style = file.read()

with open(sidebar_filename, 'r') as file:
    sidebar = file.read()

print("Going to Reddit %s" % subreddit)
r = praw.Reddit(user_agent = USER_AGENT)
r.login(username, password)
print("Logged in as %s" % username)
sr = r.get_subreddit(subreddit)
print("Got Subreddit %s" % subreddit)
print("Setting sidebar's markdown")
sr.update_settings(description = sidebar)
print("Hashing Stylesheet")
style_hash = hashlib.md5(style.encode('UTF-8'))
style = style + "/*" + style_hash.hexdigest() + "*/"
print("Setting Stylesheet")
sr.set_stylesheet(style)
style_set = sr.get_stylesheet()['stylesheet']
if (style_set.find(style_hash.hexdigest()) == -1):
    print("Style that was uploaded was invalid. Upload manually for errors")
    d = difflib.Differ()
    result = list(d.compare(style_set.splitlines(1),style.splitlines(1)))
    pprint(result)
else:
    print("Sucessfully uploaded CSS to Subreddit %s" % subreddit)
print(datetime.datetime.now().ctime())
