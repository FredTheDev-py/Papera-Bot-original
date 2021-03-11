import discord
from discord.ext import commands
import re
import os
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")

   
    @commands.Cog.listener()
    async def on_message(self, message, *cog):
      if message.author == self.bot.user:
        return

      if message.content == "q!help":
        embed = discord.Embed( 
            title=f"Comandi del {self.bot.user.name}",
            description=f"**Prefix** = `{self.bot.command_prefix}`\nPer avere maggiori informazioni su ogni comando digita **`{self.bot.command_prefix}help <nome comando>`**",
            color=discord.Color.blue())
        
        if len(cog)==0:
            cog = ("Ban", "Unban", "Kick", "Bang", "Libera")
        
        for i in cog:
            try:
                for command in self.bot.get_cog(i).get_commands():
                    embed.add_field(name=f"{command.name} - {command.description}.", value=f"↳ **Sintassi:** `{command.usage}`", inline=False)
            except:
                pass # What will happen if cog is unloaded, or nothing with pass
        
        embed.set_thumbnail(url=f'https://cdn.discordapp.com/attachments/654396431381037077/664597902840037376/scudo.png')
        embed.set_footer(text="Pagina 1/2, per proseguire digita <q!help numero>", icon_url=f'https://cdn.discordapp.com/attachments/651185347597828099/678964560673374208/quack.png')
        embed.timestamp = datetime.datetime.utcnow()
        
        await message.channel.send(embed=embed)
        
      elif message.content.startswith("q!help 2"):
        embed = discord.Embed( 
            title=f"Comandi del {self.bot.user.name}",
            description=f"**Prefix** = `{self.bot.command_prefix}`\nPer avere maggiori informazioni su ogni comando digita **`{self.bot.command_prefix}help <nome comando>`**",
            color=discord.Color.blue())
        
        if len(cog)==0:
            cog = ("Clear", "Close", "Open", "Lock", "Unlock")
        
        for i in cog:
            try:
                for command in self.bot.get_cog(i).get_commands():
                    embed.add_field(name=f"{command.name} - {command.description}.", value=f"↳ **Sintassi:** `{command.usage}`", inline=False)
            except:
                pass # What will happen if cog is unloaded, or nothing with pass
        
        embed.set_thumbnail(url=f'https://cdn.discordapp.com/attachments/654396431381037077/664597902840037376/scudo.png')
        embed.set_footer(text="Pagina 2/2", icon_url=f'https://cdn.discordapp.com/attachments/651185347597828099/678964560673374208/quack.png')
        embed.timestamp = datetime.datetime.utcnow()
        
        await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))