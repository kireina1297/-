import discord
import asyncio
import os
from discord import opus
from discord.ext import commands
from discord.ext.commands import Bot
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

#봇 명령 코드
bot = commands.Bot('세바스찬, ')
bot.remove_command('도')

extensions = ['foods', 'functions']

@bot.event
async def on_ready():
    #await bot.change_presence(game=discord.Game(name='Yes, My Lord'))#봇 상태메세지
   game = discord.Game("Yes, My Lord")
   print("봇이 준비되었습니다.주인님")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='')#자동 역할 부여
    await bot.add_roles(member, role)
   
@bot.command(pass_context = True)
async def 도와줘(ctx):
    channel = ctx.message.channel

    hm = discord.Embed(
        title = '도움이 필요하십니까?/모든 명령어는 리메이크 예정입니다.',
        color = 0xffffff
    )
    hm.add_field(name='우유:milk:', value='우유를 가져다 드리겠습니다.', inline=True)
    hm.add_field(name='밥:fish::milk:', value='우유와 생선을 가져다 드리겠습니다.', inline=True)
    hm.add_field(name='녹차:tea:', value='녹차를 끓여오겠습니다.', inline=True)
    hm.add_field(name='카레:curry:', value='카레를 가져다 드리겠습니다.', inline=True)
    await bot.send_message(channel, embed=hm)
    
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{}(이)가 준비되지 않았습니다. [{}]'.format(extension, error))


bot.run(os.environ['TOKEN'])
