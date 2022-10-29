import tkinter
import datetime
from tkcalendar import *
import customtkinter
import Orchestrator

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("MyWeek.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ===========

        # configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame_bottom = customtkinter.CTkFrame(master=self)
        self.frame_bottom.grid(row=1, column=0, sticky="nswe", padx=20, pady=20)

        self.frame_top = customtkinter.CTkFrame(master=self)
        self.frame_top.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        # ============ frame_top ============

        # configure grid layout (3x7)
        self.frame_top.rowconfigure((0, 1), weight=1)
        self.frame_top.rowconfigure(1, weight=10)
        self.frame_top.columnconfigure((0, 1, 2), weight=1)
        self.frame_top.columnconfigure(3, weight=0)

        # ============ frame_top ============

        self.label_mode_1 = customtkinter.CTkLabel(master=self.frame_top, text="Input folder:")
        self.label_mode_1.grid(row=0, column=0, pady=0, padx=20, sticky="w")

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_top,
                                            placeholder_text="No folder selected...")
        self.entry_1.grid(row=0, column=1, columnspan=2, pady=20, padx=20, sticky="we")



        self.label_mode_2 = customtkinter.CTkLabel(master=self.frame_top, text="Input filename:")
        self.label_mode_2.grid(row=1, column=0, pady=0, padx=20, sticky="w")

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_top,
                                            width=120,
                                            placeholder_text="No filename selected...")
        self.entry_2.grid(row=1, column=1, columnspan=2, pady=20, padx=20, sticky="we")


        self.label_mode_3 = customtkinter.CTkLabel(master=self.frame_top, text="Output folder:")
        self.label_mode_3.grid(row=2, column=0, pady=0, padx=20, sticky="w")

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_top,
                                            width=120,
                                            placeholder_text="No folder selected...")
        self.entry_3.grid(row=2, column=1, columnspan=2, pady=20, padx=20, sticky="we")


        self.label_mode_4 = customtkinter.CTkLabel(master=self.frame_top, text="Output filename:")
        self.label_mode_4.grid(row=3, column=0, pady=0, padx=20, sticky="w")

        self.entry_4 = customtkinter.CTkEntry(master=self.frame_top,
                                            width=120,
                                            placeholder_text="No filename selected...")
        self.entry_4.grid(row=3, column=1, columnspan=2, pady=20, padx=20, sticky="we")


        self.label_mode_5 = customtkinter.CTkLabel(master=self.frame_top, text="Date:")
        self.label_mode_5.grid(row=4, column=0, pady=0, padx=20, sticky="w")

        self.label_5 = customtkinter.CTkLabel(master=self.frame_top,
                                                   text="No date selected...",
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_5.grid(row=4, column=1, sticky="nwe", padx=15, pady=15)

        self.date = customtkinter.CTkButton(master=self.frame_top,command=self.create_date_selection_window,text="Select date",fg_color=("#b2b4b8"),width=160,height=32,border_width=0,corner_radius=8)
        self.date.grid(row=4,column=2,pady=10)

        # ============ frame_bottom ============

        # configure grid layout (3x7)
        self.frame_bottom.rowconfigure((0, 1), weight=1)
        self.frame_bottom.rowconfigure(1, weight=10)
        self.frame_bottom.columnconfigure((0, 1), weight=1)
        self.frame_bottom.columnconfigure(2, weight=0)

        # ============ frame_bottom ============

        self.button_5 = customtkinter.CTkButton(master=self.frame_bottom,
                                                text="Calculate",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.calculate_event)
        self.button_5.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")


        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_bottom,
                                                   text="Output will be printed here..." ,
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=1, row=0, sticky="nwe", padx=15, pady=15)


        # set default values
        self.entry_1.insert(-1, "InputFiles")
        self.entry_2.insert(-1, "MyWeek.xlsx")
        self.entry_3.insert(-1, "OutputFiles")
        self.entry_4.insert(-1, "Output.xlsx")


    def calculate_event(self):
        inputFolder = self.entry_1.get()
        inputFileName = self.entry_2.get()
        outputFolder = self.entry_3.get()
        outfupFileName= self.entry_4.get()
        date = self.label_5.text_label.cget("text")
        calcResult = Orchestrator.InitiateCalculation(inputFolder, inputFileName, outputFolder, outfupFileName, date)

        self.label_info_1.configure(text=calcResult, justify=tkinter.LEFT)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def on_closing(self, event=0):
        self.destroy()


    ''' Çreates a window in which the user is allowed to select a date for the calculation'''
    def create_date_selection_window(self):
        WIDTH = 260
        HEIGHT = 200

        date_selection_window = customtkinter.CTk()
        date_selection_window.geometry(f"{WIDTH}x{HEIGHT}")
        cal = Calendar(date_selection_window, selectmode="day", year=int(datetime.date.today().year), month=int(datetime.date.today().month), day=int(datetime.date.today().day))
        cal.pack()
        tkinter.Button(date_selection_window, text="Select date", command= lambda: self.insert_selected_date(cal, date_selection_window)).pack()
        date_selection_window.mainloop()

    ''''Helper method for create_date_selection_window that inserts the selected date'''
    def insert_selected_date(self, cal, date_selection_window):
        date_selection_window.destroy()
        self.label_5.configure(text=cal.get_date())


if __name__ == "__main__":
    app = App()
    app.mainloop()