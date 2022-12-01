import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class Lester(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="lester", description="gives an image of a discord mod", guild_ids=[1046702726886735935, 1005944053038321826, 941837967654256701])
    async def when(self, inter: Interaction) -> None:
        await inter.send(files=[nextcord.File("D:\\home\\Documents\\GitHub\\lebot-nextcord\\assets\\images\\lester.jpg")])
        
def setup(bot: Bot) -> None:
    bot.add_cog(Lester(bot))