# https://github.com/regulad/SpiceBot

import discord, os, requests, json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print('Logged in as ' + str(bot.user.name) + '#' + str(bot.user.discriminator) + '(' + str(bot.user.id) + ')')

@bot.command(name='quote',description='Get Inspired!',aliases=['inspire'])
async def quote(ctx):
  response = requests.get("https://zenquotes.io/api/random")
  # We sucked at asyncio.
  await ctx.send(embed=discord.Embed(title=str(json.loads(response.text)[0]['q'] + " - " + json.loads(response.text)[0]['a'])))

@bot.command(name='ez',description='gg no re')
async def ez(ctx):
  await ctx.send("https://tenor.com/view/ez-yann-gauthier-gif-18979624")

@bot.command(name='real',description='get real')
async def real(ctx):
  await ctx.send("https://tenor.com/view/get-real-sexy-among-us-gif-19307656")
  
@bot.command(name='gummi',description='🐻🐻🐻🐻 🧟 👉😗👈 🌪',aliases=['gummy'])
async def gummi(ctx):
  await ctx.send("https://vm.tiktok.com/ZMJWJQCSH/")

@bot.command(name='derg',description='Nice doggy!',aliases=['dog'])
async def derg(ctx):
  await ctx.send(embed=discord.Embed(title="░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░\n░█░░░░░░░░▀▄░░░░░░▄░\n█░░▀░░▀░░░░░▀▄▄░░█░█\n█░▄░█▀░▄░░░░░░░▀▀░░█\n█░░▀▀▀▀░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n░█░░▄▄░░▄▄▄▄░░▄▄░░█░\n░█░▄▀█░▄▀░░█░▄▀█░▄▀░\n░░▀░░░▀░░░░░▀░░░▀░░░"))

bot.run(os.environ['BOT_TOKEN'])
