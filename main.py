import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Intents
import json
import os
import asyncio
from googlesearch import search
import requests



intents = Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="!", intents=intents)


 

@bot.event
async def on_ready():


token = ("token here yuh")
bot.run(token)