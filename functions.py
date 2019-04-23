import discord
import asyncio
import time
from discord.ext import commands

class functions:
    def __init__(self, bot):
        self.bot = bot
        
#ban&blacklist        
    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context = True)
    async def 쫒아내(self, ctx, member: discord.Member=None):
        if not member:
            await self.bot.say('존재자체가 없습니다.')
            return
        await self.bot.kick(member)
        await self.bot.say('{}(이)을 쫒아냈습니다.'.format(member))
    
    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context = True)
    async def 죽여(self, ctx, member: discord.Member=None):
        if not member:
            await self.bot.say('존재자체가 없습니다.')
        await self.bot.ban(member)
        await self.bot.say('{}(이)가 죽었습니다.'.format(member))
        await asyncio.sleep(1)
        await self.bot.say('{}(은)는 더이상 돌아오지 못합니다.'.format(member))

def setup(bot):
    bot.add_cog(functions(bot))
    print('기능 파일이 준비되었습니다.')
