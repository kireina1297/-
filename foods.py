import discord
from discord.ext import commands

class foods:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    async def 우유(self, ctx):
        channel = ctx.message.channel
        await self.bot.send_message(channel, ':milk:')
        
    @commands.command(pass_context = True)
    async def 밥(self, ctx):
        channel = ctx.message.channel
        await self.bot.send_message(channel, ':fish::milk:')
        
    @commands.command(pass_context = True)
    async def 녹차(self, ctx):
        channel = ctx.message.channel
        await self.bot.send_message(channel, ':tea:')
        
def setup(bot):
    bot.add_cog(foods(bot))
    print('음식 파일이 준비되었습니다.')