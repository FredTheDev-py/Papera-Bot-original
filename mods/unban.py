import discord
from discord.ext import commands

class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")


    @commands.command(aliases=["unban"], name="Unban", description="sbanna gli utenti", usage="{prefix}unban/sban @user | <motivo opzionale>")
    @commands.has_any_role('Generale', 'Senato Imperiale', 'Imperatori')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                
                embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", color=discord.Color.green())
                embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(697515044593729586)
                embed = discord.Embed(title="[MODERAZIONE]", color=discord.Color.blue())
                embed.add_field(name="Comando eseguito:", value=f"{self.__class__.__name__}", inline=True)
                embed.add_field(name="Utente moderato:", value=f"{member}\n{member.id}")
                embed.add_field(name="Moderatore:", value=f"{ctx.message.author.mention}")
                await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Unban(bot))