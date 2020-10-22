import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import os

bot = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print("Selamün Aleyküm, Bot Çevrimiçi!")
    print("İsim: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print(str(len(set(bot.get_all_members()))) + " tane üye aktif.")
    await bot.change_presence(activity=discord.Game(name="Compec'e Öğrenci Topluyor..."))

@bot.command(pass_context=True)
async def posta(ctx):
    await ctx.send("Ben CompecMan!")

@bot.command(pass_context=True)
async def a(ctx, member : discord.Member):
    urll = ["https://i.pinimg.com/originals/23/c1/b9/23c1b9ae331f780b4165bb670bae88d0.gif",
            "https://i.pinimg.com/originals/ec/c3/6d/ecc36d225dbf7c843a9e458720231c48.gif",
            "https://thumbs.gfycat.com/LankyFewCoelacanth-small.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name)
    embed.set_image(url = random.choice(urll))
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def sil (ctx, number):
    mgs = []
    number = int(number)
    async for x in ctx.Messageable.history(ctx.message.channel, limit=number):
        mgs.append(x)
    await ctx.delete_messages(mgs)

bot.run(os.environ.get('token'))
