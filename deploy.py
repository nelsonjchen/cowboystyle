import reddit
import ConfigParser

print reddit.__version__
print "loading config"

config = ConfigParser.ConfigParser()
username = config.get("user", username)
password = config.get("user", password)
subreddit = config.get("user", subreddit)
