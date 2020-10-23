import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random


characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(7, 14)))


mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("marselinhani@gmail.com", os.environ.get('sifre'))

mesaj = MIMEMultipart()
mesaj["From"] = "marselinhani@gmail.com"      # Gönderen
mesaj["Subject"] = "Python Smtp ile Mail Gönderme"    # Konusu

body = "Parolanız: " + password

body_text = MIMEText(body, "plain")  #
mesaj.attach(body_text)

bot = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print("Selamün Aleyküm, Bot Çevrimiçi!")
    print("İsim: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print(str(len(set(bot.get_all_members()))) + " tane üye aktif.")
    await bot.change_presence(game=discord.Game(name="Compec'e Öğrenci Topluyor..."))

@bot.command(pass_context=True)
async def posta(ctx):
    await bot.say("Ben CompecMan!")

@bot.command(pass_context=True)
async def eposta(ctx, epostaadr):
    epostaadr = str(epostaadr)
    mesaj["To"] = epostaadr
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()

@bot.command(pass_context=True)
async def dogrula(ctx, dogrulakod):
    dogrulakod = dogrulakod
    if dogrulakod == password:
        await bot.say("Hesabın doğrulandı!")
    else:
        await bot.say("Tekrar Dene!")

@bot.command(pass_context=True)
async def a(ctx, member : discord.Member):
    urll = ["https://i.pinimg.com/originals/23/c1/b9/23c1b9ae331f780b4165bb670bae88d0.gif",
            "https://i.pinimg.com/originals/ec/c3/6d/ecc36d225dbf7c843a9e458720231c48.gif",
            "https://thumbs.gfycat.com/LankyFewCoelacanth-small.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name)
    embed.set_image(url = random.choice(urll))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def sil (ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(x)
    await bot.delete_messages(mgs)

bot.run(os.environ.get('token'))
