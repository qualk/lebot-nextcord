import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
import os
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True

bot = Bot(intents=intents)
bot.load_extensions([
  "modules.ping.cog",
  "modules.jokes.deez.cog",
  "modules.jokes.copypastas.nft.cog",
  "modules.jokes.copypastas.cena.cog",
  "modules.jokes.when.cog",
  "modules.jokes.lester.cog"])

print(bot.extensions)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Game("with qualk's balls"))
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    elif 'fogor' in message.content.lower():
      await message.add_reaction('💀')
      return
    
    elif 'yum' in message.content.lower():
      await message.add_reaction('😋')
      return
  
    elif 'did i ask' in message.content.lower():
      await message.channel.send('shut the fuck up', reference=message)
      return
  
    # elif 'when' in message.content.lower():
    #   await message.channel.send('Did u mean wenomechaindasama?', file=nextcord.File('assets\\images\\wenomechainsama.jpg'), reference=message)
    #   return
    
    elif 'cena' in message.content.lower():
      await message.channel.send('Zǎoshang hǎo zhōngguó xiànzài wǒ yǒu BING CHILLING 🥶🍦 wǒ hěn xǐhuān BING CHILLING 🥶🍦 dànshì sùdù yǔ jīqíng 9 bǐ BING CHILLING 🥶🍦 sùdù yǔ jīqíng sùdù yǔ jīqíng 9 wǒ zuì xǐhuān suǒyǐ…xiànzài shì yīnyuè shíjiān zhǔnbèi 1 2 3 liǎng gè lǐbài yǐhòu sùdù yǔ jīqíng 9 ×3 bùyào wàngjì bùyào cu òguò jìdé qù diànyǐngyuàn kàn sùdù yǔ jīqíng 9 yīn wéi fēicháng hǎo diànyǐng dòngzuò fēicháng hǎo chàbùduō yīyàng BING CHILLING 🥶🍦zàijiàn 🥶🍦', reference=message)
      return
    
    elif 'hot' in message.content.lower():
      await message.channel.send('Fucking plastic balls. Mid. Instead lf trying to be cool 🤐🤐😂 how about you invest in NFTs 😃💯 💵  earn some bands 🥶🥶😱😈😈 💵 and become an entrepreneur. 😴😎😎🥶🥶😴😴😪😪🥵🥵🥵🥶😎😎😎😎🥱🥱. Live the top G lifestyle mate. 😇😇😉😊🤩🤩😍😍🥵🥵🥵🥳🥳🥶🥶🥶🥶', file=nextcord.File('assets\\images\\cena.jpg'), reference=message)

    elif '?' in message.content.lower():
      await message.channel.send('Teacher I suspect the answer to your question is four teacher', file=nextcord.File('assets\\images\\four.jpg'), reference=message)
      return
     
    else:
      return

bot.run(os.getenv("TOKEN"))