#This config has a cool spam command, delete this, if you don't wanna to get your server Raided!


import discord
from discord.ext import commands
import random
import asyncio

description = '''Hello! My prefix is m?'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='m?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Started!')
    bot.loop.create_task(status_task())
    print("My name is")
    print(bot.user.name)
    

@bot.listen()
async def on_message(message):
    print(message.author, message.content)



async def status_task():
    while not bot.is_closed():
        await bot.change_presence(activity=discord.Game('with m?help'), status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game('with wumpus!'), status=discord.Status.online)
        await asyncio.sleep(3)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run('YOUR TOKEN')
