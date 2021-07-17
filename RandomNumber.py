import discord
import random

bot = commands.Bot(command_prefix = "!")

@bot.command()
async def num(ctx)
  ctx.send(f"{random.randint(0,9999)"})
  
bot.run(BOT TOKEN)
