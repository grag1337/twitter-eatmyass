import keyboard  # using module keyboard
import tweepy
import io
from bs4 import BeautifulSoup
import requests
import urllib
from art import *
import io
import os
from time import sleep
import pickle
import glob
from urllib.request import Request, urlopen

auth = tweepy.OAuthHandler("your_consumer_key",
                           "your_consumer_secret")

auth.set_access_token("your_access_token",
                      "your_access_token_secret")

api = tweepy.API(auth)

url = "your_raw_pastebin_link"
hdr = {'User Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")
soup2 = str(soup)
soup3 = soup2.splitlines()


def eatmyass(soup3):

    try:
        for index, value in enumerate(soup3):
            api.update_status("[+] 9gag " + value)
            soup3.pop(0)
            print("[*] Tweeted [+] 9gag " + value + "!")
    except KeyboardInterrupt:
        print("Exiting Program...")
    except tweepy.TweepError:
        soup3.pop(0)
        print("Found Duplicate, Skipping...")
        eatmyass(soup3)


eatmyass(soup3)
