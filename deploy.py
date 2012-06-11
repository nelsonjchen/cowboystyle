import sys
import reddit
import ConfigParser

print "Beginning uploading CSS to Subreddit"
config = ConfigParser.ConfigParser()
config.read(sys.argv[1])
username = config.get("user", "username")
password = config.get("user", "password")
subreddit = config.get("user", "subreddit")

USER_AGENT = "subreddit css bot for reddit %s" % subreddit

with open("stylesheets/style.css",'r') as file:
    style = file.read()

r = reddit.Reddit(user_agent = USER_AGENT)
r.login(username, password)
print "Logged in"
sr = r.get_subreddit(subreddit)
print "Got subreddit"
sr.set_stylesheet(style)
print "Finished uploading CSS to Subreddit"
