# Author: Taimur Khan
# Purpose: To get the top posts w/ the top comment on the front page of any given subreddit
# Date: 22 December 2019

import urllib.request
import json
import urllib.error
from textwrap import wrap
import sys


# Gets the JSON file and returns a string with the JSON file's contents
def get_data(url):
    web = urllib.request.urlopen(url)

    if web.getcode() == 200:
        d = web.read()
        return d
    else:
        print("Error with JSON file!")


# Using the above returned string, it creates a dictionary where every element can be properly accessed
def get_json(data):
    the_json = json.loads(data)
    return the_json


# Gets the data and prints out every top post on the front page and also prints the top comment for that post
# All is formatted semi-properly
def print_results(data, comments):
    # Get the dictionary
    data = get_json(data)["data"]

    # Indicate beginning
    print("\n\n------------------------ Start ------------------------\n")

    # Try to go through the dictionary and print everything properly
    # The reason there is an except is because Reddit kicks me off randomly if I'm accessing data too often
    # I need to fix this, but the weird thing is sometimes reddit blocks me right away and sometimes it doesn't
    # This program is pretty finicky
    try:
        for val in data["children"]:
            # Get the title from the dictionary and print it
            print("Title:", val["data"]["title"])

            # Get the URL of the post
            url = val["data"]["url"]

            # Print the URL
            print("URL:", url)

            # Create comment data, which is a dictionary of all its properties from the JSON file by appending
            # .json at the end of the URL. Reddit allows this for any post, which makes it very easy to get the comments
            # Very lazy way of checking if the post is a text post. It checks to see if reddit.com/r/ is in the URL of
            # where to post links to
            if "reddit.com/r/" in str(url) and comments_enabled:
                # Try to show comments, if none are present then this code will throw and IndexError
                try:
                    comment_data = get_json(get_data(url + ".json"))
                    # Print that one top comment, all formatted so that text wraps appropriately in the console
                    print("-------------------- Top Comment --------------------")
                    print("\n".join(wrap(f'''{comment_data[1]["data"]["children"][0]["data"]["body"]}''', 53)))
                    print("------------------------- / -------------------------")
                except IndexError:
                    print("No comments here!")

            # New line
            print()

    except urllib.error.HTTPError:
        # TODO: Fix this somehow, so you can avoid reddit kicking you off
        # Instead of getting a huge exception, just tell the user that Reddit hates em
        print("\n-------------------------------------------------")
        print("|\t\tToo many calls, reddit hates you :(\t\t|")
        print("-------------------------------------------------")


# The URl for any subreddit, just add .json at the end of it
url = "https://www.reddit.com/r/AskReddit"

# Boolean to print comments as well
comments_enabled = True

# Get arguments passed
args = sys.argv

# If the script itself is not the only argument, the other must be a subreddit the user wants to link to
# If there are 3 arguments, then it reads the last one as the true or false. If the third one is not properly set
# then the comments will be enabled by default
if len(args) > 1:
    url = "https://www.reddit.com/r/" + args[1] + "/"
    if len(args) > 2:
        try:
            ce = args[2].capitalize()
            if ce == "False": ce = False
            comments_enabled = bool(ce)
        except Exception:
            comments_enabled = True

# Print the results by calling the function
# Throw exception if needed
try:
    print_results(get_data(url + ".json"), comments_enabled)
except urllib.error.HTTPError:
    print("Reddit booted us off! Sorry!")
