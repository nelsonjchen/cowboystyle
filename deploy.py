import sys
import reddit
import configparser
import datetime
import difflib
from pprint import pprint
import hashlib

print("Beginning uploading CSS to Subreddit")
config = configparser.ConfigParser()
config.read(sys.argv[1])
username = config.get("user", "username")
password = config.get("user", "password")
subreddit = config.get("user", "subreddit")

USER_AGENT = "subreddit css bot for reddit %s" % subreddit

print(USER_AGENT)

with open("stylesheets/style.css",'r') as file:
    style = file.read()

print("Going to Reddit")
r = reddit.Reddit(user_agent = USER_AGENT)
r.login(username, password)
print("Logged in")
sr = r.get_subreddit(subreddit)
print("Got subreddit")
style_hash = hashlib.md5(style.encode('UTF-8'))
style = style + "/*" + style_hash + "*/"
print("set style")
style_set = sr.get_stylesheet()['stylesheet']
if (style_set.find(style_hash) == -1):
    print("Style that was uploaded was invalid. Manual mode")
    # d = difflib.Differ()
    # result = list(d.compare(style_set.splitlines(1),style.splitlines(1)))
    # pprint(result)
    # print style
else:
    print("Sucessfully uploaded CSS to Subreddit")
print(datetime.datetime.now().ctime())
