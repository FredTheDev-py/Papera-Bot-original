import discord
from discord.ext import commands
import task
from discord import Embed
from discord.utils import get
import asyncio
import sys
import os
from discord.ext import tasks
import webserver
from webserver import keep_alive

bot = commands.Bot(command_prefix = "q!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Papera bot vive, vive e vivrà!")
    await bot.change_presence(activity=discord.Game("q!help / q!help <comando>"))
    #giorgio.start()
    #channel = bot.get_channel(697514947126624428)
    #await channel.send("FILIPPO ARGENTI")

"""@tasks.loop(minutes=5)
async def giorgio():
    channel = bot.get_channel(697514947915284529)
    await channel.send("fine, grazie per i 000000 iscritti.")"""

@bot.command()
@commands.has_any_role("IDP Studios", "IDP Bot Studios")
async def load(ctx, extension):
    bot.load_extension(f"mods.{extension}")
    await ctx.send(f"```il comando {extension} è stato attivato!```")

@bot.command()
@commands.has_any_role("IDP Studios", "IDP Bot Studios")
async def unload(ctx, extension):
    bot.unload_extension(f"mods.{extension}")
    await ctx.send(f"```il comando {extension} è stato disattivato!```")

@bot.command()
@commands.has_any_role("IDP Studios", "IDP Bot Studios")
async def reload(ctx, extension):
    bot.unload_extension(f"mods.{extension}")
    bot.load_extension(f"mods.{extension}")
    await ctx.send(f"```il comando {extension} è stato aggiornato!```")

@bot.command()
@commands.has_any_role("IDP Studios", "IDP Bot Studios")
async def rreload(ctx, extension):
    bot.unload_extension(f"info.{extension}")
    bot.load_extension(f"info.{extension}")
    await ctx.send(f"```il comando {extension} è stato aggiornato!```")

@bot.command()
async def blacklist(ctx, member: discord.Member):
  file =  open("banned.txt", "a")#
  file.write(member.id)
  file.close()
  await ctx.send(f"{member} has been added to the blacklist")



@bot.command(aliases=['eval'])
@commands.has_role("Papera Bot")
async def _eval(ctx, *, msg):
  msg = msg.replace("“", "\"")
  msg = msg.replace("‘", "'")
  try:
    if "await ctx.send" not in msg:
      await ctx.send(eval(msg))

    else:
      exec(
        f'async def __ex(ctx): ' +
        ''.join(f'\n {l}' for l in msg.split('\n'))
      )
      return await locals()['__ex'](ctx)
    
  except Exception as e:
    await ctx.send(f'```py\n{e}\n```')


for filename in os.listdir("./mods"):
    if filename.endswith(".py"):
        bot.load_extension(f"mods.{filename[:-3]}")

for filename in os.listdir("./info"):
    if filename.endswith(".py"):
        bot.load_extension(f"info.{filename[:-3]}")

for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        bot.load_extension(f"events.{filename[:-3]}")

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
