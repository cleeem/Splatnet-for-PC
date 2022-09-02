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
        
        # self.resizable(True, True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.list_frame = []

        self.creation()

        
    def creation(self):
        for elt in self.list_frame:
            elt.destroy()

        self.frame_data = customtkinter.CTkFrame(master=self, width=800, height=680, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_data.place(relx=0.625, rely=0.5, anchor=tkinter.CENTER)

        self.list_frame.append(self.frame_data)

        self.frame_icon = customtkinter.CTkFrame(master=self, width=250, height=680, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_icon.place(relx=0.125, rely=0.5, anchor=tkinter.CENTER)

        self.button_home = customtkinter.CTkButton(master=self.frame_icon, text="home", text_font=("Roboto Medium", -30), command=self.home, corner_radius=6, width=200, height=100)
        self.button_home.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


        self.button_stats = customtkinter.CTkButton(master=self.frame_icon, text="stats", text_font=("Roboto Medium", -30), command=self.stats, corner_radius=6, width=200, height=100)
        self.button_stats.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.optionmenu_1 = customtkinter.CTkComboBox(master=self.frame_icon, 
                                                    values=["regular", "gachi", "league"], 
                                                    command=self.maps, width=200, height=75,
                                                    text_font=("Roboto Medium", -30), dropdown_text_font=("Roboto Medium", -30), button_color="gray")
        self.optionmenu_1.set("maps")
        self.optionmenu_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button_rotations = customtkinter.CTkButton(master=self.frame_icon, text="weapons\ndata", text_font=("Roboto Medium", -30), command=self.weapons_data, corner_radius=6, width=200, height=100)
        self.button_rotations.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.button_splatnet = customtkinter.CTkButton(master=self.frame_icon, text="splatnet", text_font=("Roboto Medium", -30), command=self.splatnet, corner_radius=6, width=200, height=100)
        self.button_splatnet.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


    def get_maps(self, test : test_schedule.Rotation):
        current_map_a = Image.open("maps_splatoon/200px-S2_Stage_" + test.current_stage_a.replace(" ", "_") + ".png").resize((200, 100))
        self.current_map_a = ImageTk.PhotoImage(current_map_a)

        current_map_b = Image.open("maps_splatoon/200px-S2_Stage_" + test.current_stage_b.replace(" ", "_") + ".png").resize((200, 100))
        self.current_map_b = ImageTk.PhotoImage(current_map_b)            

        next_map_a = Image.open("maps_splatoon/200px-S2_Stage_" + test.next_stage_a.replace(" ", "_") + ".png").resize((200, 100))
        self.next_map_a = ImageTk.PhotoImage(next_map_a)   

        next_map_b = Image.open("maps_splatoon/200px-S2_Stage_" + test.next_stage_b.replace(" ", "_") + ".png").resize((200, 100))
        self.next_map_b = ImageTk.PhotoImage(next_map_b)

    def home(self):
        for elt in self.list_frame:
            elt.destroy()
        self.frame_data = customtkinter.CTkFrame(master=self, width=800, height=680, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_data.place(relx=0.625, rely=0.5, anchor=tkinter.CENTER)
        self.list_frame.append(self.frame_data)
        print("home")

    def stats(self):
        for elt in self.list_frame:
            elt.destroy()
        self.frame_data = customtkinter.CTkFrame(master=self, width=800, height=680, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_data.place(relx=0.625, rely=0.5, anchor=tkinter.CENTER)
        self.list_frame.append(self.frame_data)
        print("oui")

    def maps(self, arg):
        try:
            frame_map.destroy()
            frame_name.destroy()
        except:
            pass

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

        frame_name = customtkinter.CTkFrame(master=self.frame_data, width=680, height=50, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_name.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.list_frame.append(frame_name)

        frame_map = customtkinter.CTkFrame(master=self.frame_data, width=680, height=550, corner_radius=15, fg_color=("gray70", "gray20"))
        frame_map.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)
        self.list_frame.append(frame_map)

        font_size = -22  

        label_turf = customtkinter.CTkLabel(master=frame_name, text=f"Battle Type : {nom}",text_font=("Roboto Medium", -30), text_color="white")  # font name and size in px
        label_turf.place(relx=0.5, rely=0.5,  anchor = tkinter.CENTER)

        label_info = customtkinter.CTkLabel(master=frame_map, text=test ,text_font=("Roboto Medium", font_size), text_color="white")  # font name and size in px
        label_info.place(relx=0.5, rely=0.5,  anchor = tkinter.CENTER)
        
        try:
            image_current_map_a = tkinter.Label(master=frame_map, image=self.current_map_a)
            image_current_map_a.place(relx=0.175, rely=0.2, anchor=tkinter.CENTER)

            image_current_map_b = tkinter.Label(master=frame_map, image=self.current_map_b)
            image_current_map_b.place(relx=0.825, rely=0.2, anchor=tkinter.CENTER)

            image_next_map_a = tkinter.Label(master=frame_map, image=self.next_map_a)
            image_next_map_a.place(relx=0.175, rely=0.75, anchor=tkinter.CENTER)

            image_next_map_b = tkinter.Label(master=frame_map, image=self.next_map_b)
            image_next_map_b.place(relx=0.825, rely=0.75, anchor=tkinter.CENTER)           

        except:
            pass
        
    def weapons_data(self):
        for elt in self.list_frame:
            elt.destroy()
        self.frame_data = customtkinter.CTkFrame(master=self, width=800, height=680, corner_radius=15, fg_color=("gray70", "gray25"))
        self.frame_data.place(relx=0.625, rely=0.5, anchor=tkinter.CENTER)
        self.list_frame.append(self.frame_data)
        test = data_weapons.get_info(2030)
        print(test)

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
