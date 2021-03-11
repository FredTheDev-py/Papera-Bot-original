import discord
from discord.ext import commands

class Open(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")


    @commands.command(aliases=["open"], name="Open", description="apre la stanza dove viene eseguito il comando", usage="{prefix}open | <motivo opzionale>")
    @commands.has_role("Papera Bot permissions")
    async def open(self, ctx, *, reason=None):
        if reason is None:
            Papera_Cittadina = discord.utils.get(ctx.guild.roles, name="Papera Cittadina")
            await ctx.channel.set_permissions(Papera_Cittadina, send_messages=True)

            embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", description="**La stanza è stata aperta :unlock:**", color=discord.Color.green())
            embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)

            channel = self.bot.get_channel(697515044593729586)
            embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
            embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
            embed.add_field(name="Utente modificata:", value=f"{ctx.channel.mention}")
            embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
            embed.add_field(name="Motivo:", value="Nessun motivo")
            await channel.send(embed=embed)
        
        else:
            Papera_Cittadina = discord.utils.get(ctx.guild.roles, name="Papera Cittadina")
            await ctx.channel.set_permissions(Papera_Cittadina, send_messages=True)

            embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", description=f"**La stanza è stata aperta :unlock:**", color=discord.Color.green())
            embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)

            channel = self.bot.get_channel(697515044593729586)
            embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
            embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
            embed.add_field(name="Stanza modificata:", value=f"{ctx.channel.mention}")
            embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
            embed.add_field(name="Motivo:", value=f"{reason}")
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Open(bot))