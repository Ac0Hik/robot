import os
import json
import discord
from discord.ext import commands, tasks
from random import choice
import asyncio

from datetime import datetime
import random
import itertools
import requests
import sys

from dotenv import load_dotenv

load_dotenv()




#necessary for serverinfo and the ones similare to it
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True

#activity = discord.Activity(type=discord.ActivityType.watching)

bot = commands.Bot(command_prefix='-', intents = intents)



DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')
  print(f'{bot.user} is connected to the following guild:')
  for guild in bot.guilds:
    if guild.name == '':
      break
    print(f'- {guild.name} (id: {guild.id})')
  #-------------loops tasks--------------
  #change_color.start()

# IN_A_VC = int(os.environ['in_a_vc'])

# #IDs
welcome_bye=os.getenv('welcome_bye')

# #server id 


# #roles' ids
moderator_DEVS = int(os.getenv('moderator_DEVS'))


# #-------------


# # The on_ready() event happens on start of the program, on re-connects,
# # and is not necessarily the first event - i.e. the bot might start and
# # process an on_message() event before it processes the below code


# #ignore this one i will remove it later achik
# '''@bot.event
# async def on_raw_message_delete(playload):
#    message = playload.cached_message
#    content = message.content
#    author = message.author
#    at =  message.created_at
#    channel =  message.channel
#    print(f'message deleted by {author} at {at}\ncontent:{content}\nin: {channel}')'''





'''reference for future tasks'''
# #changes victoria's role color every half an hour
# @tasks.loop(hours=0.5)
# async def change_color():
#   gorbage_collective = bot.get_guild(THE_GORBAGE_COLLECTIVE)
#   role  = gorbage_collective.get_role(920797019600216114)#victoria role
#   r, g, b = next(colors)
#   await role.edit(colour = discord.Colour.from_rgb(r,g,b))



# #commands to help us with cogs
@bot.command(hidden = True)
@commands.has_role(moderator_DEVS)
async def load(ctx, extension ):
      await bot.load_extension(f'cogs.{extension}')
      await ctx.send(f"**{extension}**'s been' loaded successfully ")

@bot.command(hidden=True)
@commands.has_role(moderator_DEVS)
async def unload(ctx, extension):
      await bot.unload_extension(f'cogs.{extension}')
      await ctx.send(f"**{extension}**'s been unloaded successfully ")

@bot.command(hidden = True)
@commands.has_role(moderator_DEVS)
async def reload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"**{extension}**'s been reloaded successfully ")
#we want to send the same error for the 3 of them but idk if it's possible to do that in one error function , any ideas ?
#-------------- these commands should only used by racc dev team  
async def err_msg(ctx):
  await ctx.send('**you are not allowed to do that**')

@load.error
async def load_err(ctx, error):
  if isinstance(error, commands.MissingRole):
    await err_msg(ctx)

@unload.error
async def unload_err(ctx,error):
  if isinstance(error, commands.MissingRole):
    await err_msg(ctx)

@reload.error
async def reload_err(ctx, error):
  if isinstance(error, commands.MissingRole):
    await err_msg(ctx)
#nonrac bot role holders error
    
async def load_exts():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')



@bot.event
async def on_message(message):
  await bot.process_commands(message) #it allows to excute the commands if there's any 
# the bot should not read it's own messages and ignore messages without our prefix
  if message.author == bot.user or message.content.lower().find("?") != -1:
    return
  # #time detector
  # if message.author in timezone_users:
  #   if message.content.find()
  #olivia detector
  if message.content.find("💅") != -1 or message.content.lower().find("baddie") != -1 or message.content.lower().find("purr") != -1 or message.content.lower().find("purrr") != -1 or message.content.lower().find("purrrr") != -1:
    await message.channel.send(content="Olivia momento :pensive: :sparkles:", reference=message)
  #beep boop detector
  elif message.author == bot.get_user(173892890945257472) and message.content.upper() == 'BEEP BOOP':
    await message.channel.send('boop beep')
  elif message.content.find(":peepoJuice:") != -1:
    await message.channel.send(content = "Victoria momento :peepoJuice:", reference = message)
  #"robby " messages inside of else
  else:
      if message.content.lower().find('robby ') != 0:
        return
      else:
        try:
          print(message.content)
          await message.channel.send(
            content='I saw this message :bread::thumbsup:'
            , reference=message  #this makes send() create a reply - it's optional
          )
        except:
          await message.channel.send(
            content="https://i.imgur.com/oW93aWx.gif"
            ,response=message
        )

        
