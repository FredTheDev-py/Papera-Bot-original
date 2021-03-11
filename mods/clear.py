import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n=======================================\n{self.__class__.__name__} is ready!")


    @commands.command(aliases=["clear"], name="Clear", description="cancella i messaggi", usage="{prefix}clear <cifra numerica>")
    @commands.has_any_role("Agente Paperoso", "Guardia Imperiale", "Tenente Colonnello", "Generale", "Senato Imperiale", "Imperatori")
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title="Comando eseguito con successo! :white_check_mark:", description=f"**{amount} messaggi cancellati.**", color=discord.Color.green())
        embed.set_author(name=f"[{self.__class__.__name__}]", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed, delete_after=5)



    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.send(f"```{error}```")

def setup(bot):
    bot.add_cog(Clear(bot))