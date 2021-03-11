import discord
from discord.ext import commands

class Libera(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")


    @commands.command(aliases=["libera"], name="Libera", description="muta gli utenti", usage="{prefix}bang @user | <motivo opzionale>")
    async def libera(self, ctx, member : discord.Member, *, reason=None):
        if member.guild_permissions.manage_messages:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non è possibile moderare un Moderatore/Admin.**", color=discord.Color.red())
            await ctx.send(embed=embed)
        
        elif ctx.message.author.guild_permissions.manage_messages:
            if reason is None:
                Papera_Cittadina = discord.utils.get(ctx.guild.roles, name="Papera Cittadina")
                Prigioniero = discord.utils.get(ctx.guild.roles, name="Prigioniero")
                await member.remove_roles(Prigioniero)
                await member.add_roles(Papera_Cittadina)

                channel = self.bot.get_channel(697514996627931236)
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

                await member.send(f"Sei stato smutato nell'**Impero delle Papere**, ora puoi tornare a chattare!")

            else:
                Papera_Cittadina = discord.utils.get(ctx.guild.roles, name="Papera Cittadina")
                Prigioniero = discord.utils.get(ctx.guild.roles, name="Prigioniero")
                await member.remove_roles(Prigioniero)
                await member.add_roles(Papera_Cittadina)

                channel = self.bot.get_channel(697514996627931236)
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

                await member.send(f"Sei stato smutato nell'**Impero delle Papere**, ora puoi tornare a chattare!")
        else:
            embed = discord.Embed(title=":no_entry_sign: Comando non eseguito.", description="**Non possiedi i permessi requisiti.**", color=discord.Color.red())
            await ctx.send(embed=embed)

        

def setup(bot):
    bot.add_cog(Libera(bot))