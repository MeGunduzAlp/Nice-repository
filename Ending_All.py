import random

import os

import discord

import requests

from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event

async def on_ready():

    print(f'{bot.user} olarak giriş yaptık')

@bot.command()

async def hello(ctx):

    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()

async def heh(ctx, count_heh = 5):

    if count_heh > 1000:

        await ctx.send("Yok Daha Neler")

    else:

        await ctx.send("he"* count_heh)

@bot.command()

async def gunduz(ctx,a):

    await ctx.send("Merhaba Gündüz" * int(a) )

@bot.command()

async def tesekkur(ctx,a):

    await ctx.send("Bir Şey Değil" * int(a) )
@bot.command()
async def hey(ctx,a):

    await ctx.send("ne" * int(a) )

@bot.command()
async def antalya(ctx,a):

    await ctx.send("Konyaaltı'nda doğdum" * int(a) )

@bot.command()
async def turkiye(ctx,a):

    await ctx.send("81 ili vardır.Antalya'da doğdum" * int(a) )

@bot.command()
async def dunya(ctx,a):

    await ctx.send("195 ülkesi vardır.Türkiye'de doğdum" * int(a) )


@bot.command()
async def atik(ctx):

    await ctx.send("İşte yapabileceğin 11 şey:Son yıllarda pek çok evde kullanılan tek kullanımlık plastik buz torbaları yerine silikon buzlukları tercih edebilirsiniz.Buzdolabı poşeti, streç film gibi ürünler yerine kapaklı saklama kaplarını kullanabilirsiniz.Plastik saklama kapları hem sağlığınıza hem de çevreye zarar verebilir. Bu nedenle ihtiyacınız varsa daha uzun ömürlü ve daha sağlıklı olan cam saklama ürünlerini satın almalısınız.İçerisinde çevreye ve size zarar verebilecek pek çok metal bulunan tek kullanımlık piller yerine şarj edilebilir pilleri kullanarak çevre kirliliğini engellemek için bir adım atabilirsiniz.Evinizde hem uzun ömürlü hem de daha az enerji tüketip bütçenizi koruyan LED ampuller kullanabilirsiniz.Kâğıt peçeteler ve kâğıt havlular yerine eskiden de kullanılan yıkanabilir el bezlerini tercih ederek katı atıkları azaltma konusunda daha başarılı olabilirsiniz.Pratik olduğu için plastik ya da kâğıt bardak gibi ürünleri tercih etmemelisiniz. Bir termos alarak evin dışında içeceğiniz içecekler için bu ürünü kullanabilirsiniz.Alışverişe çıktığınızda plastik poşetler yerine bez çantaları ya da alışveriş filelerini tercih edebilirsiniz.Plastik kullanımını azaltmak için plastik ambalajlı ürünler yerine cam ambalaj içerisinde sunulan ürünleri seçebilirsiniz.Plastikten yapılan diş fırçaları yerine bambu gibi doğal malzemelerden üretilen diş fırçalarını tercih edebilirsiniz.Hayat kaynağımız olan suyu tüketmek için pet şişeler yerine su arıtma cihazları sayesinde musluktan akan sağlıklı, lezzetli ve ekonomik suyu tüketerek hem bütçenizi hem de doğayı korumuş olursunuz.")


def gelkedi():
    url = 'https://api.thecatapi.com/v1/images/search'

    res = requests.get(url)

    data = res.json()

    print(data)

    print(data[0])

    return data[0]["url"]


@bot.command()
async def kedi(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır'''

    image_url = gelkedi()

    await ctx.send(image_url)


bot.run("")
