import asyncio
import discord
import os
from flask import Flask, render_template
from flask_ask import Ask, statement
from discord.ext import commands
import urllib
from bs4 import BeautifulSoup
import threading

app = Flask(__name__)
ask = Ask(app, '/')
loop = asyncio.new_event_loop()
bot = commands.Bot(loop=loop, command_prefix="!")
global_ctx = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(search(global_ctx['song']))
    await bot.close()


def run_bot():
    loop.run_until_complete(bot.run(os.environ['DISCORD_TOKEN']))


def search(search_query):
    # query = urllib.quote(search_query)
    url = "https://www.youtube.com/results?search_query=" + search_query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    vid = soup.find(attrs={'class':'yt-uix-tile-link'})
    return 'https://www.youtube.com' + vid['href']


@ask.intent('GetSongIntent')
def getSong(song):
    global_ctx['song'] = song
    run_bot()
    return statement("Playing %s" % song).simple_card('Now Playing', song)

