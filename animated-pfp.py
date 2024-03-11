import discord
from discord.ext import commands
import requests
from io import BytesIO

# Bot token
token = "TOKEN" # Your bot token go here

# Animated pfp link
animated_pfp_url = "https://media2.giphy.com/media/67ThRZlYBvibtdF9JH/giphy.gif?cid=6c09b952t2f0xokefjxp70u4crim8f0c0dakcn735fnukg4v&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g" # Your new pfp link go here

# Create bot instance with intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Change bot's profile picture
    await change_pfp(bot.user, animated_pfp_url)
    print('Profile picture changed successfully!')

async def change_pfp(user, pfp_url):
    # Download image
    response = requests.get(pfp_url)
    pfp_data = BytesIO(response.content)

    # Change profile picture
    await user.edit(avatar=pfp_data.read())

# Run the bot
bot.run(token)
