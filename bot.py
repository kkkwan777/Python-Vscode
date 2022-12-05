import discord
import os
import sys
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GULID = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    guild = discord.utils.get(bot.guilds, name = GULID)
    print(GULID)
    print(discord.version_info)
    print(discord.__version__,  type(discord.__version__))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('bad bot'):
        await message.channel.send('say that again?')
    elif message.content == 'exception':
        raise discord.DiscordException

    await bot.process_commands(message)
    
@bot.command(name='random', help='random choice starting from 1.')
async def roll(ctx, times: int, number_of_choices: int):
    dice = [
        str(random.choice(range(1, number_of_choices + 1)))
        for _ in range(times)
    ]
    await ctx.send(', '.join(dice))

@bot.command(help = 'A plus B')
async def add(ctx, arg1: int, arg2: int):
    await ctx.send(arg1 + arg2)

@bot.command(help = 'A minus B')
async def minus(ctx, arg1: int, arg2: int):
    await ctx.send(arg1 - arg2)

@bot.command(help = 'A times B')
async def times(ctx, arg1: int, arg2: int):
    await ctx.send(arg1 * arg2)

@bot.command(help = 'A over B')
async def over(ctx, arg1: int, arg2: int):
    await ctx.send(arg1 / arg2)

@bot.command()
async def check_guild(ctx):
    await ctx.send(ctx.guild)

@bot.command()
async def check_author(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def check_message(ctx):
    await ctx.send(ctx.message)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def check_bot(ctx):
    await ctx.send(ctx.bot)

bot.run(TOKEN)
