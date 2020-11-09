# bot.py
# driver for the bot
# is the brains of this whole operation

import os
import sys
import random, json
import discord
import aiohttp

from discord.ext import commands

from dotenv import load_dotenv
#add memebers = True
intents = discord.Intents(guilds = True, members = True, emojis = True, messages = True, reactions = True, typing = True)

load_dotenv()
TOKEN = os.getenv('IKA_TOKEN') #obtains bot token from .env file

bot = commands.Bot(command_prefix = ('m.', '<@!705683895055679521>', '<@!705683895055679521> ', 'M.'), intents = intents)
bot.remove_command('help')


@bot.command() # live load cogs
async def load(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  else:
    await ctx.message.add_reaction('👍')
    bot.load_extension(f'commands.{extension}')


@bot.command() # live unload cogs
async def unload(ctx, extension):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  else:
    await ctx.message.add_reaction('👍')
    bot.unload_extension(f'commands.{extension}')


@bot.command()
async def reload(ctx, extension = ''):
  if ctx.author.id != 275065846836101120:
    await ctx.message.add_reaction('👎')
    return
  
  #reloads all cogs if no extension is spefically given
  elif extension == '':
    for filename in os.listdir('./commands/general'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.general.{filename[:-3]}')

    for filename in os.listdir('./commands/img'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.img.{filename[:-3]}')

    for filename in os.listdir('./commands/mal_anilist'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.mal_anilist.{filename[:-3]}')

    for filename in os.listdir('./commands/misc'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.misc.{filename[:-3]}')

    for filename in os.listdir('./commands/src'):
      if filename.endswith('.py'):
        bot.reload_extension(f'commands.src.{filename[:-3]}')

    await ctx.message.add_reaction('👍')


  else:
    await ctx.message.add_reaction('👍')
    bot.reload_extension(f'commands.{extension}')






#Load all cogs when bot starts
for filename in os.listdir('./commands/general'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.general.{filename[:-3]}')

for filename in os.listdir('./commands/img'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.img.{filename[:-3]}')

for filename in os.listdir('./commands/mal_anilist'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.mal_anilist.{filename[:-3]}')

for filename in os.listdir('./commands/misc'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.misc.{filename[:-3]}')

for filename in os.listdir('./commands/src'):
  if filename.endswith('.py'):
    bot.load_extension(f'commands.src.{filename[:-3]}')


bot.run(TOKEN)
