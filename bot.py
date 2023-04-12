import os

import discord
from discord import app_commands
import openai

DISCORD_TOKEN = os.getenv("SMARTBOT_TOKEN") #Client secret for Discord bot, set as an env variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #Same for OpenAI
GUILD_ID = os.getenv("GUILD_ID")
# OPENAI_ORG = os.getenv("OPENAI_ORG") unneeded unless you belong to multiple orgs

intents = discord.Intents.all() #needed for next line
client = discord.Client(intents=intents) #as of api v2.0 this is required
tree = app_commands.CommandTree(client) #to hold all commands

#openai.organization = "org-Rsl5JS63ShHy62MuJZS2RKtL"
openai.api_key = OPENAI_API_KEY
print(OPENAI_API_KEY)
openai.Model.list()

'''
@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=957119803397644378)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=957119803397644378))
    print("Ready!") #sync once ready

client.run(DISCORD_TOKEN)
'''