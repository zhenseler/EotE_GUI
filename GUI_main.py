# GUI imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import ImageTk, Image

# Built-in imports
import pickle
import os

# Self-made module imports
import Player_class
import Eote_manual
import Navigate_frames
import PC_creator


#======================================================================

#======================================================================


# PC names as keys, class object as values
if os.stat("Player_database.py").st_size != 0:
    PC_dict = pickle.load(open("Player_database.py","rb"))
else:
    PC_dict = {}




class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("EotE GM Assistant")

        # List of tuples for PC creation.  First member is field name, second is widget type
        self.creation_entry_fields = [("Character Name", "entry"),
                                      ("Player", "entry"),
                                      ("Species", "combobox", Eote_manual.species),
                                      ("Career", "combobox", Eote_manual.career),
                                      ("Specialization Tree", "combobox", Eote_manual.specialization_default)]

        # Add widgets
        self.create_widgets()



# ======================================================================
    # Functions
# ======================================================================



    # Displays PC's stats when selected in the Players tab combobox
    def display_PC(self, event):
        PC_name = event.widget.get()
        PC = PC_dict[PC_name]
        for i, field in enumerate(self.creation_entry_fields):

            col_pos = (i % 2) + 2  # Set column position
            row_pos = i // 2 # Set row position

            print(getattr(PC, field[0]))

            # Add label above widget to be added
            label = ttk.Label(self.creation_frame, text = getattr(PC, field[0])).grid(column = col_pos, row = row_pos, padx = 100, pady = 10)


    # Sets which PCs are displayed in Players tab combobox
    def set_PC_selector(self):
        self.PC_selection_combobox['values'] = [x for x in PC_dict.keys()]


    # Create PC_creator window on new_pc button click
    def pc_creator(self):
        self.pc_creator = PC_creator.PC_Creator(PC_dict)





#======================================================================
#   Draw all widgets on main menu
#======================================================================


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
        self.creation_frame = ttk.LabelFrame(tab1, text = "Select a PC, or create a new one")
        self.creation_frame.grid(column = 0, row = 0, padx = 8, pady = 4)


        # New PC button
        self.creation_submit_button = ttk.Button(self.creation_frame, text = "New PC", command = self.pc_creator)
        self.creation_submit_button.grid(column = 0, row = 0)




        # PC selector combobox
        self.PC_selection = tk.StringVar()
        self.PC_selection_combobox = ttk.Combobox(self.creation_frame, width = 10, textvariable = self.PC_selection)
        self.set_PC_selector()
        self.PC_selection_combobox.grid(column = 0, row = 1)
        self.PC_selection_combobox.bind("<<ComboboxSelected>>", self.display_PC)




#======================================================================
    # GUI initialization
#======================================================================

gui_instance = GUI()
gui_instance.win.mainloop()