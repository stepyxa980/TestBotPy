import datetime

import disnake
from disnake.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def timeout(self, interaction, member: disnake.Member, time: str, reason: str):
        time_now = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        try:
            await member.timeout(reason=reason, until=time_now)
        except:
            await interaction.response.send_message("Missing Permissions")
        await interaction.response.send_message(f"Вы выдали пользователю >> {member.mention} таймаут на {time} минут по причине {reason}")

def setup(bot):
    bot.add_cog(Test(bot))