from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class Nft(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="nft", description="Replies with the NFT's copypasta.", guild_ids=[1046702726886735935, 1005944053038321826])
    async def nft(self, inter: Interaction) -> None:
        await inter.send("Fucking plastic balls. Mid. Instead lf trying to be cool π€π€π how about you invest in NFTs ππ― π΅  earn some bands π₯Άπ₯Άπ±ππ π΅ and become an entrepreneur. π΄πππ₯Άπ₯Άπ΄π΄πͺπͺπ₯΅π₯΅π₯΅π₯Άπππππ₯±π₯±. Live the top G lifestyle mate. πππππ€©π€©πππ₯΅π₯΅π₯΅π₯³π₯³π₯Άπ₯Άπ₯Άπ₯Ά")
        
def setup(bot: Bot) -> None:
    bot.add_cog(Nft(bot))