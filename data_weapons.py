import requests
import json


response = requests.get(
    url = "https://leanny.github.io/splat3/data/mush/099/WeaponInfoMain.json"
)

data = json.loads(response.text)
dico = {}

def get_all_weapons_info():
    for elt in data:
        if len(str(elt["Id"])) <= 4:
            dico[elt["Id"]] = elt


url_image = "https://leanny.github.io/splat3/images/weapon_flat/Path_Wst_"


dico_id_armes = {
    250: 'Rapid Blaster Pro',
    230: 'Clash Blaster', 
    240: 'Rapid Blaster', 
    220: 'Range Blaster', 
    210: 'Blaster', 
    200: 'Luna Blaster', 
    1100: 'Inkbrush', 
    1110: 'Octobrush', 
    2060: 'Gootuber', 
    2050: 'Bamboozler', 
    2040: 'E-Liter Scope', 
    2030: 'E-Liter', 
    2020: 'Splatterscope', 
    2010: 'Charger', 
    2000: 'Squiffer', 
    5030: 'Dualies Squelshers', 
    5020: 'Glooga Dualies', 
    5010: 'Dualies', 
    5000: 'Dapple Dualies', 
    5040: 'Tetra Dualies', 
    1000: 'Carbon Roller', 
    1020: 'Dynamo Roller', 
    1030: 'Flingza Roller', 
    1010: 'Roller', 
    8010: 'Splatana', 
    8000: 'Heavy Splatana',
    6020: 'Undercover Brella', 
    6000: 'Brella', 
    6010: 'Tenta Brella', 
    30: 'Aerospray', 
    70: 'Splattershot Pro', 
    10: 'Splattershot Jr', 
    400: 'Squeezer', 
    50: '.52 Gal', 
    80: '.96 Gal', 
    90: 'Jet Squelsher', 
    40: 'Splattershot', 
    20: 'Splash-o-matic', 
    60: 'Nzap', 
    0: 'Sploosh-o-matic', 
    310: 'H-3 Nozzlenose', 
    300: 'L-3 Nozzlenose', 
    3030: 'Bloblober', 
    3010: 'Tri Slosher', 
    3020: 'Sloshing Machine', 
    3000: 'Slosher', 
    3040: 'Explosher', 
    4030: 'Ballpoint Splatling', 
    4020: 'Hydra Splatling', 
    4000: 'Mini Splatling', 
    4040: 'Nautilus', 
    4010: 'Heavy Splatling', 
    7010: 'Stringer'
}

dico_armes_id = {
    'Rapid Blaster Pro': 250, 
    'Clash Blaster': 230, 
    'Rapid Blaster': 240, 
    'Range Blaster': 220, 
    'Blaster': 210, 
    'Luna Blaster': 200, 
    'Inkbrush': 1100, 
    'Octobrush': 1110, 
    'Gootuber': 2060, 
    'Bamboozler': 2050, 
    'E-Liter Scope': 2040, 
    'E-Liter': 2030, 
    'Splatterscope': 2020, 
    'Charger': 2010, 
    'Squiffer': 2000, 
    'Dualies Squelshers': 5030, 
    'Glooga Dualies': 5020, 
    'Dualies': 5010, 
    'Dapple Dualies': 5000, 
    'Tetra Dualies': 5040, 
    'Carbon Roller': 1000, 
    'Dynamo Roller': 1020, 
    'Flingza Roller': 1030, 
    'Roller': 1010, 
    'Splatana': 8010, 
    'Heavy Splatana': 8000, 
    'Undercover Brella': 6020, 
    'Brella': 6000, 
    'Tenta Brella': 6010, 
    'Aerospray': 30, 
    'Splattershot Pro': 70, 
    'Splattershot Jr': 10, 
    'Squeezer': 400, 
    '.52 Gal': 50, 
    '.96 Gal': 80, 
    'Jet Squelsher': 90, 
    'Splattershot': 40, 
    'Splash-o-matic': 20, 
    'Nzap': 60, 
    'Sploosh-o-matic': 0, 
    'H-3 Nozzlenose': 310, 
    'L-3 Nozzlenose': 300, 
    'Bloblober': 3030, 
    'Tri Slosher': 3010, 
    'Sloshing Machine': 3020, 
    'Slosher': 3000, 
    'Explosher': 3040, 
    'Ballpoint Splatling': 4030, 
    'Hydra Splatling': 4020, 
    'Mini Splatling': 4000, 
    'Nautilus': 4040, 
    'Heavy Splatling': 4010, 
    'Stringer': 7010
    }

        

def lisible(dico_weapon):
    if dico_weapon["DefaultHitEffectorType"] == "Maneuver":
        weapon_type = "Dualies"
    elif dico_weapon["DefaultHitEffectorType"] == "Spinner":
        weapon_type = "Splatling"
    elif dico_weapon["DefaultHitEffectorType"] == "Shelter":
        weapon_type = "Brella"
    else:
        weapon_type = dico_weapon["DefaultHitEffectorType"]
    weapon_id = dico_weapon["Id"]
    weapon_name = dico_id_armes[weapon_id]
    weapon_range = dico_weapon["Range"]
    weapon_price = dico_weapon["ShopPrice"]
    unlock_rank = dico_weapon["ShopUnlockRank"]
    weapon_spe_pts = dico_weapon["SpecialPoint"]
    weapon_image = "images_armes/" + dico_id_armes[weapon_id] + ".png"
    special_weapon = dico_weapon["SpecialWeapon"].replace("Work/Gyml/", "").replace(".spl__WeaponInfoSpecial.gyml", "")
    sub_weapon = dico_weapon["SubWeapon"].replace("Work/Gyml/", "").replace(".spl__WeaponInfoSub.gyml", "")

    return weapon_name, weapon_type, weapon_price, unlock_rank, weapon_range, weapon_spe_pts, sub_weapon, special_weapon, weapon_image


def get_info(weapon_id):
    if type(weapon_id) != int:
        weapon_id = dico_armes_id[weapon_id]
    get_all_weapons_info()
    info_lisible = lisible(dico[weapon_id])
    return info_lisible
