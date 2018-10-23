import asyncio
import discord
import os
# from flask import Flask
from discord.ext import commands

# from pylexa.app import alexa_blueprint
# from pylexa.intent import handle_intent
# from pylexa.response import PlainTextSpeech

# app = Flask(__name__)
# app.config['app_id'] = os.getenv('ALEXA_APP_ID')
# app.register_blueprint(alexa_blueprint)

loop = asyncio.get_event_loop()
bot = commands.Bot(loop=loop, command_prefix="!")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.disconnect()

# @bot.command()
# async def greet(ctx):
#     await ctx.send(":smiley: :wave: Hello, there!")

# app.
# bot.run(os.environ['DISCORD_TOKEN'])

from flask import Flask, render_template
from flask_ask import Ask, statement

loop = asyncio.get_event_loop()
app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('GetSongIntent')
def getSong(song):
    text = song
    loop.run_until_complete(bot.run(os.environ['DISCORD_TOKEN']))
    return statement(text).simple_card('Hello', text)

# if __name__ == '__main__':
#     app.run(debug=True)