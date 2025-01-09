import asyncio
import discord
import hmac
import requests
import hashlib
from secrets import TOKEN_LOCAL_SERVER, DISCORD_BOT_TOKEN

# HMAC secret for server interactions
secret = bytes.fromhex(TOKEN_LOCAL_SERVER)

# Generate challenge for server interaction
def generate_challenge():
    challenge = requests.post("https://play.jaysee.ca/generate_challenge").json()["challenge"]
    challenge_result = hmac.new(secret, bytes.fromhex(challenge), hashlib.sha256).hexdigest()
    return challenge, challenge_result

# Server control commands
def start_server(server_name):
    challenge, challenge_result = generate_challenge()
    resp = requests.post(
        "https://play.jaysee.ca/health",
        params={"challenge": challenge, "challenge_result": challenge_result, "authority": "copium_bot"}
    ).json()

    if resp["status"] != 'ok' or not resp["authorized"]:
        return f"ERROR: {resp}"

    challenge, challenge_result = generate_challenge()
    resp = requests.post(
        f"https://play.jaysee.ca/servers/{server_name}/start",
        params={"challenge": challenge, "challenge_result": challenge_result, "authority": "copium_bot"}
    ).json()
    return resp

def stop_server(server_name):
    challenge, challenge_result = generate_challenge()
    resp = requests.post(
        "https://play.jaysee.ca/health",
        params={"challenge": challenge, "challenge_result": challenge_result, "authority": "copium_bot"}
    ).json()

    if resp["status"] != 'ok' or not resp["authorized"]:
        return f"ERROR: {resp}"

    challenge, challenge_result = generate_challenge()
    resp = requests.post(
        f"https://play.jaysee.ca/servers/{server_name}/stop",
        params={"challenge": challenge, "challenge_result": challenge_result, "authority": "copium_bot"}
    )
    return resp.json()

def get_status(server_name):
    challenge, challenge_result = generate_challenge()
    resp = requests.post(
        f"https://play.jaysee.ca/servers/{server_name}/query",
        params={"challenge": challenge, "challenge_result": challenge_result, "authority": "copium_bot"}
    )
    return resp.json()

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore bot's own messages

    # Commands for server control
    if message.content.startswith("!start_server"):
        server_name = message.content.split(" ", 1)[-1]
        response = start_server(server_name)
        await message.channel.send(f"Starting server `{server_name}`...\nResponse: {response}")

    elif message.content.startswith("!stop_server"):
        server_name = message.content.split(" ", 1)[-1]
        response = stop_server(server_name)
        await message.channel.send(f"Stopping server `{server_name}`...\nResponse: {response}")

    elif message.content.startswith("!status"):
        server_name = message.content.split(" ", 1)[-1]
        response = get_status(server_name)
        await message.channel.send(f"Status of server `{server_name}`:\n{response}")

    # Help command
    elif message.content.startswith("!help"):
        help_text = (
            "**Game Server Bot Commands**:\n"
            "`!start_server <server_name>` - Start a specified server.\n"
            "`!stop_server <server_name>` - Stop a specified server.\n"
            "`!status <server_name>` - Query the status of a server.\n"
            "`!help` - Display this help message."
        )
        await message.channel.send(help_text)

client.run(DISCORD_BOT_TOKEN)
