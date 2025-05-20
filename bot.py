import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

    guild = bot.guilds[0]  # 最初に参加しているサーバーを使う
    print(f'Checking members in guild: {guild.name}')

    booster_role_id = 1249722860126076949
    perk_roles = [
        1372488450581987419,  # 特典ロールハル
        1372488680152895499,  # 特典ロールシオン
        1372488751472709703   # 特典ロールアオイ
    ]

    removed_count = 0
    async for member in guild.fetch_members(limit=None):
        role_ids = [r.id for r in member.roles]
        if booster_role_id not in role_ids:
            to_remove = [discord.Object(id=rid) for rid in perk_roles if rid in role_ids]
            if to_remove:
                await member.remove_roles(*to_remove)
                print(f'Removed perk roles from {member.display_name}')
                removed_count += 1

    print(f'Removal complete. {removed_count} member(s) updated.')
    await bot.close()  # 終了させる

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
