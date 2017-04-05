import json
import urllib2

url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"
data = json.load(urllib2.urlopen(url))
print (data)
