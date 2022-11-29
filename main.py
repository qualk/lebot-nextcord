import nextcord
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
    
    elif 'fogor' in message.content.lower():
      await message.add_reaction('\N{skull}')
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
  
    else:
      return


client.run(os.getenv("TOKEN"))