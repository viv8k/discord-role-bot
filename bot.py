import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

@bot.event
async def on_member_update(before, after):
    booster_role_id = 1249722860126076949  # ←ブースターロールのID
    perk_roles = [
        1372488450581987419,  # 特典ロールハル
        1372488680152895499,  # 特典ロールシオン
        1372488751472709703   # 特典ロールアオイ
    ]

    before_roles = set([r.id for r in before.roles])
    after_roles = set([r.id for r in after.roles])

    was_booster = booster_role_id in before_roles
    is_booster = booster_role_id in after_roles

    if was_booster and not is_booster:
        roles_to_remove = [discord.Object(id=rid) for rid in perk_roles if rid in after_roles]
        if roles_to_remove:
            await after.remove_roles(*roles_to_remove)
            print(f'Removed perk role(s) from {after.display_name}')

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
