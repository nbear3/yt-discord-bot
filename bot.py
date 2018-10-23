import asyncio
import discord
import os
from flask import Flask, render_template
from flask_ask import Ask, statement
from discord.ext import commands
import urllib
from bs4 import BeautifulSoup
import threading

loop = asyncio.get_event_loop()
app = Flask(__name__)
ask = Ask(app, '/')
bot = commands.Bot(command_prefix="!")
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

def run_after(f_after):
	def wrapper(f):
	    def wrapped(*args, **kwargs):
	        ret = f(*args, **kwargs)
	        f_after()
	        return ret
	    return wrapped
	return wrapper

@ask.intent('GetSongIntent')
@run_after(run_bot)
def getSong(song):
    global_ctx['song'] = song
    return statement("Playing %s" % song).simple_card('Now Playing', song)
