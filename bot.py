import os

import discord
import openai

DISCORD_TOKEN = os.getenv("SMARTBOT_TOKEN") #Client secret for Discord bot, set as an env variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #Same for OpenAI