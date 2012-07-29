import sys
import praw
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
filename = config.get("user", "file")
mkdnfilename = config.get("user", "mkdn")

USER_AGENT = "subreddit css development bot for reddit %s" % subreddit
print(USER_AGENT)

print("uploading %s" % filename)

with open(filename, 'r') as file:
    style = file.read()

with open(mkdnfilename, 'r') as file:
    sidebar = file.read()

print("Going to Reddit %s" % subreddit)
r = praw.Reddit(user_agent = USER_AGENT)
r.login(username, password)
print("Logged in")
sr = r.get_subreddit(subreddit)
print("Got subreddit")
print("Setting sidebar markdown")
sr.update_settings(description = sidebar)
print("hashing style")
style_hash = hashlib.md5(style.encode('UTF-8'))
style = style + "/*" + style_hash.hexdigest() + "*/"
print("set style")
sr.set_stylesheet(style)
style_set = sr.get_stylesheet()['stylesheet']
if (style_set.find(style_hash.hexdigest()) == -1):
    print("Style that was uploaded was invalid. Manual mode")
    d = difflib.Differ()
    result = list(d.compare(style_set.splitlines(1),style.splitlines(1)))
    pprint(result)
else:
    print("Sucessfully uploaded CSS to Subreddit %s" % subreddit)
print(datetime.datetime.now().ctime())
