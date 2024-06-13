import discord
import os
from discord.ext import commands
import random
from asyncio import sleep

#------------------------env variables
welcome_bye = int(os.environ['welcome_bye'])

class Embeds(commands.Cog):


  def __innit__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('embeds is ready')
    print(f'bot variable:{self.bot}')
    print('------------------')


  @commands.Cog.listener()
  async def on_member_join(self, member):
      gorbage_collective = member.guild
      welcome_channel = self.bot.get_channel(welcome_bye)
      embed = discord.Embed(
          color = discord.Color.random(),
          timestamp = member.joined_at
      )
      welcome = f"hey{member.mention} welcome to **{gorbage_collective}**"
      embed.set_author(name = f'{member.name}#{member.discriminator}')
      embed.set_image(url = str(member.avatar_url))
      welcome_message = await welcome_channel.send(welcome, embed = embed)
      wlcm_emoji = self.bot.get_emoji(920346312799580210)
      await welcome_message.add_reaction(wlcm_emoji)

  @commands.command()
  async def gayrate(self, ctx, *, user: commands.MemberConverter = None):
    grate = random.randint(0,100)
    msg = ""
    if user is None:
      msg += '**you are '
      user = ctx.author
    else:
      msg += f'**{user.name}#{user.discriminator} is '
    msg += f' {grate}% gay :rainbow_flag: **'
    embed = discord.Embed(
      title = "Robby gayrate machine:",
      description = msg,
      color = user.color,
      timestamp = ctx.message.created_at
    )  
    await ctx.send(embed = embed)

  @commands.command()
  async def simprate(self, ctx, *, user: commands.MemberConverter = None):
      srate = random.randint(0,100)
      msg = ""
      if user is None:
        msg += '**you are '
        user = ctx.author
      else:
        msg += f'**{user.name}#{user.discriminator} is '
      msg += f' {srate}% simp  <:heheclassyLeo:920660557487542312>**'
      embed = discord.Embed(
          title = "Robby simprate machine:",
          description = msg,
          color = user.color,
          timestamp = ctx.message.created_at
      )  
      await ctx.send(embed = embed)

  @commands.command(aliases = ['es'], help ="use 'es' to embed say something ")
  async def emsay(self, ctx, *, arg):
      await ctx.message.delete()
      author = ctx.author
      ctn = "```" + arg + "```"
      embed = discord.Embed(
          color = author.color,
          timestamp = ctx.message.created_at
      )
      embed.add_field(name = "message:", value = ctn)
      embed.set_footer(text = f'requested by {author}.', icon_url = str(author.avatar_url))
      await ctx.send(embed =  embed)

  @commands.command(help = '''param :the question: (between ""!!)\n:options:[max4] comma seperated''')
  async def poll(self, ctx, about :str , *, options: str):
    options = options.split(',')

    if( len(options) > 4 ):
      return await ctx.reply('too many arguments**[max options 4]**')

    await ctx.message.delete()
    async with ctx.typing():

      nums = ['1️⃣','2️⃣','3️⃣','4️⃣']
      embed = discord.Embed(
        title = '**__poll__**:',
        description = about,
        color = discord.Colour.random()
      )
      numerated_options = ""
      for i, option in enumerate(options):
          numerated_options += f'``{i + 1}``-{option}\n'

      embed.add_field(name = 'make your pick!', value = numerated_options, inline = False)
      await sleep(4)
      message = await ctx.send(embed = embed)#sending the poll embed
      #adding reaction to the embed
      for i in range(len(options)):
          await message.add_reaction(nums[i])


  @poll.error
  async def poll_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.reply("**missing an arguement(s)**")



async def setup(bot):
  await bot.add_cog(Embeds(bot))
  