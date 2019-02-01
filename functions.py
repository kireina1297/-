import discord
import asyncio
import time
from discord.ext import commands

class functions:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def 내보내(self, ctx, member: discord.Member=None):
        if not member:
            await self.bot.say('정확한 사람을 골라야합니다.')
            return
        await member.kick()
        await self.bot.say('{}(이)가 퇴장되었습니다.'.format(member))
        
    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def 추방시켜(self, ctx, member: discord.Member=None):
        if not member:
            await self.bot.say('정확한 사람을 골라야합니다.')
        await member.ban()
        await self.bot.say('{}(이)가 추방되었습니다.'.format(member))
        await asyncio.sleep(1)
        await self.bot.say('{}(은)는 더이상 돌아오지 못합니다.'.format(member))

def setup(bot):
    bot.add_cog(functions(bot))
    print('기능 파일이 준비되었습니다.')
