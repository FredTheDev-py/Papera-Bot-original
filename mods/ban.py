import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")
    

    @commands.command(aliases=["ban"], name="Ban", description="banna gli utenti", usage="{prefix}ban @user | <motivo opzionale>")
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if member.guild_permissions.manage_messages:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non è possibile moderare un Moderatore/Admin.**", color=discord.Color.red())
            await ctx.send(embed=embed)
        
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await member.send("Sei stato bannato dall'**Impero delle Papere**.\n se ritieni di essere stato bannato ingiustamente contatta un admin del server.")
                await member.ban(reason=None, delete_message_days=0)

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
                await member.send(f"Sei stato bannato dall'**Impero delle Papere** per il seguente motivo: **{reason}**\n se ritieni di essere stato bannato ingiustamente contatta un admin del server.")
                await member.ban(reason=reason, delete_message_days=0)

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
    bot.add_cog(Ban(bot))