import sys
import reddit
import ConfigParser

print reddit.__version__

print "loading config"
config = ConfigParser.ConfigParser()
config.read(sys.argv[1])
username = config.get("user", "username")
password = config.get("user", "password")
subreddit = config.get("user", "subreddit")

USER_AGENT = "subreddit css bot for reddit %s" % subreddit

with open("style.css",'r') as file:
    style = file.read()

