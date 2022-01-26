import random, discord
from datetime import date
from time import strftime
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix="+")
status = cycle(["Never","Gonna","Give","You","Up","Never","Gonna","Let","You","Down","Never","Gonna","Turn","Around",
                "And","Desert","You","🔥","🔥"])

@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    general_channel = client.get_channel(848137973958443028)
    await general_channel.send(f"{client.user} is here!")

@client.command(name="ping")
async def ping(ctx, message):
    number5 = await client.wait_for("Number of pings? -->")
    await ctx.send(number5)

@client.command(name="poll")
async def poll(ctx, *,message):
    myembed = discord.Embed(title="Idea for: ", description=f"{message}", color=0x86ff45)
    myembed.set_author(name=client.user)
    msg = await ctx.channel.send(embed=myembed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    await msg.add_reaction("🎯")

@client.command(name="ban")
@commands.has_any_role("Bot", "Owner")
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *,reason=None):
    await member.ban(reason="You are way too dumb")

@client.command(name="kick")
@commands.has_any_role("Bot", "Owner")
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *,reason=None):
    await member.kick(reason="You are dumb")

@client.command(name="rayquaza")
async def rayquaza(context):
    myembed = discord.Embed(title="Rayquaza",
                            description="Rayquaza is the best pokemon, as you can see",
                            color=0x45ff95)
    myembed.add_field(name="Official Pokedex entry(newest)", value="One of it^s Pokedex entries reads,^Rayquaza is said to have lived for hundreds of millions of years.Legends remain of how it put to rest the clash between Kyogre and Groudon.^", inline=False)
    myembed.add_field(name="Shiny Form", value="It`s shiny is, in my opinion, the best. It just looks so cool!", inline=False)
    myembed.add_field(name="Stats", value="Attack and Special Attack are the highest, HP is second highest, and Defense, Special Defense and Speed are even", inline=False)
    myembed.add_field(name="Types", value="It is a Dragon + Flying Type. It is 2x weak to Fairy, Dragon and Rock, but is 4x weak to Ice Types", inline=False)
    myembed.add_field(name="Overall", value="Overall, it is just a cool legendary pokemon, and super strong. It^s even stronger in it^s mega form!", inline=True)
    myembed.add_field(name="More information about Rayquaza", value="[Click here for more information](https://www.serebii.net/pokedex-xy/384.shtml)", inline=False)
    myembed.add_field(name="Clip", value="https://www.youtube.com/watch?v=66KfqgZAhM8", inline=False)
    myembed.set_author(name=client.user)
    myembed.set_thumbnail(url="https://i.pinimg.com/originals/da/b0/07/dab0070e6ea692aa0087a471afe2a8f4.jpg")
    msg2 = await context.message.channel.send(embed=myembed)
    await msg2.add_reaction("🌪️")
    await msg2.add_reaction("🌩️")
    await msg2.add_reaction("🐉")
    await msg2.add_reaction("🐍")

@client.command(name="attack")
async def attack(context):
    await context.message.channel.send("ATTACK!")
    await context.message.channel.send("🏴‍☠️")
    await context.message.channel.send("🔥🔥")
    await context.message.channel.send("🔥🔥")
    await context.message.channel.send("🔥🔥")
    await context.message.channel.send("🔥🔥")

@client.command(name="defend")
async def defend(context):
    await context.message.channel.send("HELP PUT OUT THE FIRE!")
    await context.message.channel.send("🧯🧯🧯")
    await context.message.channel.send("🌊🌊🌊")

@client.command(name="dice")
async def dice(context):
    random1 = random.randint(1,6)
    myembed = discord.Embed(title="Random Dice Roll", description="You will be rolling a dice and getting a number between 1 to 6", color=0x45ff78)
    myembed.add_field(name="Your roll dice is:", value=random1, inline=True)
    myembed.set_author(name=client.user)
    myembed.set_thumbnail(url="https://pngimg.com/uploads/dice/dice_PNG49.png")
    myembed.set_footer(text="This is a generated procedure.")
    await context.message.channel.send(embed=myembed)

