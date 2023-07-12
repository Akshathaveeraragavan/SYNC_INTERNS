#Create a URL shortener using python

import pyshorteners
long_url=input('Hi user , Please enter the long url:') #getting input from user

tiny_url= pyshorteners.Shortener()      #shorten the url
short_url=tiny_url.tinyurl.short(long_url) 

print('The short url is:',short_url)

