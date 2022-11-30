from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog


class Nft(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="nft", description="Replies with the NFT's copypasta.", guild_ids=[1046702726886735935, 1005944053038321826])
    async def nft(self, inter: Interaction) -> None:
        await inter.send("Fucking plastic balls. Mid. Instead lf trying to be cool 🤐🤐😂 how about you invest in NFTs 😃💯 💵  earn some bands 🥶🥶😱😈😈 💵 and become an entrepreneur. 😴😎😎🥶🥶😴😴😪😪🥵🥵🥵🥶😎😎😎😎🥱🥱. Live the top G lifestyle mate. 😇😇😉😊🤩🤩😍😍🥵🥵🥵🥳🥳🥶🥶🥶🥶")
        
def setup(bot: Bot) -> None:
    bot.add_cog(Nft(bot))