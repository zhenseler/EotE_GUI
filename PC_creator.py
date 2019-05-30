
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import ImageTk, Image


import pickle
from copy import deepcopy

import Player_class
import Navigate_frames
import Eote_manual
import Talent_list


class PC_Creator:
    def __init__(self, PC_dict):
        self.creation_popup = tk.Toplevel()
        self.creation_popup.title("Create New PC")
        self.PC_dict = PC_dict

        # List that holds all frame objects
        self.creation_popup_frame_list = Navigate_frames.Navigate_frames(7, self.creation_popup)

        self.frame_1 = self.creation_popup_frame_list.frame_list[0].frame
        self.frame_1_draw()
        self.frame_2 = self.creation_popup_frame_list.frame_list[1].frame
        self.frame_3 = self.creation_popup_frame_list.frame_list[2].frame




    # ======================================================================
    # Generic functions
    # ======================================================================

    # Throw an error message, displaying text
    def generic_error_message(self, text, title = 'ERROR', exception = 'generic_error_message thrown'):
        msg.showwarning(title, text)
        raise Exception(exception)

    # Throw an error message when a required field is empty
    def empty_field_error_message(self, field_string):
        msg.showwarning('Required Field Missing', 'The required field ' + field_string + ' is missing')
        raise ValueError('Required field must be filled')

    # Takes a list of widgets and makes sure none are empty
    def check_if_empty(self, widget, field_string):
        if getattr(widget, "get")() == '':
            self.empty_field_error_message(field_string)

    # Setting possible values of Specialization based off of selected Career
    def callback(self, caught_event):
        selected_career = self.frame_1_widget_dict["Career"].get()
        self.frame_1_widget_dict["Specialization Tree"]['values'] = Eote_manual.specialization[
            selected_career]
        self.frame_1_widget_dict["Specialization Tree"].current(0)



    # ======================================================================
    # Drawing frames
    # ======================================================================


    # Drawing frame 1

    def frame_1_draw(self):
        self.frame_1_widget_dict = {}

        self.creation_entry_fields = [("Character Name", "entry"),
                                      ("Player", "entry"),
                                      ("Species", "combobox", Eote_manual.species),
                                      ("Career", "combobox", Eote_manual.career),
                                      ("Specialization Tree", "combobox", Eote_manual.specialization_default)]

        # Adds all of the widgets in the self.creation_entry_fields list
        for i, field in enumerate(self.creation_entry_fields):

            col_pos = i%2               # Set column position
            row_pos = 1+(i-i%2)         # Set row position

            # Add label above widget to be added
            self.frame_1_widget_dict[field[0]] = field_label = ttk.Label(self.frame_1, text = field[0])
            field_label.grid(column = col_pos, row = row_pos - 1)

            if field[1] == "entry":
                self.frame_1_widget_dict[field[0]] = field_entry = ttk.Entry(self.frame_1, width = 12)
                field_entry.grid(column = col_pos, row = row_pos)

            elif field[1] == "combobox":
                self.frame_1_widget_dict[field[0] + "_combobox_var"] = field_combobox_var = tk.StringVar()
                self.frame_1_widget_dict[field[0]] = field_combobox = ttk.Combobox(self.frame_1,
                                                                    width = 12, textvariable = field_combobox_var,
                                                                    state = "readonly")
                field_combobox.grid(column = col_pos, row = row_pos)
                field_combobox['values'] = field[2]
                if field[0] == "Career":
                    field_combobox.bind("<<ComboboxSelected>>", self.callback)

        self.frame_1_widget_dict["back_button"] = back_button = ttk.Button(self.frame_1, text = 'back', command = self.creation_popup.destroy)
        back_button.grid(column = 0, row = 101)
        self.frame_1_widget_dict["next_button"] = next_button = ttk.Button(self.frame_1, text = 'next', command = self.frame_1_next_function)
        next_button.grid(column = 2, row = 101)

    # Modify 'Next' button in frame_1 to check for completion
    def frame_1_next_function(self):
        self.new_PC_name = self.frame_1_widget_dict["Character Name"].get()
        if self.new_PC_name in self.PC_dict:
            self.generic_error_message(
                'The entered Character Name is already present in the database.\n\nPlease choose a different name')

        # Create new PC instance with input data.  Will not save in database until finished.
        self.frame_1_stats = []
        for field in self.creation_entry_fields:
            widget = self.frame_1_widget_dict[field[0]]
            self.check_if_empty(widget, field[0])
            self.frame_1_stats.append(widget.get())
        self.new_PC = Player_class.PC(*self.frame_1_stats)

        starting_talent_tree_string = self.frame_1_widget_dict["Specialization Tree"].get()
        self.new_PC.owned_talent_trees.append(starting_talent_tree_string)
        starting_talent_tree_constructor = Talent_list.tree_constructor_dict[starting_talent_tree_string]
        self.new_PC.talent_tree_dict[starting_talent_tree_string] = Talent_list.Talent_tree(starting_talent_tree_constructor)


        self.creation_popup_frame_list.frame_list[0].next()
        self.frame_2_draw()





    # Drawing frame 2

    def frame_2_draw(self):
        self.frame_2_widget_dict = {}
        self.frame_2_checkbox_list_career = []
        self.frame_2_checkbox_list_bonus = []

        # Make a saved state of the new_PC
        self.new_PC_backup_post1 = deepcopy(self.new_PC)

        self.frame_2_widget_dict["career_label"] = career_label = ttk.Label(self.frame_2, text="Select 4 career skills to gain a free rank in")
        career_label.grid(column = 0, row = 0, columnspan = 8, pady = 10)
        career_label.configure(anchor = "center")

        career_row_number = [1,1,1,1,2,2,2,2]
        career_col_number = [0,2,4,6,0,2,4,6]
        spec_row_number = [4,4,4,4]
        spec_col_number = [0,2,4,6]

        for i, career_skill in enumerate(Eote_manual.career_skills[self.new_PC.career]):
            checkbox = ttk.Checkbutton(self.frame_2, text = career_skill, width = 12)
            checkbox.grid(column = career_col_number[i], row = career_row_number[i], sticky = "W", padx = 1, pady = 1)
            checkbox.invoke()
            checkbox.invoke()
            self.frame_2_checkbox_list_career.append(checkbox)

        self.frame_2_widget_dict["bonus_label"] = bonus_label = ttk.Label(self.frame_2, text = "Select 2 bonus career skills to gain a free rank in\n(based on specialization)")
        bonus_label.grid(column = 0, row = 3, columnspan = 8, pady = 10)
        bonus_label.configure(anchor = "center")

        for i, bonus_skill in enumerate(Eote_manual.bonus_career_skills[self.new_PC.specialization]):
            checkbox = ttk.Checkbutton(self.frame_2, text = bonus_skill, width = 12)
            checkbox.grid(column = spec_col_number[i], row = spec_row_number[i], sticky = "W", padx = 1, pady = 1)
            checkbox.invoke()
            checkbox.invoke()
            self.frame_2_checkbox_list_bonus.append(checkbox)

        self.frame_2_widget_dict["next_button"] = next_button = ttk.Button(self.frame_2, text = 'next', command = self.frame_2_next_function)
        next_button.grid(column = 2, row = 101)
        self.frame_2_widget_dict["back_button"] = back_button = ttk.Button(self.frame_2, text = 'back', command = self.frame_2_back_function)
        back_button.grid(column = 0, row = 101)

    # Check that correct number of checkboxes are checked before advancing to frame 3
    def frame_2_next_function(self):
        total_career_checked = 0
        career_list = []
        total_bonus_checked = 0
        print(self.frame_2_checkbox_list_career)
        for widget in self.frame_2_checkbox_list_career:
            if widget.state() == ('selected',):
                total_career_checked += 1
                career_list.append(widget["text"])
        for widget in self.frame_2_checkbox_list_bonus:
            if widget.state() == ('selected',):
                total_bonus_checked += 1
                career_list.append(widget["text"])
        if total_career_checked == 4 and total_bonus_checked == 2:
            for skill in career_list:
                skill_to_increase = getattr(self.new_PC, skill)
                setattr(skill_to_increase, "rank", skill_to_increase.rank + 1)
            self.creation_popup_frame_list.frame_list[1].next()
            self.frame_3_draw()
        else:
            self.generic_error_message("Please select 4 career skills and 2 bonus skills")

    def frame_2_back_function(self):
        del self.new_PC
        self.creation_popup_frame_list.frame_list[1].back()
        list = self.frame_2.grid_slaves()
        for l in list:
            l.destroy()





    # Draw frame 3

    def frame_3_draw(self):
        self.frame_3_widget_dict = {}

        self.frame_3_widget_dict["XP_label"] = XP_label = ttk.Label(self.frame_3, text = "XP")
        XP_label.grid(column = 0, row = 0)

        self.frame_3_widget_dict["XP_entry_var"] = XP_entry_var = tk.StringVar()
        XP_entry_var.set(str(self.new_PC.current_XP) + " / " + str(self.new_PC.starting_XP))

        self.frame_3_widget_dict["XP_entry"] = XP_entry = ttk.Entry(self.frame_3, textvariable = XP_entry_var, width = 12)
        XP_entry.grid(column = 0, row = 1)

        self.frame_3_widget_dict["obligation_label"] = obligation = ttk.Label(self.frame_3, text = "Obligation")
        obligation.grid(column = 4, row = 0)

        self.frame_3_widget_dict["obligation_entry_var"] = obligation_entry_var = tk.IntVar()
        obligation_entry_var.set(0)

        self.frame_3_widget_dict["obligation_entry"] = obligation_entry = ttk.Entry(self.frame_3, textvariable = obligation, width = 12)
        obligation_entry.grid(column = 4, row = 1)

        self.frame_3_widget_dict["five_obligation_label"] = five_obligation_label = ttk.Label(self.frame_3, text = "+5 Obligation")
        five_obligation_label.grid(column = 5, row = 0)

        self.frame_3_widget_dict["five_XP_button"] = five_XP_button = ttk.Checkbutton(self.frame_3, text = "+5 starting XP")
        five_XP_button.grid(column = 5, row = 1)

        self.frame_3_widget_dict["ten_XP_button"] = ten_XP_button = ttk.Checkbutton(self.frame_3, text = "+10 starting XP")
        ten_XP_button.grid(column = 6, row = 1)

        self.frame_3_widget_dict["ten_obligation_label"] = ten_obligation_label = ttk.Label(self.frame_3, text = "+10 Obligation")
        ten_obligation_label.grid(column = 6, row = 0)

        self.frame_3_widget_dict["one_k_cred_button"] = one_k_cred_button = ttk.Checkbutton(self.frame_3, text="+1k credits")
        one_k_cred_button.grid(column = 5, row = 2)

        self.frame_3_widget_dict["twop5_k_cred_button"] = twop5_k_cred_button = ttk.Checkbutton(self.frame_3, text="+2.5k credits")
        twop5_k_cred_button.grid(column = 6, row = 2)

        self.frame_3_widget_dict["reset_button"] = reset_button = ttk.Button(self.frame_3, text = "Reset", command = self.reset_2)
        reset_button.grid(column = 8, row = 0)

        for i, char in enumerate(["Brawn", "Agility", "Intellect", "Cunning", "Willpower", "Presence"]):
            self.frame_3_widget_dict[char + "_buttons"] = Char_buttons(self.frame_3, self.new_PC, char, i, self.frame_3_widget_dict)

        for i, skill in enumerate(Eote_manual.general_skill_list):
            self.frame_3_widget_dict[skill[0] + "_widgets"] = Skill_widgets(self.frame_3, self.new_PC, skill[0], 0, i+7, self.frame_3_widget_dict)

        for i, skill in enumerate(Eote_manual.combat_skill_list):
            self.frame_3_widget_dict[skill[0] + "_widgets"] = Skill_widgets(self.frame_3, self.new_PC, skill[0], 9, i + 7, self.frame_3_widget_dict)

        for i, skill in enumerate(Eote_manual.knowledge_skill_list):
            self.frame_3_widget_dict[skill[0] + "_widgets"] = Skill_widgets(self.frame_3, self.new_PC, skill[0], 9, i + 14, self.frame_3_widget_dict)

        self.frame_3_widget_dict["talent_button"] = talent_button = ttk.Button(self.frame_3, text = "Talent Tree", command = self.draw_talent_frame)
        talent_button.grid(column = 9, row = 22)

        self.frame_3_widget_dict["next_button"] = next_button = ttk.Button(self.frame_3, text='next',command = self.creation_popup_frame_list.frame_list[2].next)
        next_button.grid(column = 2, row = 101)
        self.frame_3_widget_dict["back_button"] = back_button = ttk.Button(self.frame_3, text='back',command = self.frame_3_back_function)
        back_button.grid(column = 0, row = 101)




    # Restore new_PC to how it was at the end of frame 2
    def reset_2(self):
        del self.new_PC
        self.new_PC = deepcopy(self.new_PC_backup_post1)

    def frame_3_back_function(self):
        del self.new_PC
        self.new_PC = deepcopy(self.new_PC_backup_post1)
        self.creation_popup_frame_list.frame_list[2].back()
        list = self.frame_3.grid_slaves()
        for l in list:
            l.destroy()


    def draw_talent_frame(self):
        self.frame_3_widget_dict["talent_frame"] = talent_frame = tk.Toplevel(self.frame_3)
        tab_control = ttk.Notebook(talent_frame)
        self.tab_1 = ttk.Frame(tab_control)
        tab_control.add(self.tab_1, text = self.new_PC.specialization)
        tab_control.pack(expand = 1, fill = "both")
        self.frame_3_widget_dict["talent_canvas"] = talent_canvas = tk.Canvas(self.tab_1)
        talent_canvas.grid(column = 0, row = 0)
        x = Talent_list.Draw_talent_tree(talent_canvas, self.new_PC, self.new_PC.specialization, talent_frame, self.frame_3_widget_dict["XP_entry_var"])








