# import asyncio
# import discord
# import os
# from flask import Flask
# from discord.ext import commands

# from pylexa.app import alexa_blueprint
# from pylexa.intent import handle_intent
# from pylexa.response import PlainTextSpeech

# app = Flask(__name__)
# app.config['app_id'] = os.getenv('ALEXA_APP_ID')
# app.register_blueprint(alexa_blueprint)

# loop = asyncio.get_event_loop()
# bot = commands.Bot(loop=loop, command_prefix="!")

# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')

# @bot.command()
# async def greet(ctx):
#     await ctx.send(":smiley: :wave: Hello, there!")

# app.
# bot.run(os.environ['DISCORD_TOKEN'])


# @handle_intent('Echo')
# def handle_echo_intent(request):
#     return PlainTextSpeech(
#         request.slots.get('message', 'Nothing to echo'))

from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('GetSongIntent')
def getSong(song):
	text = song
	return statement(text).simple_card('Hello', text)

# if __name__ == '__main__':
#     app.run(debug=True)