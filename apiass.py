#ques 1

print("The Access Token is a credential that can be used by an application to access an API.")
print("It can be any type of token and is meant for an API.Its purpose is to inform the API that the bearer of this token.")
print("The Access Token should be used as Bearer credential and transmitted in an HTTP Authorization header to the API.")

#ques 2

import socket
n=input("enter domain name: ")
addr1 = socket.gethostbyname("www.google.com")
print(addr1)

#ques 3

import tweepy
Consumer_key="hehtEpCPZdEoSa2AciI9Pq6O1"
Consumer_secret="qoemhQOm9W4EFmkrXukhKukFw0DF6RELj3FfwwbYRVDbNC3ghO"
Access_Token="1011804076793708544-AUO91zwik6awYayp97U7LfYDMXmiyS"
Access_secret="W4EH66xRDEHJpUshHYa3WVRVcvG6fU0PjQEkRllzYSc88"
oauth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
oauth.set_access_token(Access_Token, Access_secret)
api=tweepy.API(oauth)
print(api.search("#casting"))

#ques 4

print("API is a part of library which defines how an application communicates with external code.API can be wiitten in any language.")
print("Library is written in same language which is a collection of all the functions required for the use  case.")
print("for example : Numpy is a library of python,ading support for large,multidimensional arrays and matrices." )
