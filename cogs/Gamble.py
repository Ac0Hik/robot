import discord
from discord.ext import commands
from random import randint


class Gamble(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    '''tells you when the Gabble cog is ready'''
    print('Gamble is ready')
    print('------------------------')


  def cf(self):
      return randint(0,1)

  @commands.command(aliases=["cf"], help="coin flip with no money (we trying to keep it halal guys)\nparam :bet:")
  async def coin_flip(self,ctx, bet: str):
      bets = ['heads', 'tails', 'h', 't']
      if bet.lower() not in bets:
          return await ctx.reply("invalid parameter [tails, heads, h, t]")
      bet = 1 if(bet == 'h' or bet == 'heads') else 0#parsing user's input to a a boolean value True for heads False for tailes
      bot_cf = self.cf()#bot's bet
      author = ctx.message.author
      bot_bet_value = 'heads' if bot_cf else 'tails' #heads of the bot chose 1 tailes otherwise
    
      if(bet == bot_cf):
          embed = discord.Embed(
          color = discord.Color.green()
          )
          embed.add_field(name= "you have won!", value = f"it's {bot_bet_value}")
          embed.set_author(name = author,icon_url = str(author.avatar_url))
          embed.set_footer(text = f'gambled by {author.name}#{author.discriminator}')
          await ctx.reply(embed=embed)
      else:
          embed = discord.Embed(
          color = discord.Color.red()
          )
          embed.add_field(name= "you have lost!", value = f"it's {bot_bet_value}")
          embed.set_author(name = author,icon_url = str(author.avatar_url))
          embed.set_footer(text = f'gambled by {author.name}#{author.discriminator}')
          await ctx.reply(embed=embed)

        
  


async def setup(bot):
  await bot.add_cog(Gamble(bot))