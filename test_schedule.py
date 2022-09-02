import json
import time
from urllib import response
import requests


##################################
# Toutes les données nécessaires #
##################################


dico_emote = {
    "Clam Blitz" : "<:cb:853656449825243166>",
    "Rainmaker" : "<:rm:853656465725456424>",
    "Tower Control" : "<:tc:853656463846146068>",
    "Splat Zones" : "<:sz:853656465423990807>",
    "Turf War" : "<:turf:1010462680663994418>"
}

dico_armes = {
    "Sploosh-o-matic" : "<:sploosh:1010480744860221440>",
    "Splattershot Jr." : "<:jr:1010480455935606835>",
    "Splash-o-matic" : "<:splash:1010480508263739442>",
    "Splattershot" : "<:splattershot:1010480502341378078>",
    ".52 Gal" : "<:52:1010480347051470889>",
    "N-ZAP '85" : "<:zap:1010480527041626212>",
    "Splattershot Pro" : "<:pro:1010480489150283797>",
    ".96 Gal" : "<:96:1010480370225000488>",
    "Jet Squelcher" : "<:vjs:1010480520624349246>",
    "Luna Blaster" : "<:luna:1010480475581718559>",
    "Blaster" : "<:blaster:1010480387379703879>",
    "Range Blaster" : "<:rb:1010480513833783296>",
    "Clash Blaster" : "<:clash:1010480411757002752>",
    "Rapid Blaster" : "<:rapid:1010480495102005281>",
    "Rapid Blaster Pro" : "<:rapid_pro:1010480546431897680>",
    "L-3 Nozzlenose" : "<:l3:1010480468896002049>",
    "H-3 Nozzlenose" : "<:h3:1010480445378543687>",
    "Squeezer" : "<:squeezer:1010480536365576272>",
    "Carbon Roller" : "<:carbon:1010480104100606002>",
    "Splat Roller" : "<:roller:1010480240310628372>",
    "Dynamo Roller" : "<:dynamo:1010480141153095731>",
    "Flingza Roller" : "<:flingza:1010480170009890837>",
    "Inkbrush" : "<:brush:1010480211462201374>",
    "Octobrush" : "<:octobrush:1010480271633694760>",
    "Classic Squiffer" : "<:squiffer:1010479578654978119>",
    "Splat Charger" : "<:charger:1010479663367331871>",
    "Splatterscope" : "<:scope:1010479699861970984>",
    "E-liter 4K" : "<:eliter:1010479738592165959>",
    "E-liter 4K Scope" : "<:scope_e:1010479773698498610>",
    "Bamboozler 14 Mk I" : "<:bamboo:1010479551522033674>",
    "Goo Tuber" : "<:gootuber:1010479619562029076>",
    "Slosher" : "<:slosher:1010480833368428594>",
    "Tri-Slosher" : "<:tri:1010480890545193072>",
    "Sloshing Machine" : "<:machine:1010480865450676305>",
    "Bloblobber" : "<:blob:1010480782315372564>",
    "Explosher" : "<:explo:1010480807955152917>",
    "Mini Splatling" : "<:mini:1010480997260865678>",
    "Heavy Splatling" : "<:heavy:1010481066408149025>",
    "Hydra Splatling" : "<:hydra:1010480972552228884>",
    "Ballpoint Splatling" : "<:bp:1010480947373817876>",
    "Nautilus 47" : "<:naut:1010481030689472532>",
    "Dapple Dualies" : "<:dapple:1010479913746309130>",
    "Splat Dualies" : "<:dualies:1010479952006750240>",
    "Glooga Dualies" : "<:glooga:1010480064770605087>",
    "Dualie Squelchers" : "<:vds:1010479983501791252>",
    "Dark Tetra Dualies" : "<:tetra:1010480021611221042>",
    "Splat Brella" : "<:brella:1010479399881150474>",
    "Tenta Brella" : "<:tent:1010479510581411880>",
    "Undercover Brella" : "<:under:1010479455338242069>",
    "Random" : "<:uk:1009071227043852310>",

}

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


list_mode = ["regular", "gachi", "league"]

url_assets = "https://splatoon2.ink/assets/splatnet/"


#############################################################################
# Creation des différentes classes pour accéder aux données plus facilement #
#############################################################################

