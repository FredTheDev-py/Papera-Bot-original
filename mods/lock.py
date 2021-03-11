import discord
from discord.ext import commands


class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")
        
    
    @commands.command(aliases=["lock"], name="Lock", description="chiude tutte le stanze del server", usage="{prefix}lock")
    @commands.has_any_role('Generale', 'Senato Imperiale', 'Imperatori')
    async def lock(self, ctx):
        embed = discord.Embed(title="Comando eseguito con sucesso!", description="**Server chiuso momentaneamente per motivi di sicurezza!**",colour=discord.Color.green())
        await ctx.send(embed=embed)
        
        role = discord.utils.get(ctx.guild.roles, name='Papera Cittadina')

        channel = discord.utils.get(ctx.guild.channels, name='【🐤】piazza-generale')
        await channel.set_permissions(role, send_messages=False)

        channel = discord.utils.get(ctx.guild.channels, name='【⌨】piazza-spam')
        await channel.set_permissions(role, send_messages=False)

        channel = discord.utils.get(ctx.guild.channels, name='【😂】meme')
        await channel.set_permissions(role, send_messages=False)

        channel = discord.utils.get(ctx.guild.channels, name='【🎨】museo-disegni')
        await channel.set_permissions(role, send_messages=False)

        channel = discord.utils.get(ctx.guild.channels, name='【💻】ufficio-papere-inc')
        await channel.set_permissions(role, send_messages=False)         

        channel = discord.utils.get(ctx.guild.channels, name='【📨】suggerimenti')
        await channel.set_permissions(role, send_messages=False)

        channel = discord.utils.get(ctx.guild.channels, name='【🏹】risposta')
        await channel.set_permissions(role, send_messages=False)

        channel = discord.utils.get(ctx.guild.channels, name='【🎶】discoteca-paperosa')
        await channel.set_permissions(role, send_messages=False)

        channel = channel = self.bot.get_channel(697514964897759333)
        await channel.set_permissions(role, send_messages=False)

        channel = channel = self.bot.get_channel(697514966521086045)
        await channel.set_permissions(role, send_messages=False)

        channel = channel = self.bot.get_channel(697514969033342986)
        await channel.set_permissions(role, send_messages=False)

        channel = channel = self.bot.get_channel(743434498598895644)
        await channel.set_permissions(role, send_messages=False)

        channel = channel = self.bot.get_channel(697514975865864192)
        await channel.set_permissions(role, send_messages=False)

        channel = channel = self.bot.get_channel(760582600652881940)
        await channel.set_permissions(role, send_messages=False)


        channel = self.bot.get_channel(697515044593729586)
        embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
        embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
        embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Lock(bot))