import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Test test test')

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)


@bot.event
async def on_message(message):
    y = list(message.content)
    y.insert(1, 'e')
    z = ''.join(y)
    channel = message.channel
    await channel.send(z)


SECREEEEEET = 'YOUR_SECRETS_HERE'

bot.run(SECREEEEEET)
