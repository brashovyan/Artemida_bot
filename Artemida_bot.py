from discord.ext import commands
from config import settings
import json
import requests
import discord
import random
#from discord.utils import get

from asyncio import sleep
from youtube_dl import YoutubeDL

import os
from bs4 import BeautifulSoup
from balaboba import balaboba

#перед запуском не забудь вставить токен
intents = discord.Intents.default()
intents.members = True

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
bot = commands.Bot(command_prefix=settings['prefix'], intents = intents, help_command=None)  # Так как мы указали префикс в settings.
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

@bot.command()
async def p(ctx): #случайная пикча с интернета (с определенного сайта)
    r = random.randint(1, 14)
    if r == 1:
        response = requests.get('https://some-random-api.ml/img/pikachu')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Anime')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    elif r == 2:
        response = requests.get('https://some-random-api.ml/animu/wink')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Anime')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
    elif r == 3:
        response = requests.get('https://some-random-api.ml/animu/pat')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Anime')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
    elif r == 4:
        response = requests.get('https://some-random-api.ml/meme')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Meme')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 5:
        response = requests.get('http://aws.random.cat/meow')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Cat')
        embed.set_image(url=json_data['file'])
        await ctx.send(embed=embed)
    elif r == 6:
        response = requests.get('https://some-random-api.ml/animal/panda')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Panda')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 7:
        response = requests.get('https://some-random-api.ml/animal/dog')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Dog')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 8:
        response = requests.get('https://some-random-api.ml/animal/cat')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Cat')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 9:
        response = requests.get('https://some-random-api.ml/animal/fox')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Fox')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 10:
        response = requests.get('https://some-random-api.ml/animal/red_panda')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Red Panda')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 11:
        response = requests.get('https://some-random-api.ml/animal/koala')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Koala')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 12:
        response = requests.get('https://some-random-api.ml/animal/birb')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Bird')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 13:
        response = requests.get('https://some-random-api.ml/animal/raccoon')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Racoon')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)
    elif r == 14:
        response = requests.get('https://some-random-api.ml/animal/kangaroo')
        json_data = json.loads(response.text)  # Извлекаем JSON

        embed = discord.Embed(color=0xff9900, title='Random Kangaroo')
        embed.set_image(url=json_data['image'])
        await ctx.send(embed=embed)

@bot.command() #случайное число от 0 до 100
async def roll(message):
    r = random.randint(0, 100)
    await message.send(f"{message.author.mention }: {str(r)}")

@bot.command() #цитата из аниме (пока на английском)
async def s(ctx):
    response = requests.get('https://some-random-api.ml/animu/quote')
    json_data = json.loads(response.text)  # Извлекаем JSON

    s = "Цитата: " + json_data['sentence']+"\n" + "\nАниме: " + json_data['anime'] + "\nПерсонаж: " + json_data['characther']
    await ctx.send(s)

@bot.command() #музыка с ютуба. $play ссылка
async def play(ctx, arg):
    global vc

    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    while vc.is_playing():
        await sleep(1)

    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(arg, download=False)
    URL = info['formats'][0]['url']
    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))

@bot.command() #локальная музыка с компа
async def playl(ctx):
    global vc
    i = 0
    path = "C:\\Games\\Muzlo" #путь до папки с музыкой. умеет скипать то, что не может воспроизвести
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))

    l = list(range(0, len(filelist)))
    random.shuffle(l)

    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается. Если нет, то повторите попытку через минуту.')
    else:
        while True:
            while vc.is_playing():
                await sleep(1)
            if not vc.is_paused():
                if i != (len(filelist)-1):
                    i += 1
                    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=filelist[l[i]]))
                else:
                    i = 0
                    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=filelist[l[i]]))

@bot.command()
async def anekdot(ctx):
    page = requests.get(f"https://vse-shutochki.ru/anekdoty/{random.randint(1, 2059)}")
    page1 = page.content
    soup = BeautifulSoup(page1, "lxml")
    soup1 = soup.find_all("div", {"class":"post"})
    print(soup1)
    str = soup1[random.randint(0, len(soup1)-1)].text.split("\n")
    await ctx.send(str[0])

@bot.command()
async def stop(ctx):
    await vc.disconnect()

@bot.command()
async def skip(ctx):
    try:
        await vc.pause()
        await vc.resume()
    except:
        vc.stop()

@bot.command()
async def bal(ctx):
    str = ctx.message.content.split("$bal ")
    with requests.Session() as session:
         response = balaboba(str[1], intro=6, session=session)
    await ctx.send(response)

@bot.command()
async def film(ctx):
    page = requests.get(f"https://randomfilm.ru")
    page1 = page.content
    soup = BeautifulSoup(page1, "lxml")
    title1 = soup.find_all("h2")
    inf = soup.find_all("tr")
    st = str(inf).split('\n')

    year = st[0]
    year = year[173:len(year)-5]

    country = st[1]
    country = country[18:len(country)-5]

    genre = st[2]
    genre = genre[16:len(genre)-5]

    #print(st[3]) #yt]]недоделал продолжительность, режиссера и актера - они есть не увсех фильмов
    await ctx.send(f"{str(title1)[5:len(title1)-7]}\n\nГод: {year}\nСтрана: {country}\nЖанр: {genre}")

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
    await message.send("Мои команды:\n$p - случайная пикча\n$roll - случайное число от 0 до 100\n"
                       "$s - случаная цитата из аниме (на английском)\n$play + ссылка - играет музыку с ютуба\n"
                       "$playl - играет музыку из моего локального плейлиста\n$skip - следующий трек\n"
                       "$stop - отключает музыку\n$anekdot - отправляет анекдот\n"
                       "$bal + сообщение - Балабоба от Яндекса\n"
                       "$film - случайный фильм\n$who - участники голосового канала")

bot.run(settings['token'])