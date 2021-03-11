import discord
from discord.ext import commands


class Helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self, ):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")

    @commands.group()
    async def help(self, ctx):
        pass

    @help.command()
    async def ban(self, ctx):
        for command in self.bot.get_cog("Ban").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```BAN, @GENERALE - @SENATO IMPERIALE - @IMPERATORI```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)

    @help.command()
    async def unban(self, ctx):
        for command in self.bot.get_cog("Unban").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```BAN, @GENERALE - @SENATO IMPERIALE - @IMPERATORI```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)
            

    @help.command()
    async def kick(self, ctx):
        for command in self.bot.get_cog("Kick").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```KICK, @GUARDIA IMPERIALE - @TENENTE COLONELLO +```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)




    @help.command()
    async def bang(self, ctx):
        for command in self.bot.get_cog("Bang").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```GESTIONE MESSAGGI, @AGENTE PAPEROSO - @GUARDIA IMPERIALE - @TENENTE COLONELLO +```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)



    @help.command()
    async def libera(self, ctx):
        for command in self.bot.get_cog("Libera").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```GESTIONE MESSAGGI, @AGENTE PAPEROSO - @GUARDIA IMPERIALE - @TENENTE COLONELLO +```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)


    @help.command()
    async def close(self, ctx):
        for command in self.bot.get_cog("Close").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```@PAPERA BOT PERMISSIONS```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)


    @help.command()
    async def open(self, ctx):
        for command in self.bot.get_cog("Open").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```@PAPERA BOT PERMISSIONS```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed) 





    @help.command()
    async def lock(self, ctx):
        for command in self.bot.get_cog("Lock").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```@PAPERA BOT PERMISSIONS```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)



    @help.command()
    async def unlock(self, ctx):
        for command in self.bot.get_cog("Unlock").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```@PAPERA BOT PERMISSIONS```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)

    
    @help.command()
    async def clear(self, ctx):
        for command in self.bot.get_cog("Clear").get_commands():
            embed = discord.Embed(title=f"Info Comando {command.name}", 
            description=f"**Uso:** {command.description}\n**Sintassi:** ```{command.usage}```\n**Permessi e Ruoli:** ```GESTIONE MESSAGGI, @AGENTE PAPEROSO```", 
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Helpcmd(bot))