import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! บอทออนไลน์แล้ว")

@bot.command()
async def hello(ctx):
    await ctx.send(f"สวัสดี {ctx.author.mention} !")

bot.run(os.getenv("DISCORD_TOKEN"))
