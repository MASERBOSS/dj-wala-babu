import discord
import os
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(";;;"))
bot.remove_command('help')
bot.initials = ('modules.misc', 'modules.music')

@bot.check
async def _bot_protection(ctx):
    return not ctx.author.bot

@bot.event
async def on_ready():
    print('Bot is ready!')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Streaming(name=f"your music! ;;;help", url="https://twitch.tv/streamer"))

if __name__ == "__main__":
	for extension in bot.initials:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f'Failed to load extension {extension}: {e}')

bot.run(os.environ.get('TOKEN'))