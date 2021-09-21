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

#перед запуском не забудь вставить токен

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
bot = commands.Bot(command_prefix=settings['prefix'])  # Так как мы указали префикс в settings.
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

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)

        URL = info['formats'][0]['url']
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))

        while vc.is_playing():
            await sleep(1)
        if not vc.is_paused():
            await vc.disconnect()

@bot.command() #локальная музыка с моего компа
async def playl(ctx):
    global vc
    i = 0
    path = "C:\\Games\\Muzlo"
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))

    l = list(range(0, len(filelist)-1))
    random.shuffle(l)

    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        while 1>0:
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
async def skipl(ctx):
    vc.stop()

@bot.command()
async def h(message):
    await message.send("Мои команды:\n$p - случайная пикча\n$roll - случайное число от 0 до 100\n$s - случаная цитата из аниме (на английском)\n$play + ссылка - играет музыку с ютуба (очередь в разработке)\n$playl - играет музыку из моего локального плейлиста\n$skipl - следующий локальный трек")

bot.run(settings['token'])