# # on_reaction_add(reaction, user) only gets updates on cached messages
# # on_raw_reaction_add(payload) maybe gets updates on all messages?
# # but we will want the details of the original message, user reacting, and emoji
# #   e.g. if it is a poll by the bot, or for users to self-add roles
# # Note: the event payload may include that the reaction was removed not added
# '''
# @bot.event
# async def on_raw_reaction_add(payload):
#   print('reaction detected')
#   print(payload.message_id)
# '''


@bot.command()
async def ping(ctx):
  await ctx.send(f':ping_pong:**Pong! {round(bot.latency*1000)}ms.**')

@bot.command(name = "justask", help = "shows a link to \"don't ask to ask article\"")
async def justask(ctx):
  msg = "**[Don't ask to ask! JUST ASK:)](https://dontasktoask.com/)**"
  icon = ctx.author.avatar_url
  embed = discord.Embed(
    #  title = "",
    description = msg,
    color = ctx.author.color,
    timestamp = ctx.message.created_at
  )   
  embed.set_footer(text = f'requested by {ctx.author}', icon_url = icon)
  await ctx.send(embed = embed)



@bot.command()
async def dividebyzero(ctx):
  await ctx.send(content="https://i.imgur.com/oW93aWx.gif",response=ctx.message) #what is this command lmao


#pomo timer prototype 
@bot.command(
  name='pom',
  aliases = ["pomodoro", "timer"],
  help = "A Pomodoro timer. Give 3 numbers:"
    +"\n(a) work duration in minutes"
    +"\n(b) rest duration in minutes"
    +"\n(c) number of work periods"
)
async def pom(ctx, work_duration: int, rest_duration: int, work_count: int):
  try:
    while work_count > 0:
      work_count -= 1
      await ctx.send(f'{ctx.message.author.mention},{work_duration} min session starts now \nFOCUS!')
      await asyncio.sleep(work_duration*60)
      if work_count == 0: ## last work timer
        await ctx.send(f'{ctx.message.author.mention} Last sessions is over! You\'re done! :ok_hand:')
      else: ## a rest follows
        response = f'{ctx.message.author.mention}session is over! {work_count} pomodoro'
        if work_count > 1:
          response += 's'#pluralised
        response += f' to go.\nRest for {rest_duration} min starts now.'
        await ctx.send(response)
        await asyncio.sleep(rest_duration*60)
  except:
    print("something went wrong")


@pom.error
async def pom_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You're missing a required argument idiot.¯\_(ツ)_/¯")

@bot.command(name = 'eightball', aliases = ['8ball', '8b'], help = 'The Magic 8-ball will answer your questions.')
async def eightball(ctx):
  responses = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',   #<---- fuck this shit -G
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
  ]
  #replaced sample with choice, per G - Ruby
  await ctx.send(choice(responses), reference=ctx.message)


@bot.command(name='GetEmoji', aliases=['getemoji', 'Getemoji'], help = "Gets an emoji's full picture")
async def GetEmoji(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)


@bot.command(name='delete', aliases=['purge'], help='Delete chat messages.[]')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, i: int):
  j = i + 1
  await ctx.channel.purge(limit = j)
  await ctx.send("What were y'all sayin?")

@bot.command(aliases=['purgeall'], help='Delete all chat messages.', hidden = True)
@commands.has_role(moderator_DEVS)
async def purge_all(ctx):
  await ctx.channel.purge()
  print(f'{ctx.author.name} has just purged {ctx.channel.name}')

