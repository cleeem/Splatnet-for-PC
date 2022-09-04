from PIL import Image, ImageDraw
from io import BytesIO


import splatnet2statink as sp

from discord import *
import discord.ui as bt
from discord.ext import commands


def addincsv(url_file,objet,newline =True, delimiter =  None):
    csv = open(url_file,'a',encoding='utf-8')
    if newline:
        csv.write((str(objet)+'\n'))
    else:
        csv.write(str(objet))
        csv.write(str(delimiter))
    csv.close()


client = Client()

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description="Bot de clem#1777", intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Ready !")
    activity = Game(name=f"!help\nOn {len(bot.guilds)} servers", type=1)
    await bot.change_presence(status=Status.online, activity=activity)


@bot.command()
async def report(ctx, *args):

    clem = bot.get_user(485851523247505409)
    await clem.send(f"{ctx.author} a éffectué la commande dans '{ctx.channel}' dans le serveur '{ctx.guild}'")
    await clem.send(str(args).replace("(","").replace('"',"").replace("'", "").replace(",", "").replace(")", ""))

    files = ctx.message.attachments
    for elt in files:
        temp : File = await elt.to_file()
        await clem.send(file=temp)

    test = await ctx.channel.create_invite()
    await clem.send(test)


@bot.command()
async def splatnet(ctx):
    for i in range(6):
        data : test.Stuff = test.get_stuff(indice=i)
        dico = {'fields': [
            {'inline': True, 'name': "New Price", 'value': f"{data.new_price} <:sp_coin:1010654259425062952>"}, 
            {'inline': True, 'name': "New Ability", 'value': data.new_main_emote},
            {'inline': True, 'name': "Brand", 'value': data.brand},

            {'inline': True, 'name': "Old Price", 'value': f"{data.old_price} <:sp_coin:1010654259425062952>"}, 
            {'inline': True, 'name': "old Ability", 'value': data.old_main_emote},
            {'inline': True, 'name': "Frequent Bonus", 'value': f"{data.frequent_bonus} {data.frequent_bonus_emote}"},
            
            ], 'color': 3394303, 'type': 'rich', 'description': f"Available until {data.end_time}", "title" : data.name_stuff}
        embed_stuff = Embed.from_dict(dico)
        embed_stuff.set_thumbnail(url=data.gear_url)
        await ctx.send(embed=embed_stuff)


@bot.command()
async def salmon(ctx):
    data = test.get_salmon()
    dico = {'fields': [
            {'inline': True, 'name': 'Maps :', 'value': data.current_map }, 
            {'inline': True, 'name': 'Weapons :', 'value': data.current_weapon_list},
            {'inline': True, 'name': "Date", 'value': f"{data.current_start_time} \nto \n{data.current_end_time}"},
            {'inline': False, 'name': "--------------------", 'value': f"Next Rotation \n**--------------------**"},
            {'inline': True, 'name': 'Next Map :', 'value': data.next_map }, 
            {'inline': True, 'name': 'Next Weapons :', 'value': data.next_weapon_list},
            {'inline': True, 'name': "Date", 'value': f"{data.next_start_time} \nto \n{data.next_end_time}"},
            ], 'color': 3394303, 'type': 'rich', 'description': "", "title" : "Salmon Run"}
    embed_salmon = Embed.from_dict(dico)

    await ctx.send(embed=embed_salmon)

@bot.command()
async def rotation(ctx):
    for key in test.list_mode:
        data = test.get_data()
        dico = {'fields': [
            {'inline': True, 'name': 'Maps :', 'value': data.current_maps }, 
            {'inline': True, 'name': 'Next Maps :', 'value': data.next_maps }, 
            {'inline': False, 'name': 'Mode :', 'value': data.current_mode},
            {'inline': False, 'name': 'Next Mode :', 'value': data.next_mode},             
            ], 'color': 3394303, 'type': 'rich', 'description': f"__Available as from {data.current_start_time[11:16]} to {data.current_end_time[11:16]}__", 'title': data.type}
        embed = Embed.from_dict(dico)
        
        if key == "league":
            embed.set_thumbnail(url="http://splating.ink/ligue.png")
        elif key == "gachi":
            embed.set_thumbnail(url="http://splating.ink/rank.png")
        elif key == "regular":
            embed.remove_field(3)
            embed.set_thumbnail(url="http://splating.ink/turf.png")
        
        embed.add_field(name="Additional Informations", value=f"[link to splatoon2.ink](https://splatoon2.ink/)")

        await ctx.send(embed=embed)

    

