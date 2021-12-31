import requests
import json
from os import environ
from dotenv import load_dotenv
import time, random

load_dotenv()

channel_file = open('channels.txt', 'r')
channels = channel_file.readlines()

message_file = open('messages.txt', 'r')
messages = message_file.readlines()

for channel in channels:

  baseURL = "https://discordapp.com/api/channels/{}/messages".format(channel)
  headers = {"Authorization": environ.get("AUTH_TOKEN"),
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Content-Type": "application/json", }

  message = random.choice(messages)

  POSTedJSON = json.dumps({"content": message})

  r = requests.post(baseURL, headers= headers, data = POSTedJSON)
  time.sleep(10)
