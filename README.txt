This program is very finicky, definitely not complete until I figure out how to iron out some issues.

It just gets the top posts along with the top comment of any Reddit subreddit that is entered as an argument. To prevent constantly
being shut down by reddit, you can disable getting comments. It makes the script run faster too.
The way you would do this is by running it in the terminal like so:

>reddit.py <name of subreddit> <true or false>

No arguments will result in the default. Default is just the AskReddit subreddit, and true for comments.

Important: Top comments will not show if the post is not a textpost since the URL associated with that post will 
not be where the comments are. So subreddits with posts only linking to pictures will have no comments shown regardless of your setting

For some reason that I can't seem to figure out entirely, sometimes Reddit will kick me off and the program will throw error 429.
Now it says that there are too many calls, but sometimes the program won't even access anything more than once before throwing the 
exception, it'll just crash when you first run it! This happens very randomly, sometimes it'll get midway through and stop working 
or it'll stop working right from the start. I need to fix this before I can call this fully operational.

I made this for fun when I learned how to access JSON files from websites and get data from them. It's very rewarding to figure it out
and actually get it to retrieve the data. Instead of returning the name, URL, and top comment of any post I might decide to scrap the 
top comment part. So I might just display the name of the top posts and a link to them. It seems to me like accessing both the title and 
top comment is what's causing too many calls to be sent out. I could alternatively make my program wait before trying to get more data, 
but that would make it too slow.