import disnake
from disnake.ext import commands

class Embit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def embed(self, interaction, member: disnake.Member):
        embed = disnake.Embed(title="Артём еврей!", description="Внимание неопровержимые доказательства!", color=0x00ff00)
        embed.set_author(name="Liho")
        embed.add_field(name="", value="1. Он любит деньги", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.set_footer(text="")
        embed.set_thumbnail(url=member.avatar.url)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Embit(bot))