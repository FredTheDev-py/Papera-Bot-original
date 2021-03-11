import discord
from discord.ext import commands
import datetime

class MemberLoggin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):

        embed = discord.Embed(colour=discord.Color.blue(), description="**Nuovo Utente è entrato\nGeneralità:**")
        
        embed.add_field(name="Nome completo:", value=f"{member}", inline=False)
        embed.add_field(name="ID:", value=f"{member.id}", inline=False)
        embed.add_field(name="Data creazione account", value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=False)
        embed.add_field(name="Data di entrata", value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=False)

        embed.set_footer(text="In caso l'account fosse stato appena creato è consigliato di monitorarlo e prefibilmente bannarlo dato che in maggiori casi si tratta di alt per raidare.")
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()

        channel = self.bot.get_channel(800324077256572928)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MemberLoggin(bot))