# import requests
# import json
from os import environ
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import random

load_dotenv()

channel_file = open('channels.txt', 'r')
channels = channel_file.readlines()

message_file = open('messages.txt', 'r')
messages = message_file.readlines()

"""
for channel in channels:

  baseURL = "https://discordapp.com/api/channels/{}/messages".format(channel)
  headers = {"Authorization": environ.get("AUTH_TOKEN"),
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Content-Type": "application/json", }

  POSTedJSON = json.dumps({"content": message})

  r = requests.post(baseURL, headers= headers, data = POSTedJSON)
  time.sleep(10)
  """

client = discord.Client()

@tasks.loop(minutes=5)
async def background():
   await client.wait_until_ready()
   channel = client.get_channel(random.choice(channels))
   await channel.send(random.choice(messages))

@client.event
async def on_ready():
    background.start()

client.run(environ.get('BOT_TOKEN'))
