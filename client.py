import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GULID = os.getenv("DISCORD_GUILD")
print(GULID)

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name = GULID)
    print(
        f'{client.user} is connected to the guild:\n'
        f'Guild name: {guild.name} (id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('bad bot'):
        await message.channel.send('say that again?')
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Server'
    )

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled messages: {args[0]}\n')
        else:
            raise

client.run(DISCORD_TOKEN)