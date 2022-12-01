import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

cena = "Zǎoshang hǎo zhōngguó xiànzài wǒ yǒu BING CHILLING 🥶🍦 wǒ hěn xǐhuān BING CHILLING 🥶🍦 dànshì sùdù yǔ jīqíng 9 bǐ BING CHILLING 🥶🍦 sùdù yǔ jīqíng sùdù yǔ jīqíng 9 wǒ zuì xǐhuān suǒyǐ…xiànzài shì yīnyuè shíjiān zhǔnbèi 1 2 3 liǎng gè lǐbài yǐhòu sùdù yǔ jīqíng 9 ×3 bùyào wàngjì bùyào cu òguò jìdé qù diànyǐngyuàn kàn sùdù yǔ jīqíng 9 yīn wéi fēicháng hǎo diànyǐng dòngzuò fēicháng hǎo chàbùduō yīyàng BING CHILLING 🥶🍦zàijiàn 🥶🍦"

class Cena(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="cena", description="Replies with the John Cena ice-cream copypasta.", guild_ids=[1046702726886735935, 1005944053038321826])
    async def cena(self, inter: Interaction) -> None:
        await inter.send(cena, files=[nextcord.File("D:\\home\\Documents\\GitHub\\lebot-nextcord\\assets\\images\\cena.jpg")])
        
#    @cena.event
#    async def on_message(message):
#        if 'cena' in message.content.lower():
#            await message.channel.send(cena)
#            return   
        
def setup(bot: Bot) -> None:
    bot.add_cog(Cena(bot))