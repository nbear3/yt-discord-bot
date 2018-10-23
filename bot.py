import asyncio
import discord
import os
# from flask import Flask
# from flask_ask import Ask, statement
from discord.ext import commands
import urllib
from bs4 import BeautifulSoup


# app = Flask(__name__)    
# ask = Ask(app, '/')
bot = commands.Bot(command_prefix="!")
# global_ctx = {}

# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')
#     print(search(global_ctx['song']))
#     await bot.close()

def search(search_query):
    # query = urllib.quote(search_query)
    url = "https://www.youtube.com/results?search_query=" + search_query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    vid = soup.find(attrs={'class':'yt-uix-tile-link'})
    return 'https://www.youtube.com' + vid['href']

# @ask.intent('GetSongIntent')
# def getSong(song):
#     global_ctx['song'] = song
#     run_bot()
#     return statement("Playing %s" % song).simple_card('Now Playing', song)


@bot.command(name='play',
                pass_context=True,
                description='play from youtube',
                brief='URL',
                aliases=['p'])
async def play_song(ctx, *search_query):
    url = search('+'.join(search_query).strip())
    voice = await bot.join_voice_channel(global_player['bear'].voice.voice_channel)
    player = await voice.create_ytdl_player(url)
    global_player['yt'] = player
    player.start()


global_player = {}
@bot.event
async def on_ready():
    print('Logged in as %s' % bot.user.name)
    print(bot.user.id)
    print('------')

    global_player['bear'] = next((x for x in bot.get_all_members() if x.id=='156832648042512384' and x.voice.voice_channel is not None), None)
    print(global_player['bear'].name)
    print(global_player['bear'].voice.voice_channel)


def search(search_query):
    # query = urllib.quote(search_query)
    url = "https://www.youtube.com/results?search_query=" + search_query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    vid = soup.find(attrs={'class':'yt-uix-tile-link'})
    return 'https://www.youtube.com' + vid['href']


bot.run(os.environ['DISCORD_TOKEN'])