dico_stuff = {
    "Main Power Up" : "<:mpu:1009070739170799626>",
    "Ability Doubler" : "<:ab:1009070271661084733>",
    "Run Speed Up" : "<:rsu:1009070594911907901>",
    "Swim Speed Up" : "<:ssu:1009071046105759865>",
    "Ink Saver (Main)" : "<:ism:1009070712822181901>",
    "Ink Saver (Sub)" : "<:iss:1009071116842717275>",
    "Special Saver" : "<:ss:1009070872616763463>",
    "Special Charge Up" : "<:scu:1009070989474271322>",
    "Quick Respawn" : "<:qr:1009070895383466046>",
    "Quick Super Jump" : "<:qsj:1009070688256151624>",
    "Comeback" : "<:cbk:1009070396429062195>",
    "Ink Resistance Up" : "<:ir:1009070848931532881>",
    "Bomb Defense Up DX" : "<:bdu:1009070315814518816>",
    "Respawn Punisher" : "<:rsp:1009070563580452914>",
    "question mark" : "<:uk:1009071227043852310>",
    "uk" : "<:uk:1009071227043852310>",
    "Stealth Jump" : "<:sj:1009071141664604200>",
    "Special Power Up" : "<:spu:1009071008021483530>",
    "Ink Recovery Up" : "<:iru:1009070659843919913>",
    "Object Shredder" : "<:os:1009070825023995996>",
    "Last-Ditch Effort" : "<:lde:1009070541711343756>",
    "Ninja Squid" : "<:ns:1009071068360753242>",
    "Drop Roller" : "<:dr:1009070967785525299>",
    "Thermal Ink" : "<:ti:1009071170018095126>",
    "Tenacity" : "<:tnty:1009070763745234944>",
    "Opening Gambit" : "<:og:1009071094352838727>",
    "Haunt" : "<:hnt:1009070429064941628>",
    "Sub Power Up" : "<:sbpu:1009070353810735196>",
}

dico_spe = {
    "Tenta Missiles" : "<:missiles:1009101166732378232>",
    "Sting Ray" : "<:sting:1009101111526965269>",
    "Inkjet" : "<:inkjet:1009101175435563020>",
    "Splashdown" : "<:splashdown:1009101152434004070>",
    "Ink Armor" : "<:armor:1009101295170359327>",
    "Autobomb Laucher" : "<:autobomb:1009101223598764032>",
    "Burst-Bomb Laucher" : "<:burst:1009101252287811594> ",
    "Curling-Bomb Launcher" : "<:curling:1009101190925144105>",
    "Splat-Bomb Launcher" : "<:splat:1009101120955760740>",
    "Suction-Bomb Launcher" : "<:suction:1009101054207594556>",
    "Ink Storm" : "<:storm:1009101099489312860>",
    "Baller" : "<:baller:1009101289390604298>",
    "Bubble Blower" : "<:bubble:1009101278124711986>",
    "Booyah Bomb" : "<:booyah:1009101284055457913>",
    "Ultra Stamp" : "<:stamp:1009100969948229682>",
}


class Game:

    def __init__(self) -> None:
        pass

    def get_data(self, indice=0):
        data = sp.get_all(indice)
        return data

    def get_image_home(self):
        data = self.get_data()
        img_temp = data["image_gear"]
        scoreboard = Image.open(BytesIO(img_temp)).convert("RGB")
        scoreboard.save("image_home.png")
        
    def get_image_game(self, indice=0):
        data = self.get_data(indice=indice)
        img_temp = data["image_result"]
        result = Image.open(BytesIO(img_temp)).convert("RGB")
        result.save(f"image_results.png")

partie = Game()
# img_home = partie.get_image_home()
img_result = partie.get_image_game()

# import sys

# try:
#     sys.path.append("../token")
#     import token_bot
# except:
#     sys.path.append("/home/cleeem/python/token")
#     import token_bot
    
# token_run = token_bot.tokens["token_bot_splatnet"]

# bot.run(token_run)
