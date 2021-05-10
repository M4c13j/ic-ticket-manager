import bilet

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
        


