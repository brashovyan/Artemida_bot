from discord.ext import commands
from config import settings
import requests
import discord
import random
from asyncio import sleep
import os
from bs4 import BeautifulSoup
import yt_dlp

#перед запуском не забудь вставить токен
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=settings['prefix'], intents = intents, help_command=None)  # Так как мы указали префикс в settings.
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
ytdl_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": False,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": (
        "0.0.0.0"
    ),  # Bind to ipv4 since ipv6 addresses cause issues at certain times
}


@bot.command() #случайное число от 0 до 100
async def roll(message):
    r = random.randint(0, 100)
    await message.send(f"{message.author.mention }: {str(r)}")


@bot.command() #музыка с ютуба. $play ссылка
async def play(ctx, arg):
    try:
        if "www.youtube.com" in str(arg):
            if str(arg).count('=') < 2:
                global vc

                try:
                    voice_channel = ctx.message.author.voice.channel
                    vc = await voice_channel.connect()
                except:
                    try:
                        if vc.is_playing():
                            await ctx.send(f'{ctx.message.author.mention}, Видео добавлено в очередь.')
                        else:
                            await ctx.send(f'{ctx.message.author.mention} Ошибка! Возможно, вы не находитесь в голосовом канале. Либо попробуйте через минуту.')
                    except:
                        await ctx.send(f'{ctx.message.author.mention} Ошибка! Возможно, вы не находитесь в голосовом канале. Либо попробуйте через минуту.')


                while vc.is_playing():
                    await sleep(1)

                with yt_dlp.YoutubeDL(ytdl_options) as ydl:
                    info = ydl.extract_info(arg, download=False)
                    URL = info['url']
                    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))

            else:
                await ctx.send(f'{ctx.message.author.mention}, плейлисты не проигрываются(')

        else:
            await ctx.send(f'{ctx.message.author.mention}, плейлисты не проигрываются(')
                     
    except:
        await ctx.send(f'{ctx.message.author.mention}, плейлисты не проигрываются(')


# @bot.command() #локальная музыка с компа
# async def playl(ctx):
#     global vc
#     i = 0
#     path = "D:\\Muzlo" #путь до папки с музыкой. умеет скипать то, что не может воспроизвести
#     filelist = []
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             filelist.append(os.path.join(root, file))
#
#     l = list(range(0, len(filelist)))
#     random.shuffle(l)
#
#     try:
#         voice_channel = ctx.message.author.voice.channel
#         vc = await voice_channel.connect()
#     except:
#         try:
#             if vc.is_playing():
#                 await ctx.send(f'{ctx.message.author.mention}, Ошибка! Бот уже что-то проигрывает, скорее всего ютуб. Сначала выключите его, написав $leave или $stop.')
#             else:
#                 await ctx.send(f'{ctx.message.author.mention} Ошибка! Возможно, вы не находитесь в голосовом канале.')
#         except:
#             await ctx.send(f'{ctx.message.author.mention} Ошибка! Возможно, вы не находитесь в голосовом канале.')
#
#     if vc.is_playing() == False:
#         while True:
#             while vc.is_playing():
#                 await sleep(1)
#             if not vc.is_paused():
#                 if i != (len(filelist)-1):
#                     i += 1
#                     vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=filelist[l[i]]))
#
#                 else:
#                     i = 0
#                     vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=filelist[l[i]]))
#                 n = filelist[l[i]].split('\\')
#                 n = n[len(n) - 1]
#                 n = n[:-4]
#                 await ctx.send(f'Сейчас проигрывается: {n}')


# короче дискорд без танцев с бубном теперь на даёт отправлять запросы в инет(
# python requests и сайт тут не причем
# @bot.command()
# async def anekdot(ctx):
#     page = requests.get(f"https://vse-shutochki.ru/anekdoty/{random.randint(1, 2078)}")
#     page1 = page.content
#     soup = BeautifulSoup(page1, "lxml")
#     soup1 = soup.find_all("div", {"class":"post"})
#     #print(soup1)
#     str = soup1[random.randint(0, len(soup1)-1)].text.split("\n")
#     await ctx.send(str[0])


@bot.command()
async def stop(ctx):
    global vc
    await vc.disconnect()
    vc = ""


@bot.command()
async def leave(ctx):
    global vc
    await vc.disconnect()
    vc = ""


@bot.command()
async def skip(ctx):
    try:
        await vc.pause()
        await vc.resume()
    except:
        vc.stop()

# аналогично надо воевать с дискордом (см. anekdot)
# @bot.command()
# async def film(ctx):
#     page = requests.get(f"https://randomfilm.ru")
#     page1 = page.content
#     soup = BeautifulSoup(page1, "lxml")
#     title1 = soup.find_all("h2")
#     inf = soup.find_all("tr")
#     st = str(inf).split('\n')
#
#     year = st[0]
#     year = year[173:len(year)-5]
#
#     country = st[1]
#     country = country[18:len(country)-5]
#
#     genre = st[2]
#     genre = genre[16:len(genre)-5]
#
#     #print(st[3]) #yt]]недоделал продолжительность, режиссера и актера - они есть не увсех фильмов
#     await ctx.send(f"{str(title1)[5:len(title1)-7]}\n\nГод: {year}\nСтрана: {country}\nЖанр: {genre}")


@bot.command()
async def who(ctx):
    try:
        #users = ctx.guild.members
        voice_channel = ctx.message.author.voice.channel
        st = f'Сейчас в вашем голосовом канале "{voice_channel}" находятся:\n'
        users = voice_channel.members
        for member in users:
            if member.nick is None:
                st += (member.name + "\n")
            else:
                st += (member.nick + "\n")
        await ctx.send(st)
    except:
        await ctx.send(f'{ctx.message.author.mention} В данный момент вы не находитесь в голосовом канале. Зайдите в тот канал, из которого вы хотите получить список участников.')


@bot.command()
async def help(message):
    await message.send("Мои команды:\n$roll - случайное число от 0 до 100"
                       "\n$play + ссылка - играет музыку с ютуба\n"
                       # "$playl - играет музыку из моего локального плейлиста\n$skip - следующий трек\n"
                       "$stop - отключает музыку (бот ливает)\n"
                       "$who - участники голосового канала\n$leave - бот покидает голосовой канал")

bot.run(settings['token'])