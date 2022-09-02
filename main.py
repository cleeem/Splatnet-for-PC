import customtkinter
import os
import tkinter 
from PIL import Image, ImageTk

import data_weapons 
import test_schedule

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):

    APP_NAME = "Splatnet PC"
    WIDTH = 1080
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(1080, 720)
        self.maxsize(1920, 1080)
        
        self.resizable(True, True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.list_frame = []

        self.liste_weapons_id = []
        self.liste_weapons_name = []
        dico = sorted(data_weapons.dico_id_armes)
        for id in dico:
            self.liste_weapons_id.append(int(id))
            self.liste_weapons_name.append(data_weapons.dico_id_armes[int(id)])
        self.font_size = (self.current_height + self.current_width)//95
        self.creation()

        
        
    def creation(self):

        self.frame_icon = customtkinter.CTkFrame(master=self, width=self.current_width * 0.23, height=self.current_height*0.94, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_icon.place(relx=0.125, rely=0.5, anchor=tkinter.CENTER)

        self.button_width = self.frame_icon._current_width * 0.9
        self.button_height = self.frame_icon._current_height * 0.15

        self.button_home = customtkinter.CTkButton(master=self.frame_icon, text="home", text_font=("Roboto Medium", self.font_size), command=self.home, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_home.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


        self.button_stats = customtkinter.CTkButton(master=self.frame_icon, text="stats", text_font=("Roboto Medium", self.font_size), command=self.stats, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_stats.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.optionmenu_1 = customtkinter.CTkComboBox(master=self.frame_icon, 
                                                    values=["regular", "gachi", "league"], 
                                                    command=self.test, width=self.button_width, height=self.button_height,
                                                    text_font=("Roboto Medium", self.font_size), dropdown_text_font=("Roboto Medium", self.font_size), button_color="gray")
        self.optionmenu_1.set("maps")
        self.optionmenu_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button_rotations = customtkinter.CTkButton(master=self.frame_icon, text="weapon ndata\n(SP3 Vanilla kit only)", text_font=("Roboto Medium", self.font_size), command=self.weapons_data, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_rotations.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.button_splatnet = customtkinter.CTkButton(master=self.frame_icon, text="splatnet", text_font=("Roboto Medium", self.font_size), command=self.splatnet, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_splatnet.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        self.crea_frame_data()
        
    def crea_frame_data(self):
        try:
            self.frame_data.destroy()
            self.button_refresh.destroy()
        except:
            pass
        
        self.frame_data = customtkinter.CTkFrame(master=self, width=self.current_width * 0.70, height=self.current_height*0.94, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_data.place(relx=0.625, rely=0.5, anchor=tkinter.CENTER)

        self.button_refresh = customtkinter.CTkButton(master=self.frame_data, text="resize", text_font=("Roboto Medium", self.font_size//2), command=self.refresh_scale, corner_radius=6, width=self.frame_data._current_height*0.05, height=15)
        self.button_refresh.place(relx=0.038, rely=0.5, anchor=tkinter.CENTER)
        
    def update_info(self, bouton):
        if bouton == "stats":
            self.stats()
        elif bouton == "maps":
            self.maps()

    def refresh_scale(self):
        self.font_size = (self.current_height + self.current_width)//95
        self.frame_icon.destroy()
        self.frame_data.destroy()
        self.creation()
        self.home()

    def test(self ,arg):
        self.maps(arg=arg)

    def home(self):
        self.crea_frame_data()

    def stats(self):
        self.crea_frame_data()

    def get_maps(self, test : test_schedule.Rotation):
        img_width = int((self.frame_data._current_width*0.85)*0.25)
        img_height = int((self.frame_data._current_width*0.8)*0.141)
        current_map_a = Image.open("maps_splatoon/200px-S2_Stage_" + test.current_stage_a.replace(" ", "_") + ".png").resize((img_width, img_height))
        self.current_map_a = ImageTk.PhotoImage(current_map_a)

        current_map_b = Image.open("maps_splatoon/200px-S2_Stage_" + test.current_stage_b.replace(" ", "_") + ".png").resize((img_width, img_height))
        self.current_map_b = ImageTk.PhotoImage(current_map_b)            

        next_map_a = Image.open("maps_splatoon/200px-S2_Stage_" + test.next_stage_a.replace(" ", "_") + ".png").resize((img_width, img_height))
        self.next_map_a = ImageTk.PhotoImage(next_map_a)   

        next_map_b = Image.open("maps_splatoon/200px-S2_Stage_" + test.next_stage_b.replace(" ", "_") + ".png").resize((img_width, img_height))
        self.next_map_b = ImageTk.PhotoImage(next_map_b)

    def maps(self, arg):
        self.crea_frame_data()

        if arg == "gachi":
            nom = "Ranked Battle"
            test = test_schedule.get_data(arg)
            self.get_maps(test=test)  

        elif arg == "league":
            nom = "League Battle"
            test = test_schedule.get_data(arg)
            self.get_maps(test=test)  

        elif arg == "regular":
            nom = "Turf War Battle"
            test = test_schedule.get_data(arg)
            self.get_maps(test=test)  

        else:
            nom = ""
            test = ""

        frame_name = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width*0.85, height=self.frame_data._current_height*0.1, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_name.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        frame_map = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width*0.85, height=self.frame_data._current_height*0.8, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_map.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)

        label_turf = customtkinter.CTkLabel(master=frame_name, text=f"Battle Type : {nom}",text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_turf.place(relx=0.5, rely=0.5,  anchor = tkinter.CENTER)
        
        label_info = customtkinter.CTkLabel(master=frame_map, text=test ,text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_info.place(relx=0.2, rely=0.5,  anchor = tkinter.CENTER)
        
        try:
            image_current_map_a = tkinter.Label(master=frame_map, image=self.current_map_a, border=0)
            image_current_map_a.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

            image_current_map_b = tkinter.Label(master=frame_map, image=self.current_map_b, border=0)
            image_current_map_b.place(relx=0.825, rely=0.2, anchor=tkinter.CENTER)

            image_next_map_a = tkinter.Label(master=frame_map, image=self.next_map_a, border=0)
            image_next_map_a.place(relx=0.5, rely=0.775, anchor=tkinter.CENTER)

            image_next_map_b = tkinter.Label(master=frame_map, image=self.next_map_b, border=0)
            image_next_map_b.place(relx=0.825, rely=0.775, anchor=tkinter.CENTER)           

        except:
            pass
        
    def weapons_data(self):
        self.crea_frame_data()

        self.optionmenu_armes = customtkinter.CTkOptionMenu(master=self.frame_data, 
                                                    values=self.liste_weapons_name, 
                                                    command=self.weapons, width=200, height=75,
                                                    text_font=("Roboto Medium", self.font_size), dropdown_text_font=("Roboto Medium", self.font_size), button_color="gray")
        self.optionmenu_armes.place(relx=0.2, rely=0.1, anchor=tkinter.CENTER)
            
        frame_name = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width*0.55, height=self.frame_data._current_height*0.1, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_name.place(relx=0.7, rely=0.1, anchor=tkinter.CENTER)
        
        frame_info = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width*0.85, height=self.frame_data._current_height*0.8, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_info.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)

    def weapons(self, weapon):
        try:
            frame_name.destroy()
            frame_info.destroy()
        except:
            pass

        weapon_infos = data_weapons.get_info(weapon_id=weapon)

        frame_name = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width*0.55, height=self.frame_data._current_height*0.1, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_name.place(relx=0.7, rely=0.1, anchor=tkinter.CENTER)
        
        frame_info = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width*0.85, height=self.frame_data._current_height*0.8, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_info.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)

        label_name = customtkinter.CTkLabel(master=frame_name, text=f"Infos : {weapon_infos[0]}",text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_name.place(relx=0.5, rely=0.5,  anchor = tkinter.CENTER)

        res = f"Weapon Type : {weapon_infos[1]} \n\nWeapon Price : {weapon_infos[2]} \n\nUnlock Rank : {weapon_infos[3]} \n\nRange : {weapon_infos[4]} \n\nPoints for Special : {weapon_infos[5]} \n\n Sub Weapon : {weapon_infos[6]} \n\nSpecial Weapon : {weapon_infos[7]} "

        label_info = customtkinter.CTkLabel(master=frame_info, text=res,text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_info.place(relx=0.3, rely=0.5,  anchor = tkinter.CENTER)

        img_width = int((self.frame_data._current_width*0.8)*0.25)
        img_height = int((self.frame_data._current_width*0.8)*0.25)

        weapon_image = Image.open(weapon_infos[8]).resize((img_width, img_height))
        self.weapon_image = ImageTk.PhotoImage(weapon_image)

        label_image = tkinter.Label(master=frame_info, image=self.weapon_image, border=0, background=("gray20"))
        label_image.place(relx=0.825, rely=0.775, anchor=tkinter.CENTER)  

    def splatnet(self):
        test = test_schedule.get_stuff(1)
        print(test)


    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()



if __name__ == "__main__":
    app = App()
    app.start()
