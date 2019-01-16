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

bot = commands.Bot('세바스찬,')#봇 명령 코드

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Yes, My Lord'))#봇 상태메세지
    print('봇이 준비되었습니다.주인님')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='직원')#자동 역할 부여
    await bot.add_roles(member, role)
    
@bot.event
async def on_message(message):
    chanel - message.channel
    if message.content.startswith('우유)
    await bot.send._message(chanel, 'milk:')
    
bot.run(os.environ['TOKEN'])
