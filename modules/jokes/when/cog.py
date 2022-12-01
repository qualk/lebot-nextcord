import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog


class When(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="when", description="wenimechaindasuma", guild_ids=[1046702726886735935, 1005944053038321826, 941837967654256701])
    async def when(self, inter: Interaction) -> None:
        await inter.send('Did u mean wenomechaindasama?', files=[nextcord.File("D:\\home\\Documents\\GitHub\\lebot-nextcord\\assets\\images\\wenomechainsama.jpg")])
        
def setup(bot: Bot) -> None:
    bot.add_cog(When(bot))