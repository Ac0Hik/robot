import discord
from discord.ext import commands
from datetime import datetime
from asyncio import sleep


class Information(commands.Cog):
  
  def __innit__(self, bot):
    self.bot =  bot


  @commands.Cog.listener()
  async def on_ready(self):
    print('Information is ready')
    print('-----------------')


  
  @commands.command(name = 'serverinfo', help = "shows server's info") #removed aliases because not needed, -G
  async def serverinfo(self,ctx):
    guild =  ctx.guild
    msg = "<#919780692567666708>" 
    guildName = str(guild.name)
    guildDescription = str(guild.description)
    guildOwner = '<@' + str(guild.owner.id) + '>'
    guildId = str(guild.id)
    region = str(guild.region)
    memberCount = str(guild.member_count)
    vcCount = str(len(guild.voice_channels))
    txtCount = str(len(guild.text_channels))
    rolesCount = str(len(guild.roles))
    icon = str(guild.icon_url)  
    embed = discord.Embed(
      title = guildName + " Server Information",
      description = guildDescription,
      color = ctx.author.color,
      timestamp = ctx.message.created_at
    ) 
    embed.add_field(name="Owner <:BritishTeaPeepo:919798937907494912>", value = guildOwner, inline = True )
    embed.add_field(name="Server ID", value = guildId, inline = True )
    embed.add_field(name="Region", value = region, inline = True)
    embed.add_field(name="Members Count", value = memberCount, inline = True)
    embed.add_field(name="Voice channels Count:", value = vcCount, inline = True )
    embed.add_field(name="Text channels Count:", value = txtCount, inline = True )
    embed.add_field(name="Roles Count", value = rolesCount, inline = True )
    embed.add_field(name = "for more information check", value = msg, inline = False)
    embed.set_footer(text = f'{guildName}. requested by {ctx.author}', icon_url = icon)

    await ctx.send(embed = embed)

  @commands.command()
  async def userinfo(self,ctx, *, user: commands.MemberConverter = None, help = "shows user's info"):  
    if user is None:
      user = ctx.author
    userIcon = str(user.avatar_url)
    userId = str(user.id)
    userGuildName = str(user.display_name)
    createdAt = user.created_at.strftime("%a %d %b %Y %I:%M %p")
    joinedAt = user.joined_at.strftime("%a %d %b %Y %I:%M %p")
    bot = user.bot
    joinAgeDeltatime = datetime.now() - user.joined_at #join age
    serverJoinAgeWeeks = divmod(joinAgeDeltatime.total_seconds(), 60*60*24*7)
    serverJoinAge = str(int(serverJoinAgeWeeks[0])) + ' week and ' + str(int(int(serverJoinAgeWeeks[1])/(60*60*24))) + ' days.' 

    createdAgeDeltatime = datetime.now() - user.created_at #account age
    createdAgeWeeks = divmod(createdAgeDeltatime.total_seconds(), 60*60*24*7)
    createdAge = str(int(createdAgeWeeks[0])) + ' week and ' + str(int(int(createdAgeWeeks[1])/(60*60*24))) + ' days.' 

    embed = discord.Embed(
      title = f'User info: {user}',
      description = '<@' + userId + '>',
      color = user.color,
      timestamp = ctx.message.created_at
    )
    embed.set_thumbnail(url = userIcon)
    embed.add_field(name = "ID:", value = userId, inline = False)
    embed.add_field(name = "Server name:", value = userGuildName, inline = False )
    embed.add_field(name = "Created at:", value = createdAt, inline = True)
    embed.add_field(name = "Account age:", value = createdAge, inline = False)
    embed.add_field(name = "Joined at:", value = joinedAt, inline = True)
    embed.add_field(name = "Server join age:", value = serverJoinAge, inline = False)
    embed.add_field(name = "Bot?", value = bot, inline = False )
    embed.set_footer(text = f'requested by {ctx.author}', icon_url = str(ctx.author.avatar_url))
    
    await ctx.send(embed = embed)

  @commands.command(name = 'role', help = 'shows role info')
  async def roleinfo(self,ctx, role: commands.RoleConverter = None):
    if role is None:
        role = ctx.author.top_role
    embed = discord.Embed(
      title = f'role info',
      color = ctx.author.color,
      timestamp = ctx.message.created_at
    )
    roleName = role.name
    roleID = role.id
    roleMention = role.mention
    createdAt = role.created_at.strftime("%m/%d/%y")
    isMentionable = role.mentionable
    color = role.color
    position = role.position
    hoisted =  role.hoist
    roleCount = role.member_count
    rolePermessions = ""
    for permission, tof in role.permissions:
      if tof is True:
        rolePermessions += f'{permission}, '
    embed.add_field(name = "name:", value = roleName, inline = True)
    embed.add_field(name = "ID:", value = roleID, inline = True)
    embed.add_field(name = "created at:", value = createdAt, inline = True)
    embed.add_field(name = "color:", value = color, inline = True)
    embed.add_field(name = "mentionable?", value = isMentionable, inline = True)
    embed.add_field(name = "position:", value = position, inline = True)
    embed.add_field(name = 'Role mention:', value = roleMention, inline =  True)
    embed.add_field(name = "hoisted?", value = hoisted, inline = True)
    embed.add_field(name='role holders count : ', value=roleCount, inline=True)
    embed.add_field(name = 'permessions:', value = rolePermessions, inline = False)
    embed.set_footer(text = f' requested by {ctx.author}', icon_url = str(ctx.author.avatar_url))

    await ctx.send(embed = embed)

  @commands.command(name = "inrole", help = "shows a list of all role holders.\nit takes the author's top role if no parameter is passed\n:param: role")
  async def inrole(self, ctx, role : commands.RoleConverter = None):
    if role is None:
      role = ctx.author.top_role
    members = role.members 
    members_list = ""
    for index,member in enumerate(members):
      members_list += f'``{index + 1}``--{member.mention}\n'

    embed = discord.Embed(
      color = role.color,
      timestamp = ctx.message.created_at
    )
    code_formated_list = f'{members_list}' 
    embed.add_field(name = f'**__{role.name}__ holders:**', value = code_formated_list)
    await ctx.send(embed=embed) 


  @commands.command(aliases= ['av'], help = "shows avatar\n:param: user")
  async def avatar(self,ctx, user: commands.MemberConverter = None):
      if user is None:
        user = ctx.author
      iconURL = str(user.avatar_url)
      embed = discord.Embed(
          title = f'{user}\navatar:',
          color = user.color,
          timestamp = ctx.message.created_at 
      )
      embed.set_image(url = iconURL)
      embed.set_footer(text = f'requested by{ctx.author}.',icon_url=str(ctx.author.avatar_url))
    
      await ctx.send(embed = embed)

  


async def setup(bot):
  await bot.add_cog(Information(bot))