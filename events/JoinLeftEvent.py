import discord
from discord.ext import commands
import datetime

class JoinLeft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name='Papera Cittadina')
        await member.add_roles(role)

        channel = self.bot.get_channel(697514940461875200)
        channel_id = self.bot.get_channel(697514947126624428)
        embed = discord.Embed(colour=discord.Color.gold(), description=f"Hey! **{member.name}** benvenuto nell'**Impero delle Papere**!\n__Dopo aver letto le__ {channel.mention} __puoi conversare in__ {channel_id.mention}\n\n**Membro numero:** `{len(list(member.guild.members))}`")
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_author(name=f'{member}', icon_url=f'{member.avatar_url}')
        embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
        embed.timestamp = datetime.datetime.utcnow()
        """embed.add_field(name='**I nostri social!**', value=f"[Instagram](https://www.instagram.com/insta_delle_papere/), [Youtube](https://www.youtube.com/channel/UC6qRW-4vV4uMvegskiezdyQ), [Twich](https://www.twitch.tv/paese_delle_papere?sr=a), [Reddit](https://www.reddit.com/r/PaeseDellePapere/) e [PayPal](https://paypal.me/imperodellepapere)")"""

        channel = self.bot.get_channel(697514939685929030)
        await channel.send(embed=embed)

        embed = discord.Embed(description="Hey benvenuto/a nell'**Impero delle Papere!** leggi le <#697514940461875200> prima di cominciare a chattare e buona permanenza!", color=discord.Color.gold())
        await member.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(697514939685929030)
        embed = discord.Embed(colour=discord.Color.gold(), description=f'Rip! **{member}** ha deciso di lasciarci :pensive:')
        channel = self.bot.get_channel(697514939685929030)
        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(JoinLeft(bot))