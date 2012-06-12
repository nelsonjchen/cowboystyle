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

print USER_AGENT

with open("stylesheets/style.css",'r') as file:
    style = file.read()

print "Going to Reddit"
r = reddit.Reddit(user_agent = USER_AGENT)
r.login(username, password)
print "Logged in"
sr = r.get_subreddit(subreddit)
print "Got subreddit"
sr.set_stylesheet(style)
print "set style"
style_set = sr.get_stylesheet()['stylesheet']
if (style_set != style):
    print "Style that was uploaded was invalid. Manual mode"
    # print style
else:
    print "Sucessfully uploaded CSS to Subreddit"

