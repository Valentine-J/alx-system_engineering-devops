#!/usr/bin/python3
"""Define number_of_subscribers function"""
import requests
import json

def number_of_subscribers(subreddit):
"""Return the total number of subscribers on a given subreddit."""
url = "https://www.reddit.com/r/"
headers = {"User-Agent": "User Agent"}
response = requests.get(url + subreddit + "/about.json", headers=headers, allow_redirects=False)

# print(response)
if response.status_code == 200:
x = response.json().get("data").get("subscribers")
return response.json().get("data").get("subscribers")
else:
return 0
