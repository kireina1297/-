import discord
import asyncio
import time
from discord.ext import commands

class functions:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def 내보내(self, ctx, username: discord.User):
        await self.bot.kick(username)
        await self.bot.say('{}(이)가 퇴장되었습니다.'.format(username))
        
    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def 추방시켜(self, ctx, username: discord.User):
        await self.bot.ban(username)
        await self.bot.say('{}(이)가 추방되었습니다.'.format(username))
        await asyncio.sleep(1)
        await self.bot.say('{}(은)는 더이상 돌아오지 못합니다.'.format(username))

def setup(bot):
    bot.add_cog(functions(bot))
    print('기능 파일이 준비되었습니다.')
