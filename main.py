import discord
import os
import random
from webserver import keep_alive

client = discord.Client()

rps = ['rock :rock:','paper :newspaper:','scissors :scissors:']

@client.event
async def on_ready():
 await client.change_presence(status=discord.Status.online, activity=discord.Game('rps help'))
 print('Ready to play rps!')

@client.event
async def on_message(message):

  if message.content.startswith('rps'):
    await message.channel.send("Next time put rock, paper or scissors. Use 'rps help' for more info!")

  if message.content.startswith('rps help'):
    await message.channel.send("```Here are the commands:\nchoose rock\nchoose paper\nchoose scissors\n\n\nTo play do 'choose <pick one>\n\n\nHelp the developer by subscribing to his channel!:https://www.youtube.com/channel/UC3zy2aTAIyqsqYOu7C49f2A'```")

  if message.content.startswith('choose rock'):
    await message.channel.send('Hm....'+random.choice(rps))

  if message.content.startswith('choose scissors'):
    await message.channel.send('Hm....'+random.choice(rps))
  
  if message.content.startswith('choose paper'):
    await message.channel.send('Hm....'+random.choice(rps))




keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN) 