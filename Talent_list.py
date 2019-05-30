# ======================================================================
# Talent Trees
# ======================================================================

class Talent_tree(object):
    def __init__(self, construction_tuple):
        talent_tuple = construction_tuple[0]
        self.position_tuple = construction_tuple[1]
        self.tree_list = []
        for i, talent in enumerate(talent_tuple):
            setattr(self, "pos_" + str(i), talent)
            setattr(talent, "pos", i)
            self.tree_list.append(talent)
            #row = i // 5
            #setattr(val, "row", row)
            #column = i % 4
            #setattr(val, "column", column)
            if i < 4:
                talent_connected_to_list = getattr(talent, "connected_to")
                talent_connected_to_list.append("root")
                setattr(talent, "XP_cost", 5)
            elif i < 8:
                setattr(talent, "XP_cost", 10)
            elif i < 12:
                setattr(talent, "XP_cost", 15)
            elif i < 16:
                setattr(talent, "XP_cost", 20)
            elif i < 20:
                setattr(talent, "XP_cost", 25)





        for pos in self.position_tuple:
            if pos < 15:
                first_index = pos + (pos // 3)
                second_index = first_index + 1
            elif pos < 31:
                first_index = pos - 15
                second_index = first_index + 4
            else:
                raise ValueError()
            
            first_talent = getattr(self, "pos_" + str(first_index))
            second_talent =getattr(self, "pos_" + str(second_index))
            first_talent_connected_to_list = getattr(first_talent, "connected_to")
            second_talent_connected_to_list = getattr(second_talent, "connected_to")
            first_talent_connected_to_list.append(second_index)
            second_talent_connected_to_list.append(first_index)















# ======================================================================
# Talents
# ======================================================================

class Talent(object):
    def __init__(self):
        self.owned = False
        self.connected_to = []
    def test_method(self):
        print(self.name)
        print(self.text)
        print(self.XP_cost)
        print(self.owned)




class Grit(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Grit"
        self.text = "Gain +1 strain threshold."
        self.type = "Passive"



class Lethal_blows(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Lethal Blows"
        self.text = "Add +10 per rank of Lethal Blows to any Critical Injury results inflicted on opponents."
        self.type = "Passive"


class Stalker(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Stalker"
        self.text = "Add BLUE_DIE per rank of Stalker to all Stealth and Coordination checks."
        self.type = "Passive"



class Dodge(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Dodge"
        self.text = "When targeted by combat check, may perform a Dodge incidental to suffer a number of strain" \
                    " no greater than ranks of Dodge, then upgrade the difficulty of the check by that number."
        self.type = "Active"


class Precise_aim(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Precise Aim"
        self.text = "Once per round, may perform Precise Aim maneuver.  Suffer a number of strain no greater than " \
                    "ranks in in Precise Aim, then reduce target's melee and ranged defense by that number."
        self.type = "Active"



class Jump_up(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Jump Up"
        self.text = "Once per round, may stand from seated or prone as an incidental."
        self.type = "Active"



class Quick_strike(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Quick Strike"
        self.text = "Add BLUE_DIE per rank of Quick Strike to combat checks against targets that have not acted yet" \
                    " this encounter."
        self.type = "Passive"



class Quick_draw(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Quick Draw"
        self.text = "Once per round, draw or holster a weapon or accessible item as an incidental."
        self.type = "Active"



class Targeted_blow(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Targeted Blow"
        self.text = "After making a successful attack, may spend 1 Destiny Point to add damage equal to Agility to one hit."
        self.type = "Active"


class Anatomy_lessons(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Anatomy Lessons"
        self.text = "After making a successful attack, may spend 1 Destiny Point to add damage equal to Intellect to one hit."
        self.type = "Active"


class Sniper_shot(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Sniper Shot"
        self.text = "Before making a non-thrown ranged attack, may perform a Sniper Shot maneuver to increase " \
                    "the weapon's range by 1 range pand per rank in Sniper Shot.  Upgrade the difficulty of the attack " \
                    "1 per range band increase."
        self.type = "Active"


class Deadly_accuracy(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Deadly Accuracy"
        self.text = "When acquired, choose 1 combat skill.  Add damage equal to ranks in that skill to one hit of " \
                    "successful attacks made using that skill."
        self.type = "Passive"



class Dedication(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Dedication"
        self.text = "Gain +1 to a single characteristic,  This cannot bring a characteristic above 6."
        self.type = "Passive"


class Master_of_shadows(Talent):
    def __init__(self):
        Talent.__init__(self)

        self.name = "Master of Shadows"
        self.text = "Once per round, suffer 2 strain to decrease difficulty of next Stealth or Skulduggery check by one."
        self.type = "Active"




# ======================================================================
# Visualization code
# ======================================================================


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg



class Talent_widgets(object):
    def __init__(self, master, PC, talent, i, XP_entry_var, talent_GUI_widget_list):
        self.master = master
        self.PC = PC
        self.talent = talent    # Actual talent instance
        self.i = i
        self.XP_entry_var = XP_entry_var
        self.talent_GUI_widget_list = talent_GUI_widget_list      # List of talents on particular tree

        self.talent_GUI_dict = {}

        self.talent_GUI_dict["frame"] = talent_frame = ttk.Frame(self.master, width = 30, height = 15)
        self.row = self.i // 4
        self.column = self.i % 4
        talent_frame.grid(column = self.column, row = self.row, sticky = "NSEW", padx = 20, pady = 20)

        self.talent_GUI_dict["checkbutton_var"] = checkbutton_var = tk.IntVar()
        self.talent_GUI_dict["checkbutton"] = checkbutton = ttk.Checkbutton(talent_frame, text=talent.name,
                                                                            variable = checkbutton_var,
                                                                            command = self.test_checkbutton)
        if self.talent.owned == True:
            checkbutton_var.set(1)
        elif self.talent.owned == False:
            checkbutton_var.set(0)
        checkbutton.grid(column = 0, row = 0, sticky = "NW")

        self.talent_GUI_dict["text"] = text = ttk.Label(talent_frame, text = talent.text, width = 30, wraplength = 150)
        text.config(font = ("Helvetica", 9))
        text.grid(column = 0, row = 1, sticky = "NSEW")

        self.talent_GUI_dict["XP_cost"] = XP_cost = ttk.Label(talent_frame, text = talent.XP_cost)
        XP_cost.grid(column = 1, row = 2, sticky = "SE")


    def test_checkbutton(self):
        # If selecting...
        if self.talent_GUI_dict["checkbutton_var"].get() == 1:
            if self.PC.current_XP - self.talent.XP_cost < 0:
                self.talent_GUI_dict["checkbutton_var"].set(0)
                self.generic_error_message("Not enough XP")
            else:
                if "root" in self.talent.connected_to:
                    self.PC.current_XP -= self.talent.XP_cost
                    self.XP_entry_var.set(str(self.PC.current_XP) + " / " + str(self.PC.starting_XP))
                else:
                    connection_owned = False
                    for connection in self.talent.connected_to:
                        if self.talent_GUI_widget_list[connection].talent_GUI_dict["checkbutton_var"].get() == 1:
                            connection_owned = True
                    if connection_owned == False:
                        self.talent_GUI_dict["checkbutton_var"].set(0)
                        self.generic_error_message("No connected talent is owned")
                    else:
                        self.PC.current_XP -= self.talent.XP_cost
                        self.XP_entry_var.set(str(self.PC.current_XP) + " / " + str(self.PC.starting_XP))
        # If deselecting...
        else:
            self.PC.current_XP += self.talent.XP_cost
            self.XP_entry_var.set(str(self.PC.current_XP) + " / " + str(self.PC.starting_XP))

        # Throw an error message, displaying text
    def generic_error_message(self, text, title = 'ERROR', exception = 'generic_error_message thrown'):
        msg.showwarning(title, text)
        raise Exception(exception)



class Draw_talent_tree(object):
    def __init__(self, master, PC, talent_tree_name, talent_frame, outside_XP_tracker_var):
        self.master = master
        self.PC = PC
        self.talent_tree_name = talent_tree_name
        self.talent_tree_dict = PC.talent_tree_dict
        self.talent_tree = self.talent_tree_dict[talent_tree_name]
        self.talent_frame = talent_frame
        self.outside_XP_tracker_var = outside_XP_tracker_var

        self.talent_list = self.talent_tree.tree_list

        self.talent_GUI_widget_list = [None] * 20

        self.XP_entry_var = tk.StringVar()
        self.XP_entry_var.set(str(self.PC.current_XP) + " / " + str(self.PC.starting_XP))

        for i, talent in enumerate(self.talent_list):
            self.talent_GUI_widget_list[i] = Talent_widgets(self.master, self.PC, talent, i, self.XP_entry_var, self.talent_GUI_widget_list)

        self.master.update_idletasks()

        for pos in self.talent_tree.position_tuple:
            if pos < 15:
                first_index = pos + (pos // 3)
                second_index = first_index + 1
                first_coord_x = self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_x() + (self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_width()*0.5)
                first_coord_y = self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_y() + (self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_height()*0.5)
                second_coord_x = self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_x() + (self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_width()*0.5)
                second_coord_y = self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_y() + (self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_height()*0.5)
                self.master.create_line(first_coord_x, first_coord_y, second_coord_x, second_coord_y)

            elif pos < 31:
                first_index = pos - 15
                second_index = first_index + 4
                first_coord_x = self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_x() + (self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_width()*0.5)
                first_coord_y = self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_y() + (self.talent_GUI_widget_list[first_index].talent_GUI_dict["frame"].winfo_height()*0.5)
                second_coord_x = self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_x() + (self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_width()*0.5)
                second_coord_y = self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_y() + (self.talent_GUI_widget_list[second_index].talent_GUI_dict["frame"].winfo_height()*0.5)
                self.master.create_line(first_coord_x, first_coord_y, second_coord_x, second_coord_y)

        self.XP_label = ttk.Label(self.master, text = "XP")
        self.XP_label.grid(column = 6, row = 0)

        self.XP_entry = ttk.Entry(self.master, textvariable = self.XP_entry_var, width = 12)
        self.XP_entry.grid(column = 6, row = 1)

        self.accept_button = ttk.Button(self.master, text = "Accept", command = self.accept_talent_tree)
        self.accept_button.grid(column = 7, row = 0)



    def accept_talent_tree(self):
        for i, talent in enumerate(self.talent_GUI_widget_list):
            if talent.talent_GUI_dict["checkbutton_var"].get() == 1:
                self.PC.talent_tree_dict[self.talent_tree_name].tree_list[i].owned = True
            elif talent.talent_GUI_dict["checkbutton_var"].get() == 0:
                self.PC.talent_tree_dict[self.talent_tree_name].tree_list[i].owned = False
        self.outside_XP_tracker_var.set(str(self.PC.current_XP) + " / " + str(self.PC.starting_XP))
        self.master.destroy()
        self.talent_frame.destroy()





# ======================================================================
# Tree constructors
# ======================================================================

Assassin_talents = (Grit(), Lethal_blows(), Stalker(), Dodge(), Precise_aim(), Jump_up(), Quick_strike(), Quick_draw(),
                        Targeted_blow(), Stalker(), Lethal_blows(), Anatomy_lessons(), Stalker(), Sniper_shot(), Dodge(), Lethal_blows(),
                        Precise_aim(), Deadly_accuracy(), Dedication(), Master_of_shadows())
Assassin_positions = (3, 4, 5, 7, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)






tree_constructor_dict = {"Assassin": (Assassin_talents, Assassin_positions)}








# ======================================================================
# Unit test
# ======================================================================


if __name__ == "__main__":
    test_tree = Talent_tree(tree_constructor_dict["Assassin"])

    jump_up = test_tree.tree_list[9]
    print(jump_up.name)
    print(jump_up.XP_cost)
    print(jump_up.connected_to)