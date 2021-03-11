import discord
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")


    @commands.command(aliases=["kick"], name="Kick", description="espelle gli utenti", usage="{prefix}kick @user | <motivo opzionale>")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if member.guild_permissions.manage_messages:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non è possibile moderare un Moderatore/Admin.**", color=discord.Color.red())
            await ctx.send(embed=embed)
        
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await member.kick(reason=None)
                
                embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", color=discord.Color.green())
                embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(697515044593729586)
                embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
                embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
                embed.add_field(name="Utente moderato:", value=f"{member}\n{member.id}")
                embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
                embed.add_field(name="Motivo:", value="nessun motivo")
                await channel.send(embed=embed)

            else:
                await member.kick(reason=reason)
                
                embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", color=discord.Color.green())
                embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(697515044593729586)
                embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
                embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
                embed.add_field(name="Utente moderato:", value=f"{member}\n{member.id}")
                embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
                embed.add_field(name="Motivo:", value=f"{reason}")
                await channel.send(embed=embed)
        else:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non possiedi i permessi requisiti.**", color=discord.Color.red())
            await ctx.send(embed=embed)

        

def setup(bot):
    bot.add_cog(Kick(bot))