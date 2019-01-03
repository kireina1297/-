import discord
import asyncio
import os
from discord import opus
from discord.ext import commands
from discord.voice_client import VoiceClient

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
 
def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
   
    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass
          
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
 
load_opus_lib()

bot = commands.Bot('')

@client.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='냥냥'))
    print('Bot is ready.')

bot.run(os.environ['TOKEN'])
