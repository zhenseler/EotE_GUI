
import tkinter as tk
from tkinter import ttk
import Player_class


PC_dict = {}



        self.win = tk.Tk()

        # Add title
        self.win.title("EotE GM Assistant")


        # Add widgets
        self.create_widgets()



    def create_widgets(self):
        # Tabs
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "PC Roster")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Party Manager")
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text = "Encounter Manager")
        tabControl.pack(expand=1, fill="both")

        # LabelFrame within "Add New Player" tab
        creation_frame = ttk.LabelFrame(tab1, text = "Select a PC, or create a new one")
        creation_frame.grid(column = 0, row = 0, padx = 8, pady = 4)


        # New PC button
        self.creation_submit_button = ttk.Button(creation_frame, text = "New PC", command = self.new_pc())
        self.creation_submit_button.grid(column = 0, row = 0)


        # PC selector combobox
        self.PC_selection = tk.StringVar()
        self.PC_selection_combobox = ttk.Combobox(creation_frame, width = 12, textvariable = self.PC_selection)
        self.PC_selection_combobox['values'] = ("Chris","Emmie")
        self.PC_selection_combobox.grid(column = 0, row = 1)


        # New PC pop-up
    def new_pc(self):
        self.creation_popup = tk.Toplevel(self.creation_frame)



gui_instance = GUI()
gui_instance.win.mainloop()