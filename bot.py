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


def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
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

    t = threading.Thread(target=loop_in_thread, args=(loop,))
    t.start()

    loop.run_until_complete()
    return statement(text).simple_card('Hello', text)

# if __name__ == '__main__':
#     app.run(debug=True)