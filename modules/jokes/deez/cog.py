from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog


class Deez(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="deez", description="You know what it replies with...", guild_ids=[1046702726886735935, 1005944053038321826])
    async def deez(self, inter: Interaction) -> None:
        await inter.send("nuts!")
        
def setup(bot: Bot) -> None:
    bot.add_cog(Deez(bot))