@client.command(name="clear")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(name="time")
async def time(context):
    string = strftime("%H:%M:%S %p")
    today = date.today()
    myembed = discord.Embed(title="Time", description="Time Now", color=0x45ff57)
    myembed.add_field(name="Time is:",value=string, inline=False)
    myembed.add_field(name="The date is:", value=today, inline=False)
    myembed.set_author(name=client.user)
    myembed.set_footer(text="The time shown is the Time this command was used")
    msg3 = await context.message.channel.send(embed=myembed)
    await msg3.add_reaction("⏰")
    await msg3.add_reaction("🕐")

@client.command(name="helpme")
async def helpme(context):
    response = ["Please contact the bor creator","How would I know","You need help","Idk"][random.randrange(4)]
    await context.message.channel.send(response)

@client.command(name="number")
async def number(context):
    number1 = random.randint(1, 10)
    number2 = random.randint(1000, 2000)
    total = number2 - number1

    myembed = discord.Embed(title="Random Number Generator", description="This randomly generates a number", colour=0x45ff95)
    myembed.set_thumbnail(url="https://cdn.vox-cdn.com/thumbor/rIzUCFPxAXJVl01BvxDW2UIp_TQ=/0x0:1024x576/920x613/filters:focal(431x207:593x369):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66496005/8476624791_ac7a5a8357_b.0.0.1457958152.0.jpg")
    myembed.add_field(name="First Number", value="This generates a number between 1 to 10", inline=False)
    myembed.add_field(name="Your First Number is", value=number1, inline=False)
    myembed.add_field(name="Second Number", value="This generates a number between 1000 to 2000", inline=False)
    myembed.add_field(name="Your Second Number is", value=number2, inline=False)
    myembed.add_field(name="Final Total", value="The final number is the Second Number minus the First Number.", inline=False)
    myembed.add_field(name="Your Final Number is", value=total, inline=False)
    myembed.set_footer(text="This is a generated procedure.")
    myembed.set_author(name=client.user)
    msg4 = await context.message.channel.send(embed=myembed)
    await msg4.add_reaction("🔢")
    await msg4.add_reaction("🎫")

@client.command(name="game")
async def game(context):
    response1 = ["Minecraft","Fortnite","Brawl Stars","Rocket League","Pokemon Sword/Shield","Breath of the Wild"][random.randrange(6)]

    myembed = discord.Embed(title="Video Games", description="I like games and not studying", colour=0x67ff89)
    myembed.add_field(name="Your game is:", value=response1, inline=False)
    myembed.add_field(name="Do you like", value=f"{response1}?", inline=False)
    myembed.set_thumbnail(url="https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_4/H2x1_NSwitch_Minecraft_image1600w.jpg")
    myembed.set_author(name=response1)
    myembed.set_footer(text=f"I like {response1}.")
    msg5 = await context.message.channel.send(embed=myembed)
    await msg5.add_reaction("🎮")

@client.event
async def on_message(message, context):
    if context.message == "Why are you so shady?":
        await context.message.channel.send(f"Hi {message.author.mention}")
        await context.message.channel.send(f"It`s because of my backstory. I was a normal kid, but was sold to some ducks. {message.author.mention}")
        await context.message.channel.send("They sold drugs, but was caught by the police.")
        await context.message.channel.send("I became a drug dealer, but left to be a school major.")
        await context.message.channel.send("I then started a business that sold paper, and now here i am.")
        await context.message.channel.send("I left the job as i was a billionaire but lost the money and i did drugs again.")
    elif context.message == "What drugs do you have?":
        await context.message.channel.send("I have some paper and some suspicious white powder. Oh shoot, forget i said that.")
    elif context.messsage == "I want some drugs please":
        await context.message.channel.send("Cocaine is £4. Cannabis is £6. That`s all I have.DON`T TELL ANYONE YOU SAW ME HERE.")
    elif context.message == "Send a link to drugs":
        await context.message.channel.send("https://www.youtube.com/channel/UCKm9X6EGXdM2DZQw6KErKgg")
    elif context.message == "Fuck":
        await context.message.channel.send("LANGUAGE!")
    elif context.message == "Shit":
        await context.message.channel.send("LANGUAGE!")
    elif context.message == "Bitch":
        await context.message.channel.send("LANGUAGE!")
    elif context.message.startswith("Hi"):
        await context.message.channel.send(f"Welcome{message.author}")

    await client.process_commands(message)

client.run("")
