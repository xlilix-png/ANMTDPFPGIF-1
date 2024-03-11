import discord
import asyncio

# Intents to enable certain events
intents = discord.Intents.all()

# Create a Discord client instance with intents
client = discord.Client(intents=intents)

# Event to handle bot's initialization
@client.event
async def on_ready():
    print('Connected as: {0.user}'.format(client))

    # Upload animated avatar
    try:
        with open('https://media3.giphy.com/media/26CaNATkmzrmo1VK0/giphy.gif?cid=6c09b952qord1rwe5on6ph1yn94035p0imr24kv675fs5et8&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g', 'rb') as avatar:
            await client.user.edit(avatar=avatar.read())
        print('Uploaded successfully!')
    except Exception as e:
        print('Failed:', e)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Recap'):
        await message.channel.send('Hey! Invite Recap To your server. https://discord.gg/kyNy8FZQ8J')


# Load the bot token from a secure location
try:
    with open("bot_token.txt", "r") as token_file:
        DISCORD_BOT_TOKEN = token_file.read().strip()
except FileNotFoundError:
    print("Bot token file not found.")
    DISCORD_BOT_TOKEN = input("Enter your bot token: ").strip()

# Run the bot
client.run(DISCORD_BOT_TOKEN)
