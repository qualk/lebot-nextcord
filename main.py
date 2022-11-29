import nextcord
#from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True

client = nextcord.Client(intents=intents)

TOKEN = os.environ.get('TOKEN')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=nextcord.Status.idle, activity=nextcord.Game("with qualk's balls"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith('$ping'):
        await message.channel.send('Pong!', reference=message)

    elif message.content.startswith('$your'):
        await message.channel.send('mum', reference=message)
        
    elif message.content.startswith('$deez'):
        await message.channel.send('nuts', reference=message)
        
    elif message.content.startswith('$skill'):
        await message.channel.send('issue', reference=message)
        
    elif message.content.startswith('$lester'):
        await message.channel.send(file=nextcord.File('assets\\images\\lester.jpg'), reference=message)
    
    elif 'fogor' in message.content.lower():
      await message.add_reaction('\N{skull}')
      return
    
    elif 'yum' in message.content.lower():
      await message.add_reaction('😋')
      return
  
    elif 'did i ask' in message.content.lower():
      await message.channel.send('shut the fuck up', reference=message)
      return
  
    elif 'when' in message.content.lower():
      await message.channel.send('Did u mean wenomechaindasama?', reference=message)
      await message.channel.send(file=nextcord.File('assets\\images\\wenomechainsama.jpg'))
      return
  
    elif '?' in message.content.lower():
      await message.channel.send(
        'Teacher I suspect the answer to your question is four teacher', reference=message)
      await message.channel.send(file=nextcord.File('assets\\images\\four.jpg'))
      return
    
    elif 'cena' in message.content.lower():
      await message.channel.send('Zǎoshang hǎo zhōngguó xiànzài wǒ yǒu BING CHILLING 🥶🍦 wǒ hěn xǐhuān BING CHILLING 🥶🍦 dànshì sùdù yǔ jīqíng 9 bǐ BING CHILLING 🥶🍦 sùdù yǔ jīqíng sùdù yǔ jīqíng 9 wǒ zuì xǐhuān suǒyǐ…xiànzài shì yīnyuè shíjiān zhǔnbèi 1 2 3 liǎng gè lǐbài yǐhòu sùdù yǔ jīqíng 9 ×3 bùyào wàngjì bùyào cu òguò jìdé qù diànyǐngyuàn kàn sùdù yǔ jīqíng 9 yīn wéi fēicháng hǎo diànyǐng dòngzuò fēicháng hǎo chàbùduō yīyàng BING CHILLING 🥶🍦zàijiàn 🥶🍦', reference=message)
      return
    
    elif 'hot' in message.content.lower():
      await message.channel.send('Fucking plastic chigger balls. Mid. Instead lf trying to be cool 🤐🤐😂 how about you invest in NFTs 😃💯 💵  earn some bands 🥶🥶😱😈😈 💵 and become an entrepreneur. 😴😎😎🥶🥶😴😴😪😪🥵🥵🥵🥶😎😎😎😎🥱🥱. Live the top G lifestyle mate. 😇😇😉😊🤩🤩😍😍🥵🥵🥵🥳🥳🥶🥶🥶🥶', reference=message)
  
    else:
      return

client.run(os.getenv("TOKEN"))