# ======================================================================
# Frame 3 classes
# ======================================================================


# Class containing all buttons associated with changing characteristics
class Char_buttons(object):
    def __init__(self, master, new_PC, char, column, widget_dict):
        self.master = master    # Master frame (frame_3)
        self.new_PC = new_PC
        self.char = char
        self.column = column
        self.row = 3
        self.widget_dict = widget_dict

        self.increase_button = ttk.Button(master, text = "↑", command = self.increase_char, width = 0.5)
        self.increase_button.grid(column = self.column, row = self.row)

        self.char_var = tk.IntVar()
        self.char_var.set(getattr(self.new_PC, self.char))

        self.char_entry = ttk.Entry(master, textvariable = self.char_var, width = 1, state = 'disabled')
        self.char_entry.grid(column = self.column, row = self.row + 1, sticky = "NS")

        self.char_label = ttk.Label(master, text = self.char)
        self.char_label.grid(column = self.column, row = self.row + 2)

        self.decrease_button = ttk.Button(master, text = "↓", command = self.decrease_char, width = 0.5)
        self.decrease_button.grid(column = self.column, row = self.row + 3)

    def increase_char(self):
        self.new_PC.change_characteristic(self.char, "+")
        # Reset XP tracker widget
        self.widget_dict["XP_entry_var"].set(str(self.new_PC.current_XP) + " / " + str(self.new_PC.starting_XP))
        # Reset skill die images
        for skill in Eote_manual.skills_by_char_dict[self.char]:
            self.widget_dict[skill + "_widgets"].set_dice()
        # Reset char entry value
        self.char_var.set(self.char_var.get() + 1)

    def decrease_char(self):
        self.new_PC.change_characteristic(self.char, "-")
        # Reset XP tracker widget
        self.widget_dict["XP_entry_var"].set(str(self.new_PC.current_XP) + " / " + str(self.new_PC.starting_XP))
        # Reset skill die images
        for skill in Eote_manual.skills_by_char_dict[self.char]:
            self.widget_dict[skill + "_widgets"].set_dice()
        # Reset char entry value
        self.char_var.set(self.char_var.get() - 1)



