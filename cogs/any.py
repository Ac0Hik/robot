import discord
from discord.ext import commands
from asyncio import sleep



class any(commands.Cog):


  def __innit__(self, bot):
     self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('any is ready')
    print('--------------')
    


  @commands.command(aliases = ['countdown','Count', 'COUNT'], help = "counts down from a number\n:param: number[Default 10]")
  async def count(self, ctx, count: int = 10 ):
    await ctx.send(content = f'counting down from {count}')
    message = await ctx.send(content = f'{count}')
    count -= 1
  
    while count >= 0:
      await sleep(1)
      await message.edit(content = f'{count}')
      count -= 1
    await ctx.reply('countdown is over')

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author.bot:#a message sent by a bot ignore
      print('message was sent by a bot')
      return
    print(self.bot.user)
    async for entry in message.guild.audit_logs(limit=10, action=discord.AuditLogAction.message_delete):
      if (entry.user == self.bot.user and entry.target == message.author) :#the bot deleted a user's message and the user is the message that triggered the event author 
        print(f'the message of {entry.target} was deleted by the bot ')
        print(f'this message should be ignored\ncontent: {message.content}')
        return


    #add message to dict (we are not going to do that till the event works as it;s supposed to 
    print(f'the message to add to the dict : {message.content}')


async def setup(bot):
  await bot.add_cog(any(bot))