class Salmon:
    def __init__(self, data) -> None:
        self.current_map = data["details"][0]["stage"]["name"]
        self.current_start_time = time.ctime(int(data["schedules"][0]["start_time"]))
        self.current_end_time = time.ctime(int(data["schedules"][0]["end_time"]))

        current_weapon_list = []
        if "coop_special_weapon" in data["details"][0]["weapons"][0]:
            for elt in data["details"][0]["weapons"]:
                current_weapon_list.append(elt["coop_special_weapon"]["name"])

        else :
            for elt in data["details"][0]["weapons"]:
                current_weapon_list.append(elt["weapon"]["name"])

        self.current_weapon_list = f"{dico_armes[current_weapon_list[0]]}  |  {dico_armes[current_weapon_list[1]]}  |  {dico_armes[current_weapon_list[2]]}  |  {dico_armes[current_weapon_list[3]]} "


        self.next_map = data["details"][1]["stage"]["name"]
        self.next_start_time = time.ctime(int(data["schedules"][0]["start_time"]))
        self.next_end_time = time.ctime(int(data["schedules"][0]["end_time"]))

        next_weapon_list = []
        if "coop_special_weapon" in data["details"][1]["weapons"][0]:
            for elt in data["details"][1]["weapons"]:
                next_weapon_list.append(elt["coop_special_weapon"]["name"])

        else :
            for elt in data["details"][1]["weapons"]:
                next_weapon_list.append(elt["weapon"]["name"])
        
        self.next_weapon_list = f"{dico_armes[next_weapon_list[0]]}  |  {dico_armes[next_weapon_list[1]]}  |  {dico_armes[next_weapon_list[2]]}  |  {dico_armes[next_weapon_list[3]]} "
    

    def __str__(self) -> str:
        return f"Current Rotation : \nMaps : {self.current_map} \n{self.current_weapon_list} \n{self.current_start_time} to {self.current_end_time} \n\nNext Rotation : \nMaps : {self.next_map} \n{self.next_weapon_list}\n{self.next_start_time} {self.next_end_time}"


class Rotation:
    def __init__(self, data, key) -> None:
        data = data[key]
        self.type = data[0]["game_mode"]["name"]

        self.current_stage_a = data[0]["stage_a"]["name"]
        self.current_stage_b = data[0]["stage_b"]["name"]
        self.current_maps = f"{self.current_stage_a} \n{self.current_stage_b}"
        self.current_mode = data[0]["rule"]["name"]
        self.current_start_time = time.ctime(int(data[0]["start_time"]))[11:16]
        self.current_end_time = time.ctime(int(data[0]["end_time"]))[11:16]

        self.next_stage_a = data[1]["stage_a"]["name"]
        self.next_stage_b = data[1]["stage_b"]["name"]
        self.next_maps = f"{self.next_stage_a} \n{self.next_stage_b}"
        self.next_mode = data[1]["rule"]["name"]
        self.next_start_time = str(time.ctime(int(data[1]["start_time"])))[11:16]
        self.next_end_time = time.ctime(int(data[1]["end_time"]))[11:16]


    def __str__(self) -> str:
        return f"Current Rotation : \n\n{self.current_maps} \nMode : {self.current_mode}\n{self.current_start_time} to {self.current_end_time} \n\n\n\nNext Rotation : \n{self.next_maps} \nMode : {self.next_mode}\n{self.next_start_time} to {self.next_end_time}"


class Stuff:
    def __init__(self, data, indice=0):
        self.name_stuff = data[indice]["gear"]["name"]
        self.brand = data[indice]["gear"]["brand"]["name"]
        self.new_price = data[indice]["price"]
        self.old_price = data[indice]["original_gear"]["price"]
        
        self.new_main = data[indice]["skill"]["name"]
        self.new_main_emote = dico_stuff[self.new_main]
        self.old_main = data[indice]["original_gear"]["skill"]["name"]
        self.old_main_emote = dico_stuff[self.old_main]

        self.gear_url = url_assets + data[indice]["gear"]["image"]
        self.end_time = str(time.ctime(int(data[indice]["end_time"])))[11:16]
        try:
            self.frequent_bonus = data[indice]["gear"]["brand"]["frequent_skill"]["name"]
            self.frequent_bonus_emote = dico_stuff[self.frequent_bonus]
        except:
            self.frequent_bonus_emote = dico_stuff["uk"]
            self.frequent_bonus = "None"            
    
    def __str__(self) -> str:
        return f"{self.gear_url} {self.brand} jusqu'au {self.end_time} \nold : {self.old_main} {self.old_price} \nnew : {self.new_main} {self.new_price} "



########################################################
# Fonctions permettant au bot de récupérer les données #
########################################################


def get_salmon():
    url_salmon = "https://splatoon2.ink/data/coop-schedules.json"
    response_salmon = requests.get(url=url_salmon)
    data_salmon = json.loads(response_salmon.text)

    salmon_data = Salmon(data=data_salmon)
    return salmon_data


def get_data(key):
    url = "https://splatoon2.ink/data/schedules.json"
    response_maps = requests.get(url=url)
    data_maps = json.loads(response_maps.text)

    rotation_data = Rotation(data_maps, key)
    return rotation_data


def get_stuff(indice):
    url_stuff = "https://splatoon2.ink/data/merchandises.json"
    response_stuff = requests.get(url=url_stuff)
    data_stuff = json.loads(response_stuff.text)
    data_stuff = data_stuff["merchandises"]
    
    stuff_data = Stuff(data=data_stuff, indice=indice)
    return stuff_data