class Skill_widgets(object):
    def __init__(self, master, new_PC, skill_name, column, row, widget_dict):
        self.master = master
        self.new_PC = new_PC
        self.skill_name = skill_name
        self.column = column
        self.row = row
        self.widget_dict = widget_dict

        # Skill object on new_PC
        self.new_PC_skill = getattr(self.new_PC, self.skill_name)

        if self.skill_name in self.new_PC.career_skill_list:
            self.iscareer = True
        else:
            self.iscareer = False

        self.skill_label = ttk.Label(self.master, text = self.skill_name)
        self.skill_label.grid(column = column, row = row, sticky = "W")

        self.char_label = ttk.Label(self.master, text = self.new_PC_skill.char)
        self.char_label.grid(column = column + 1, row = row, sticky = "W")

        self.decrease_button = ttk.Button(self.master, text = "-", command = self.decrease_skill, width = 1)
        self.decrease_button.grid(column = column + 2, row = row)

        green_die = Image.open("images/green_die.gif")
        green_die = green_die.resize((10, 20))  # The (250, 250) is (height, width)
        self.green_die = ImageTk.PhotoImage(green_die)

        yellow_die = Image.open("images/yellow_die.gif")
        yellow_die = yellow_die.resize((20, 20))  # The (250, 250) is (height, width)
        self.yellow_die = ImageTk.PhotoImage(yellow_die)

        white_die = Image.open("images/white_die.gif")
        white_die = white_die.resize((20, 20))  # The (250, 250) is (height, width)
        self.white_die = ImageTk.PhotoImage(white_die)

        self.die_spot_list = []
        for i in range(5):
            die_spot = ttk.Label(self.master, image = self.white_die)
            die_spot.grid(column = self.column + 3 + i, row = row)
            self.die_spot_list.append(die_spot)

        self.set_dice()

        self.increase_button = ttk.Button(self.master, text = "+", command = self.increase_skill, width = 1)
        self.increase_button.grid(column = self.column + 8, row = self.row)





    def set_dice(self):
        char_value = getattr(self.new_PC, self.new_PC_skill.char)
        skill_value = self.new_PC_skill.rank
        value_list = sorted([char_value, skill_value])
        die_list = []

        die_list += ["y"] * value_list[0]
        die_list += ["g"] * (value_list[1] - value_list[0])
        die_list += ["w"] * (5 - value_list[0] - (value_list[1] - value_list[0]))

        for i,die_spot in enumerate(self.die_spot_list):
            config = getattr(die_spot, "configure")
            if die_list[i] == "y":
                config(image = self.yellow_die)
            elif die_list[i] == "g":
                config(image=self.green_die)
            elif die_list[i] == "w":
                config(image=self.white_die)

    def decrease_skill(self):
        self.new_PC.change_skill(self.skill_name, "-")
        self.set_dice()
        self.widget_dict["XP_entry_var"].set(str(self.new_PC.current_XP) + " / " + str(self.new_PC.starting_XP))

    def increase_skill(self):
        self.new_PC.change_skill(self.skill_name, "+")
        print(self.new_PC_skill.rank)
        self.set_dice()
        self.widget_dict["XP_entry_var"].set(str(self.new_PC.current_XP) + " / " + str(self.new_PC.starting_XP))











#=================================================



