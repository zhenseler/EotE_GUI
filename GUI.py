
import tkinter as tk
from tkinter import ttk
import Player_class


PC_dict = {}


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        # Add title
        self.win.title("EotE GM Assistant")

        self.creation_entry_fields = ["Character Name", "Player", "Species","Career","Specialization Tree"]

        # Add widgets
        self.create_widgets()


    # Modified button click function
    def creation_submit(self):
        new_PC_name = self.creation_entry_dict["Character Name"].get()
        PC_dict[new_PC_name] = Player_class.PC()
        newly_created_PC = PC_dict[new_PC_name]
        for key, val in self.creation_entry_dict.items():
            setattr(newly_created_PC, key, val.get())
        for item in self.creation_entry_fields:
            print(getattr(newly_created_PC, item))
        print("Done")


    def create_widgets(self):
        # Tabs
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "Add New Player")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Something else")
        tabControl.pack(expand=1, fill="both")

        # LabelFrame within "Add New Player" tab
        creation_frame = ttk.LabelFrame(tab1, text = "New character info")
        creation_frame.grid(column = 0, row = 0, padx = 8, pady = 4)

        self.creation_entry_dict = {}
        for i,field in enumerate(self.creation_entry_fields):
            label = ttk.Label(creation_frame, text = field)
            label.grid(column = i%2, row = i-i%2)
            entry = ttk.Entry(creation_frame, width = 12)
            entry.grid(column = i%2, row = 1+(i-i%2))
            self.creation_entry_dict[field] = entry


        # Submit button
        self.creation_submit_button = ttk.Button(creation_frame, text = "Submit", command = self.creation_submit)
        self.creation_submit_button.grid(column = 2, row = 10)




gui_instance = GUI()
gui_instance.win.mainloop()