# @bot.event
# async def on_raw_reaction_add(reaction):
#     if (reaction.emoji.id == 920119505991135312):
#         dumpster_channel = bot.get_channel(FUNNY_M0MENTS)#funny moments
#         messageId = reaction.message_id
#         channel = bot.get_channel(reaction.channel_id)#the channel where the message was sent 
#         message = await channel.fetch_message(messageId)
#         reactions = message.reactions
#         for reaction in reactions:
#             if reaction.emoji.id == 920119505991135312:
#                 theReaction = reaction
#         if(theReaction.count == 3):
#           author = message.author
#           content = message.content
#           msg = f"**__[Original message]({message.jump_url})__**"
#           embed =  discord.Embed(
#             title = '**__The Dumpster__**',
#             description = msg,
#             color = author.color
#           )
#           embed.set_author(name = author.name, icon_url = author.avatar_url)
#           embed.add_field(name = 'Content:', value = content)
#           embed.set_footer(text = f'{datetime.now().strftime("%m/%d/%Y")}')
#           await dumpster_channel.send(content = f"from:{channel.mention}", embed = embed)   
 



@bot.command(name = "wouldyourather", aliases = ["Wouldyourather", "wyr"], help = "sends a would you rather prompt")
async def WouldYouRather(ctx):
  api_url = 'https://would-you-rather-api.abaanshanid.repl.co/'
  response = requests.get(api_url)
  data = response.json()['data'][16:]
  options = data.split('or')
  embed = discord.Embed(
          colour=discord.Colour.red(),
          timestamp = ctx.message.created_at
  )
  embed.set_author(name=f'Would you rather...')
  embed.add_field(name=':one:', value= options[0],inline=False)
  embed.add_field(name=':two:', value = options[1], inline=False)
  embed.set_footer(text="Raccobot Dev team \n")
  message = await ctx.send(embed=embed)
  await message.add_reaction('1️⃣')
  await message.add_reaction('2️⃣')


# 4
# # Topic command by me -G
# @bot.command(name = "Topic", aliases = ["topic"], help = "You really need help with this one? sends a conversation topic.")
# async def topcs(ctx):
#   i = random.randint(0, len(topic))
#   await ctx.send("> " + topic[i])

@bot.command(name='dice', help=': roll one or more dice. usage: "-dice [number of dice], [number of faces].', aliases = ['diceroll', "roll"])
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))



@bot.command(name = "meme", aliases=['memes'], help = ':I send a memey :)')
async def meme(ctx):
  content = requests.get("https://meme-api.herokuapp.com/gimme").text
  data = json.loads(content,)
  meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
  await ctx.reply(embed=meme)

  
@bot.command()
async def dadjoke(ctx):
    api_url = 'https://icanhazdadjoke.com/'
    response = requests.get(api_url , headers = { "Accept": "application/json" })
    print(response)
    joke = response.json()['joke']
    await ctx.reply(joke)
  #experimenting ------ 


@bot.command(name = "choose" , aliases = ["Choose", "CHOOSE"])
async def choose(ctx, *, choices: str):
    """helps u choose between multiple arguments"""
    choices = choices.split(',')
    await ctx.reply(random.choice(choices))

@bot.command(help='''reacts to a specific message
             \nparam:
             \nmessge to add the reaction to
             \nemoji the emoji u wanan react with[default:eybrow1 emoji]\n(works only with guild emojis :((''')
@commands.has_permissions(manage_messages=True)
async def react(ctx, react_to: commands.MessageConverter, emoji : discord.PartialEmoji = None):
  if emoji is None:
    emoji = bot.get_emoji(948009755413213214)#default emoji id
  await ctx.message.delete()
  await react_to.add_reaction(emoji)


@react.error
async def react_err(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply('you are missing a required argument')
  

@bot.command(name = 'join', help = ': I enter in your VC')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command(name = 'leave', aliases = ['disconnect'], help = ":I exit from your VC")
async def leave(ctx):
    await ctx.voice_client.disconnect()

# #gives vc role when u join a vc and removes it when u leave
# @bot.event
# async def on_voice_state_update(member, before, after):
#     role = discord.utils.get(member.guild.roles, id = IN_A_VC )
#     if before.channel is None and after.channel is not None: 
#         await member.add_roles(role) 
#     elif before.channel is not None and after.channel is None:
#         await member.remove_roles(role) 


@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(welcome_bye)
  await channel.send(f'sorry to see you leave {member.mention} see you again soon :raised_hands:')

@bot.hybrid_command()
async def hola(ctx):
  await ctx.reply('hola como estas?')


async def main():
  await load_exts()
  await bot.start(DISCORD_TOKEN)

asyncio.run(main())
