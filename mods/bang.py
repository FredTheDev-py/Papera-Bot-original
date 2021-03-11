import discord
from discord.ext import commands
import asyncio

class Bang(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")


    @commands.command(aliases=["bang"], name="Bang", description="muta gli utenti", usage="{prefix}bang @user | <motivo opzionale>")
    async def bang(self, ctx, member : discord.Member, *, reason=None):
        if member.guild_permissions.manage_messages:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non è possibile moderare un Moderatore/Admin.**", color=discord.Color.red())
            await ctx.send(embed=embed)
        
        elif ctx.message.author.guild_permissions.manage_messages:
              if reason is None:
                  Papera_Cittadina = discord.utils.get(ctx.guild.roles, name="Papera Cittadina")
                  Prigioniero = discord.utils.get(ctx.guild.roles, name="Prigioniero")
                  await member.remove_roles(Papera_Cittadina)
                  await member.add_roles(Prigioniero)

                  channel = self.bot.get_channel(697514996627931236)
                  embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", description=f"**{member.mention} è rinchiuso in {channel.mention}.**", color=discord.Color.green())
                  embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
                  await ctx.send(embed=embed)

                  channel = self.bot.get_channel(697515044593729586)
                  embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
                  embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
                  embed.add_field(name="Utente moderato:", value=f"{member}\n{member.id}")
                  embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
                  embed.add_field(name="Motivo:", value="nessun motivo")
                  await channel.send(embed=embed)

                  await member.send(f"Sei stato mutato nell'**Impero delle Papere** per il seguente motivo: **{reason}**\n a breve decideremo se smutarti o no\n in caso ritieni di essere stato mutato ingiustamente contatta un admin del server.")

              else:
                  Papera_Cittadina = discord.utils.get(ctx.guild.roles, name="Papera Cittadina")
                  Prigioniero = discord.utils.get(ctx.guild.roles, name="Prigioniero")
                  await member.remove_roles(Papera_Cittadina)
                  await member.add_roles(Prigioniero)

                  channel = self.bot.get_channel(697514996627931236)
                  embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", description=f"**{member.mention} è rinchiuso in {channel.mention}.**", color=discord.Color.green())
                  embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
                  await ctx.send(embed=embed)

                  channel = self.bot.get_channel(697515044593729586)
                  embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
                  embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
                  embed.add_field(name="Utente moderato:", value=f"{member}\n{member.id}")
                  embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
                  embed.add_field(name="Motivo:", value=f"{reason}")
                  await channel.send(embed=embed)

                  await member.send(f"Sei stato mutato nell'**Impero delle Papere** per il seguente motivo: **{reason}**\n a breve decideremo se smutarti o no\n in caso ritieni di essere stato mutato ingiustamente contatta un admin del server.")
        else:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non possiedi i permessi requisiti.**", color=discord.Color.red())
            await ctx.send(embed=embed)

    @bang.error
    async def bang_error(self, ctx, error):
        await ctx.send(f"```{error}```")

def setup(bot):
    bot.add_cog(Bang(bot))