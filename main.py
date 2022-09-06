from genericpath import exists
import webbrowser
import customtkinter
import os
import tkinter 
import json
from PIL import Image, ImageTk
import requests

import dbs
import game as splatnet

import test_schedule

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


PATH = os.path.dirname(os.path.realpath(__file__))


class Widget(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Widget")
        self.geometry(f"300 x 100")
        self.minsize(300, 100)
        self.maxsize(300, 100)

        self.current_power = 0
        self.power_variation = 0
        self.power_variation_color = "white"

        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.kda = 0

        self.wins = 0
        self.looses = 0
        self.win_percent = 0

        self.rule = ""

        self.get_data_widget()
        self.render_data()
        
    def get_data_widget(self):
        partie = splatnet.Game()
        data = partie.get_data()
    
        if data["mode"] == "gachi":
            self.rule = dbs.rules_short[data["rule"]]

            self.kills = data["kill_or_assist"]
            self.assists = data["kill_or_assist"] - data["kill"]
            self.deaths = data["death"]
            self.kda = round(data["kill"] / self.deaths, 4)

            if data["x_power_after"] != None:
                if self.wins > 0 or self.looses > 0:
                    self.power_variation = round(float(data["x_power_after"]) - float(self.current_power), 4)
                    if self.power_variation>0:
                        self.power_variation_color = "green"
                    elif self.power_variation<0:
                        self.power_variation_color = "red"
                    else:
                        self.power_variation_color = "white"
                
                self.current_power = data["x_power_after"]
            else:
                self.power_variation = "0.0"
                self.current_power = "calculating" 

            if data["result"] == "win":
                self.wins += 1
            else:
                self.looses += 1

            if self.wins == 0:
                self.win_percent = "0"
            elif self.looses == 0:
                self.win_percent == "100"
            elif self.wins == self.looses:
                self.win_percent = "50"
            else:
                self.win_percent = f"{(float(self.looses)/float(self.wins))*100}"

    def render_data(self):
        
        self.frame_data = customtkinter.CTkFrame(master=self, width=self.current_width, height=self.current_height)
        self.frame_data.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button_refresh= customtkinter.CTkButton(master=self.frame_data, text="🔁", text_font=("Roboto Medium", 10), command=self.refresh, corner_radius=15, width=10, height=15)
        self.button_refresh.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)

        label_info_power_variation = customtkinter.CTkLabel(master=self.frame_data, text=self.power_variation ,text_font=("Roboto Medium", 17),justify=tkinter.LEFT , text_color=self.power_variation_color)  # font name and size in px
        label_info_power_variation.place(relx=0.15, rely=0.8, anchor=tkinter.CENTER)

        label_info_power = customtkinter.CTkLabel(self.frame_data, text=self.current_power, width=75 ,text_font=("Roboto Medium", 13),justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_power.place(relx=0.15, rely=0.25, anchor=tkinter.CENTER)

        label_info_rule = customtkinter.CTkLabel(self.frame_data, text=self.rule, width=75 ,text_font=("Roboto Medium", 7),justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_rule.place(relx=0.15, rely=0.5, anchor=tkinter.CENTER)

        label_info_wins = customtkinter.CTkLabel(self.frame_data, text=f"Wins {self.wins}", width=75 ,text_font=("Roboto Medium", 10),justify=tkinter.LEFT , text_color="red")  # font name and size in px
        label_info_wins.place(relx=0.425, rely=0.25, anchor=tkinter.CENTER)

        label_info_loose = customtkinter.CTkLabel(self.frame_data, text=f"Lose {self.looses}", width=75 ,text_font=("Roboto Medium", 10),justify=tkinter.LEFT , text_color="green")  # font name and size in px
        label_info_loose.place(relx=0.625, rely=0.25, anchor=tkinter.CENTER)

        label_info_percent = customtkinter.CTkLabel(self.frame_data, text=str(self.win_percent) + "%", width=50,text_font=("Roboto Medium", 10),justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_percent.place(relx=0.9, rely=0.25, anchor=tkinter.CENTER)

        res = f"{self.kills}({self.assists})k  {self.deaths}d  {self.kda}k/d"

        label_info_kda = customtkinter.CTkLabel(self.frame_data, text=res, text_font=("Roboto Medium", 12),justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_kda.place(relx=0.55, rely=0.7, anchor=tkinter.CENTER)
    
    def refresh(self):
        self.frame_data.destroy()
        self.get_data_widget()
        self.render_data()

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

        self.font_size = (self.current_height + self.current_width)//110
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.dl_maps()

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
        
        img_width = int((frame._current_width)-20)
        img_height = int((frame._current_height)-20)

        if img_width/img_height>1.3:
            while img_width/img_height>1.3:
                img_height += 1
        try:
            image_home = Image.open("image_home.png").resize((img_width, img_height))
            self.image_home = ImageTk.PhotoImage(image_home)
        except:
            self.create_img_home()

    def open_git_app(self):
        webbrowser.open(url="https://github.com/cleeem/Splatnet-for-PC")

    def open_git_s2s(self):
        webbrowser.open(url="https://github.com/frozenpandaman/splatnet2statink")

    def home(self):
        self.crea_frame_data()
        
        hauteur = self.frame_data._current_height * 0.3
        largeur = self.frame_data._current_width * 0.5
        frame_1 = customtkinter.CTkFrame(master=self.frame_data, width=largeur, height = hauteur, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_1.place(relx=0.3, rely=0.175, anchor=tkinter.CENTER)

        res_1 = self.get_res(test_schedule.get_stuff(0))

        liste = [test_schedule.get_stuff(0).gear_url]
        self.dl_shop_images(liste=liste)

        label_info_1 = customtkinter.CTkLabel(master=frame_1, text=res_1 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=150 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_1.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

        label_info_1_image = customtkinter.CTkLabel(master=frame_1, image=self.gear_1 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_1_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

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

        self.button_github_app = customtkinter.CTkButton(master=self.frame_data, text="See the app\nOn github", text_font=("Roboto Medium", int(self.font_size*1.5)), command=self.open_git_app, corner_radius=6, width=self.frame_data._current_width*0.3, height=self.frame_data._current_height*0.3)
        self.button_github_app.place(relx=0.8, rely=0.35, anchor=tkinter.CENTER)

        self.button_github_s2s = customtkinter.CTkButton(master=self.frame_data, text="See \nsplatnet2statink\nOn github", text_font=("Roboto Medium", int(self.font_size*1.5)), command=self.open_git_s2s, corner_radius=6, width=self.frame_data._current_width*0.3, height=self.frame_data._current_height*0.3)
        self.button_github_s2s.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

    def create_img_result(self, indice):
        temp = splatnet.Game()
        temp.get_image_game(indice)

    def get_img_results(self,arg):
        img_width = int((self.frame_2._current_width)-20)
        img_height = int((self.frame_2._current_height)-20)

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

        self.label_info_loading.destroy()

    def stats(self):
        self.crea_frame_data()

        liste = [str(i) for i in range(1,51)]

        self.frame = customtkinter.CTkFrame(master=self.frame_data, width=self.frame_data._current_width * 0.9, height=100, corner_radius=15, fg_color=("gray70", "gray20"))
        self.frame.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)

        self.optionmenu_stats = customtkinter.CTkComboBox(master=self.frame, 
                                                    values=liste, 
                                                    command=self.get_img_results, width=int(self.frame._current_width*0.4), height=50,
                                                    text_font=("Roboto Medium", self.font_size), dropdown_text_font=("Roboto Medium", self.font_size), button_color="gray")
        self.optionmenu_stats.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
        
        label_info = customtkinter.CTkLabel(master=self.frame, text=f"Match you want to see \n(recent to old)",text_font=("Roboto Medium", self.font_size), text_color="white")  # font name and size in px
        label_info.place(relx=0.2, rely=0.5,  anchor = tkinter.CENTER)

        frame_width = int(self.frame_data._current_width * 0.9)
        frame_height = int(self.frame_data._current_height * 0.7,)

        if frame_width/frame_height>1.65:
            while frame_width/frame_height>1.65:
                frame_height += 5
        else:
            while frame_width/frame_height<1.65:
                frame_height -= 5

        self.frame_2 = customtkinter.CTkFrame(master=self.frame_data,  width=frame_width + 30, height=frame_height + 30, corner_radius=15, fg_color=("gray70", "gray20"))
        self.frame_2.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)

        self.label_info_loading = customtkinter.CTkLabel(master=self.frame_2, text="Loading data from match \nmight take some time" ,text_font=("Roboto Medium", 40),justify=tkinter.LEFT , text_color="white")  # font name and size in px
        self.label_info_loading.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def get_res(self, test_splat):
        res = f"Brand : {test_splat.brand} \nName : {test_splat.name_stuff} \nFrequent Bonus : {test_splat.frequent_bonus}  \n\nNew Price : {test_splat.new_price}  |  Old Price : {test_splat.old_price}   \n\nNew Main : {test_splat.new_main}  \nOld Main : {test_splat.old_main} \n\nEnd Time : {test_splat.end_time} "
        return res

    def dl_shop_images(self, liste):
                
        for i,url in enumerate(liste):
            url_save = f"image_shop_{i+1}.png"
            response = requests.get(url)
            if response.status_code:
                fp = open(url_save, 'wb')
                fp.write(response.content)
                fp.close()

        img_width = 100
        img_height = 100

        gear_1 = Image.open("image_shop_1.png").resize((img_width, img_height))
        self.gear_1 = ImageTk.PhotoImage(gear_1)

        try:
            gear_2 = Image.open(f"image_shop_2.png").resize((img_width, img_height))
            self.gear_2 = ImageTk.PhotoImage(gear_2)

            gear_3 = Image.open(f"image_shop_3.png").resize((img_width, img_height))
            self.gear_3 = ImageTk.PhotoImage(gear_3)

            gear_4 = Image.open(f"image_shop_4.png").resize((img_width, img_height))
            self.gear_4 = ImageTk.PhotoImage(gear_4)

            gear_5 = Image.open(f"image_shop_5.png").resize((img_width, img_height))
            self.gear_5 = ImageTk.PhotoImage(gear_5)

            gear_6 = Image.open(f"image_shop_6.png").resize((img_width, img_height))
            self.gear_6 = ImageTk.PhotoImage(gear_6)
        except:
            pass

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
        liste_url = []
        for i in range(6):
            temp = test_schedule.get_stuff(i)
            res = f"Brand : {temp.brand}  \nFrequent Bonus : {temp.frequent_bonus}  \n\nNew Price : {temp.new_price}  |  Old Price : {temp.old_price}   \n\nNew Main : {temp.new_main}  \nOld Main : {temp.old_main} \n\n End Time : {temp.end_time}  "
            liste_res.append(res)
            liste_url.append(temp.gear_url)

        self.dl_shop_images(liste_url)

        label_info_1_image = customtkinter.CTkLabel(master=frame_1, image=self.gear_1 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_1_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)
        
        label_info_2_image = customtkinter.CTkLabel(master=frame_2, image=self.gear_2 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_2_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

        label_info_3_image = customtkinter.CTkLabel(master=frame_3, image=self.gear_3 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_3_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

        label_info_4_image = customtkinter.CTkLabel(master=frame_4, image=self.gear_4 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_4_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

        label_info_5_image = customtkinter.CTkLabel(master=frame_5, image=self.gear_5 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100 ,justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_5_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

        label_info_6_image = customtkinter.CTkLabel(master=frame_6, image=self.gear_6 ,text_font=("Roboto Medium", int(self.font_size//1.6)), height=100, justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_6_image.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

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
        self.crea_frame_data()

        label_info_1 = customtkinter.CTkLabel(master=self.frame_data, text="Loading widget \nit might take some time" ,text_font=("Roboto Medium", 40),justify=tkinter.LEFT , text_color="white")  # font name and size in px
        label_info_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        widget = Widget()
        label_info_1.destroy()
        self.home()
        widget.start()
        
    def dl_maps(self):
        liste_map = ["https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f7/S2_Stage_The_Reef.png/200px-S2_Stage_The_Reef.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/cd/S2_Stage_Musselforge_Fitness.png/200px-S2_Stage_Musselforge_Fitness.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/3/31/S2_Stage_Starfish_Mainstage.png/200px-S2_Stage_Starfish_Mainstage.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ed/S2_Stage_Humpback_Pump_Track.png/200px-S2_Stage_Humpback_Pump_Track.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/c9/S2_Stage_Inkblot_Art_Academy.png/200px-S2_Stage_Inkblot_Art_Academy.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/62/S2_Stage_Sturgeon_Shipyard.png/200px-S2_Stage_Sturgeon_Shipyard.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/7/7e/S2_Stage_Manta_Maria.png/200px-S2_Stage_Manta_Maria.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/3/37/S2_Stage_Moray_Towers.png/200px-S2_Stage_Moray_Towers.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f0/S2_Stage_Kelp_Dome.png/200px-S2_Stage_Kelp_Dome.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/9/91/S2_Stage_Snapper_Canal.png/200px-S2_Stage_Snapper_Canal.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/11/S2_Stage_Blackbelly_Skatepark.png/200px-S2_Stage_Blackbelly_Skatepark.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/6a/S2_Stage_Walleye_Warehouse.png/200px-S2_Stage_Walleye_Warehouse.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/6c/S2_Stage_Shellendorf_Institute.png/200px-S2_Stage_Shellendorf_Institute.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/4/49/S2_Stage_Port_Mackerel.png/200px-S2_Stage_Port_Mackerel.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/d4/S2_Stage_MakoMart.png/200px-S2_Stage_MakoMart.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f5/S2_Stage_Arowana_Mall.png/200px-S2_Stage_Arowana_Mall.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/d0/S2_Stage_Goby_Arena.png/200px-S2_Stage_Goby_Arena.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ef/S2_Stage_Camp_Triggerfish.png/200px-S2_Stage_Camp_Triggerfish.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/14/S2_Stage_Wahoo_World.png/200px-S2_Stage_Wahoo_World.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/da/S2_Stage_New_Albacore_Hotel.png/200px-S2_Stage_New_Albacore_Hotel.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/2/20/S2_Stage_Ancho-V_Games.png/200px-S2_Stage_Ancho-V_Games.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/10/S2_Stage_Skipper_Pavilion.png/200px-S2_Stage_Skipper_Pavilion.png"]
        self.dico_map = {}
        for i,url in enumerate(liste_map):
            url_save = f"image_{i+1}.png"
            self.dico_map[url[66:]] = url_save
            response = requests.get(url)
            if response.status_code:
                fp = open(url_save, 'wb')
                fp.write(response.content)
                fp.close()

    def get_maps(self, test : test_schedule.Rotation):
        img_width = int((self.frame_data._current_width*0.85)*0.3)
        img_height = int((self.frame_data._current_width*0.8)*0.16)

        url_a = ""
        url_b = ""
        url_a_next = ""
        url_b_next = ""
                
        uwu = test.next_stage_b.replace(" ","_")

        for k,v in self.dico_map.items():
            if test.current_stage_a.replace(" ","_") in k:
                url_a = v
            if test.current_stage_b.replace(" ","_") in k :
                url_b = v
            if test.next_stage_b.replace(" ","_") in k :
                url_a_next = v
            if uwu in k :
                url_b_next = v

        current_map_a = Image.open(url_a).resize((img_width, img_height))
        self.current_map_a = ImageTk.PhotoImage(current_map_a)

        current_map_b = Image.open(url_b).resize((img_width, img_height))
        self.current_map_b = ImageTk.PhotoImage(current_map_b)            

        next_map_a = Image.open(url_a_next).resize((img_width, img_height))
        self.next_map_a = ImageTk.PhotoImage(next_map_a)   

        next_map_b = Image.open(url_b_next).resize((img_width, img_height))
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



# pyinstaller --noconfirm --onefile --console --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/dbs.py;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/game.py;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/iksm.py;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/image_home.png;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/image_results.png;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/salmonrun.py;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/splatnet2statink.py;." --add-data "C:/Users/cleme/code/python/Splatnet-for-PC/test_schedule.py;." --add-data "c:\users\cleme\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter"  "C:/Users/cleme/code/python/Splatnet-for-PC/main.py"
