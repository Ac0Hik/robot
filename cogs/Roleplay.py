import os
import discord
from discord.ext import commands

import requests
from random import randint

giphy_api_key = str(os.environ['GIPHY_API_KEY'])

class Roleplay(commands.Cog):


  def __innit__(self, bot):
     self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('roleplay is ready')
    print('-------------------')
  

  def get_url(self, key,theme, limit = 25, rating = 'g'):
    api_url = f'https://api.giphy.com/v1/gifs/search?api_key={key}&q={theme}&limit={limit}&rating={rating}'
    response = requests.get(api_url)
    data = response.json()
    i =  randint(0,limit)
    image = data["data"][i]["images"]
    url = image['original']['url']
    return url

  @commands.command(aliases =['SLAP', 'Slap'], help='param :member:[default:you]')
  async def slap(self, ctx, target : commands.MemberConverter = None):
    prompt = f"{ctx.author.mention} has just slapped"
    if target is None:#the user forgot to mention a member to slap-- overide the prompt variable to its new value
        prompt = f"{ctx.author.mention} didn't mention anyone so they ended u slapping themselves for being dumb"
        target = ctx.author
    else:
        prompt += f' {target.mention}'

    url = self.get_url(giphy_api_key,'slap')
    embed = discord.Embed(
        color = ctx.author.color,
        timestamp = ctx.message.created_at
    ) 
    embed.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url))
    embed.add_field(name = '**__the holy slap__:**', value=prompt)
    embed.set_image(url = url)
    await ctx.reply(embed = embed)


  @commands.command(aliases =['HUG', 'Hug'], help='param :member:')
  async def hug(self, ctx, target : commands.MemberConverter):
    prompt = f"{ctx.author.mention} has just hugged {target.mention}"
    url = self.get_url(giphy_api_key,'hug')
    embed = discord.Embed(
        color = ctx.author.color,
        timestamp = ctx.message.created_at
    ) 
    embed.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url))
    embed.add_field(name = '**__hug__:**', value = prompt)
    embed.set_image(url = url)
    await ctx.reply(embed = embed)
    
  @hug.error
  async def hug_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.message.reply("**you forgot to mention a member to hug**")


  @commands.command(aliases =['KISS', 'Kiss'], help='param :member:')
  async def kiss(self, ctx, target : commands.MemberConverter):
    prompt = f"{ctx.author.mention} has just kissed {target.mention}"
    url = self.get_url(giphy_api_key,'kiss')
    embed = discord.Embed(
        color = ctx.author.color,
        timestamp = ctx.message.created_at
    ) 
    embed.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url))
    embed.add_field(name = '**__kiss__:**', value = prompt)
    embed.set_image(url = url)
    await ctx.reply(embed = embed)
    
  @kiss.error
  async def kiss_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.message.reply("**you forgot to mention a member to kiss**")


  @commands.command(aliases =['PAT', 'Pat'], help='param :member:')
  async def pat(self, ctx, target : commands.MemberConverter):
    prompt = f"{ctx.author.mention} has just patted {target.mention}"
    url = self.get_url(giphy_api_key,'pat')
    embed = discord.Embed(
        color = ctx.author.color,
        timestamp = ctx.message.created_at
    ) 
    embed.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url))
    embed.add_field(name = '**__pat__:**', value = prompt)
    embed.set_image(url = url)
    await ctx.reply(embed = embed)
    
  @pat.error
  async def pat_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.message.reply("**you forgot to mention a member to pat**")

  @commands.command(aliases =['YEET', 'Yeet'], help='param :member:')
  async def yeet(self, ctx, target : commands.MemberConverter):
    prompt = f"{ctx.author.mention} has just yeeted {target.mention}"
    url = self.get_url(giphy_api_key,'yeet')
    embed = discord.Embed(
        color = ctx.author.color,
        timestamp = ctx.message.created_at
    ) 
    embed.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url))
    embed.add_field(name = '**__yeet__:**', value = prompt)
    embed.set_image(url = url)
    await ctx.reply(embed = embed)
    
  @yeet.error
  async def yeet_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.message.reply("**you forgot to mention a member to yeet**")


  

async def setup(bot):
  await bot.add_cog(Roleplay(bot))