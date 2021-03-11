import discord
from discord.ext import commands

class CommandErros(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRole):
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non possiedi i permessi requisiti.**", color=discord.Color.red())
            await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(CommandErros(bot))