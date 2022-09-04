from genericpath import exists
import customtkinter
import os
import tkinter 
from PIL import Image, ImageTk
import webbrowser

import sys
sys.path.append("splatnet_infos/")
import game as splatnet

import data_weapons 
import test_schedule


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


PATH = os.path.dirname(os.path.realpath(__file__))
    

class Widget(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"500 x 400")
        

    
    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    
class App(customtkinter.CTk):

    APP_NAME = "Splatnet PC"
    WIDTH = 1080
    HEIGHT = 720
    font_size : int
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(1080, 720)
        self.maxsize(1920, 1080)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.liste_weapons_id = []
        self.liste_weapons_name = []
        dico = sorted(data_weapons.dico_id_armes)
        for id in dico:
            self.liste_weapons_id.append(int(id))
            self.liste_weapons_name.append(data_weapons.dico_id_armes[int(id)])
        self.font_size = (self.current_height + self.current_width)//110

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.creation()

    def creation(self):
        self.crea_frame_icon()
        self.crea_frame_data()
        self.home()

    def crea_frame_data(self):
        try:
            self.frame_data.destroy()
            
        except:
            pass
        
        self.frame_data = customtkinter.CTkFrame(master=self, width=self.current_width * 0.70, height=self.current_height*0.94, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_data.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
    def crea_frame_icon(self):
        self.frame_icon = customtkinter.CTkFrame(master=self, width=220, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_icon.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.button_width = self.frame_icon._current_width * 0.9
        self.button_height = self.frame_icon._current_height * 0.5

        self.custom_width = 100
        self.custom_height = 100

        self.button_home = customtkinter.CTkButton(master=self.frame_icon, text="home", text_font=("Roboto Medium", self.font_size), command=self.home, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_home.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.button_stats = customtkinter.CTkButton(master=self.frame_icon, text="stats", text_font=("Roboto Medium", self.font_size), command=self.stats, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_stats.place(relx=0.5, rely=0.26, anchor=tkinter.CENTER)

        self.button_splatnet = customtkinter.CTkButton(master=self.frame_icon, text="splatnet", text_font=("Roboto Medium", self.font_size), command=self.splatnet, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_splatnet.place(relx=0.5, rely=0.42, anchor=tkinter.CENTER)

        self.button_widget= customtkinter.CTkButton(master=self.frame_icon, text="Widget", text_font=("Roboto Medium", self.font_size), command=self.start_widget, corner_radius=6, width=self.button_width, height=self.button_height)
        self.button_widget.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

        self.optionmenu_1 = customtkinter.CTkComboBox(master=self.frame_icon, 
                                                    values=["regular", "gachi", "league"], 
                                                    command=self.test, width=self.button_width, height=self.button_height,
                                                    text_font=("Roboto Medium", self.font_size), dropdown_text_font=("Roboto Medium", self.font_size), button_color="gray")
        self.optionmenu_1.set("maps")
        self.optionmenu_1.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)

        self.button_rescale = customtkinter.CTkButton(master=self.frame_icon, text="resize", text_font=("Roboto Medium", self.font_size-5), command=self.resize, corner_radius=6, width=self.custom_width , height=self.custom_height)
        self.button_rescale.place(relx=0.25, rely=0.9, anchor=tkinter.CENTER)

        self.button_refresh= customtkinter.CTkButton(master=self.frame_icon, text="refresh\n(slow)", text_font=("Roboto Medium", self.font_size-5), command=self.refresh, corner_radius=6, width=self.custom_width, height=self.custom_height)
        self.button_refresh.place(relx=0.75, rely=0.9, anchor=tkinter.CENTER)
        
    def resize(self):
        self.font_size = (self.current_height + self.current_width)//115
        if self.font_size>20:
            self.font_size = 20
        self.frame_icon.destroy()
        self.frame_data.destroy()
        self.creation()
        self.home()

    def refresh(self):
        partie = splatnet.Game()
        partie.get_image_home()
        partie.get_image_game()

    def test(self ,arg):
        self.maps(arg=arg)

    def create_img_home(self):
        temp = splatnet.Game()
        temp.get_image_home()

    def get_img_home(self, frame):
        
        img_width = int((frame._current_width))
        img_height = int((frame._current_height))

        if img_width/img_height>1.3:
            while img_width/img_height>1.3:
                img_height += 10

        image_home = Image.open("image_home.png").resize((img_width, img_height))
        self.image_home = ImageTk.PhotoImage(image_home)

    def home(self):
        self.crea_frame_data()
        
        hauteur = self.frame_data._current_height * 0.3
        largeur = self.frame_data._current_width * 0.5
        frame_1 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_1.place(relx=0.3, rely=0.175, anchor=tkinter.CENTER)

        res_1 = self.get_res(test_schedule.get_stuff(0))

        label_info_1 = customtkinter.CTkLabel(master=frame_1, text=res_1 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=150 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_1.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

        width = self.frame_data._current_width * 0.5
        height = self.frame_data._current_height * 0.5

        if width/height>1.3:
            while width/height>1.3:
                height += 5
        else:
            while width/height<1.3:
                width += 5

        frame_2 = customtkinter.CTkFrame(master=self.frame_data, width=width, height=height, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_2.place(relx=0.3, rely=0.65, anchor=tkinter.CENTER)

        self.get_img_home(frame_2)

        label_info_2 = customtkinter.CTkLabel(master=frame_2, image=self.image_home ,text_font=("Roboto Medium", int(self.font_size//1.6)), text_color="white")  # font name and size in px
        label_info_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def create_img_result(self, indice):
        temp = splatnet.Game()
        temp.get_image_game(indice)

    def get_img_results(self,arg):
        img_width = int((self.frame_2._current_width))
        img_height = int((self.frame_2._current_height))

        if img_width/img_height>1.65:
            while img_width/img_height>1.65:
                img_height += 5
        else:
            while img_width/img_height<1.65:
                img_height -= 5

        self.create_img_result(indice=int(arg)-1)
        
        image_home = Image.open(f"image_results.png").resize((img_width, img_height))
        self.image_result = ImageTk.PhotoImage(image_home)

        label_image = customtkinter.CTkLabel(master=self.frame_2, image=self.image_result,text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_image.place(relx=0.5, rely=0.5,  anchor = tkinter.CENTER)

    def stats(self):
        self.crea_frame_data()

        liste = [str(i) for i in range(1,51)]

        self.frame = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width * 0.9, height=100, corner_radius=15, fg_color=("gray70", "gray20"))
        self.frame.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.optionmenu_stats = customtkinter.CTkComboBox(master=self.frame, 
                                                    values=liste, 
                                                    command=self.get_img_results, width=int(self.frame._current_width*0.4), height=50,
                                                    text_font=("Roboto Medium", self.font_size), dropdown_text_font=("Roboto Medium", self.font_size), button_color="gray")
        self.optionmenu_stats.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
        
        label_info = customtkinter.CTkLabel(master=self.frame, text=f"Match you want to see \n(recent to old)",text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_info.place(relx=0.2, rely=0.5,  anchor = tkinter.CENTER)

        self.frame_2 = customtkinter.CTkFrame(master=self.frame_data,  width=self.frame_data._current_width * 0.9, height=self.frame_data._current_height * 0.7, corner_radius=15, fg_color=("gray70", "gray20"))
        self.frame_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def get_res(self, test_splat):
        res = f"Brand : {test_splat.brand} \nName : {test_splat.name_stuff} \nFrequent Bonus : {test_splat.frequent_bonus}  \n\nNew Price : {test_splat.new_price}  |  Old Price : {test_splat.old_price}   \n\nNew Main : {test_splat.new_main}  \nOld Main : {test_splat.old_main} \n\nEnd Time : {test_splat.end_time} "
        return res

    def splatnet(self):
        self.crea_frame_data()
        hauteur = self.frame_data._current_height * 0.3
        largeur = self.current_width * 0.325
        frame_1 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_1.place(relx=0.25, rely=0.175, anchor=tkinter.CENTER)

        frame_2 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_2.place(relx=0.75, rely=0.175, anchor=tkinter.CENTER)

        frame_3 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_3.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

        frame_4 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_4.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

        frame_5 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_5.place(relx=0.25, rely=0.825, anchor=tkinter.CENTER)

        frame_6 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_6.place(relx=0.75, rely=0.825, anchor=tkinter.CENTER)

        liste_res = []
        for i in range(6):
            temp = test_schedule.get_stuff(i)
            res = f"Brand : {temp.brand}  \nFrequent Bonus : {temp.frequent_bonus}  \n\nNew Price : {temp.new_price}  |  Old Price : {temp.old_price}   \n\nNew Main : {temp.new_main}  \nOld Main : {temp.old_main} \n\n End Time : {temp.end_time}  "
            liste_res.append(res)


        label_info_1 = customtkinter.CTkLabel(master=frame_1, text=liste_res[0] ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=150 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_1.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

        label_info_2 = customtkinter.CTkLabel(master=frame_2, text=liste_res[1] ,text_font=("Roboto Medium", int(self.font_size//1.6)), justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_2.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

        label_info_3 = customtkinter.CTkLabel(master=frame_3, text=liste_res[2] ,text_font=("Roboto Medium", int(self.font_size//1.6)), justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_3.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

        label_info_4 = customtkinter.CTkLabel(master=frame_4, text=liste_res[3] ,text_font=("Roboto Medium", int(self.font_size//1.6)), justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_4.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

        label_info_5 = customtkinter.CTkLabel(master=frame_5, text=liste_res[4] ,text_font=("Roboto Medium", int(self.font_size//1.6)), justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_5.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

        label_info_6 = customtkinter.CTkLabel(master=frame_6, text=liste_res[5] ,text_font=("Roboto Medium", int(self.font_size//1.6)), justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_6.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

    def start_widget(self):
        widget = Widget()
        widget.start()
        

    def get_maps(self, test : test_schedule.Rotation):
        img_width = int((self.frame_data._current_width*0.85)*0.3)
        img_height = int((self.frame_data._current_width*0.8)*0.16)

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

        label_name = customtkinter.CTkLabel(master=frame_name, text=f"Battle Type : {nom}",text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_name.place(relx=0.5, rely=0.5,  anchor = tkinter.CENTER)
        
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
        
    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
