import discord
import datetime
import bilet
import os
from datetime import date
from discord.ext import commands

token = 'i_dont_show_my_token_kiddos'

# przedrostek do
client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print("bot is working")
    
@client.command()
async def finito(ctx):
    await ctx.bot.logout()



@client.command()
async def bot(ctx):
    await ctx.send("Siudamk to nie bot. Bot ma mniejszy ping.")

@client.command()
async def cidran(ctx):
    await ctx.send("Citroen")

@client.command()
async def test(ctx):
    print(ctx.author)
    print(ctx.message)
    await ctx.message.delete()
@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def franoll(ctx):
    await ctx.send("ma małego lol small pp")

@client.command()
async def penis(ctx):
    await ctx.send("twój jest mały")

@client.command()
async def simp(ctx):
    await ctx.send(ctx.author + " to simp")

@client.command()
async def maciek(ctx):
    await ctx.send("ma dużego członka")


@client.command()

async def kanar(ctx):
    # stwórz embeda do danych pociągu
    embed = discord.Embed(title="Twój dzisiejszy pociąg", description="Ponieżej trochę fajnych danych")

    #aktualna data w stringu MMDD
    dzis = date.today().strftime("%d/%m/%Y")
    dzis_form = dzis[3:5] + dzis[0:2]

    plik = ""
    for filename in os.listdir():
        if filename[0:3] == "mie":
            await ctx.send(file=discord.File(filename),delete_after=10)
        elif filename[0:3] == "dod":
            if dzis_form == filename[3:7]:
                await ctx.send(file=discord.File(filename),delete_after=10)
                plik = str(filename)

    #tworzenie embeda
    embed.add_field(name="Godzina", value=plik[8:12])
    embed.add_field(name="Miejsce", value=plik[14:17])
    embed.add_field(name="Wagon", value=plik[2:3])
    await ctx.message.channel.send(content=None, embed=embed)

    await ctx.message.delete()
        
        

client.run(token)