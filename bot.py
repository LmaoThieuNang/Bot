import discord
from discord import app_commands
from discord.ext import commands
import os

database = {
    "Kenn": ["k3nn", "abaddon"],
    "Choco": ["choco"],
    "tt": ["catto"],
    "Rudi": ["yophonelinin"],
    "Ema": ["emaxwo", "emaxw2"],
    "Rashet": ["hung", "hung2", "hung3", "hung4", "hung5", "hung6"],
    "Khánh": ["khánhdeptrai"],
    "Addy": ["addydesuno", "addy2", "addy3", "addy4"],
    "Imou": ["imoutofide", "anthifide", "lua", "dust", "insanity"],
    "Ann": ["ann"],
    "vibing": ["holy gun-knight", "furnace's finale", "blackcrownedlord", "blackcrownedsage"],
    "Bẻo": ["bẻo"],
    "Xikuku": ["magiciancatto", "assistantcatto", "shimoekoharu", "sandwolfofabydos"],
    "minhvu": ["podeastive", "nothinghere"],
    "Kepper": ["kepper sthe"],
    "banlongnhulon": ["banlongnhulon", "clone1", "clone2", "clone3", "clone4", "clone5"],
    "LTG": ["nanbawan", "ltg", "thegreastest", "ahblos", "hachimi", "chetgipeeti", "donk"],
    "Leraiz": ["leraiz"]
}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"Logged in as {bot.user}")
    except Exception as e:
        print(f"Error syncing: {e}")

@bot.tree.command(name="find", description="Find which group a user is in")
async def find(interaction: discord.Interaction, username: str):
    username = username.lower()
    found_group = None

    for group, members in database.items():
        if username in members:
            found_group = group
            break

    if found_group:
        await interaction.response.send_message(f"{username} is {found_group}")
    else:
        await interaction.response.send_message(f"{username} not found in the database.")

TOKEN = os.getenv("DISCORD")
bot.run(TOKEN)

