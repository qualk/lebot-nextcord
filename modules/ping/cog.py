from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="ping", description="Replies with pong and bot latency.", guild_ids=[1046702726886735935, 1005944053038321826])
    async def ping(self, inter: Interaction) -> None:
        await inter.send(f"Pong! {self.bot.latency * 1000:.2f}ms")
           
def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))