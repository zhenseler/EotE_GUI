import Eote_manual
import Error
import tkinter as tk
from copy import deepcopy


class PC:
    def __init__(self, character_name, player, species, career, specialization):
        self.character_name = character_name
        self.player = player
        self.species = species
        self.species_dict = Eote_manual.species_dict[species].copy()
        self.career = career
        self.specialization = specialization
        self.career_skill_list = Eote_manual.career_skills[self.career].copy()
        for skill in Eote_manual.bonus_career_skills[self.specialization]:
            self.career_skill_list.append(skill)
        '''
        self.Brawn = tk.IntVar()
        self.Agility = tk.IntVar()
        self.Intellect = tk.IntVar()
        self.Cunning = tk.IntVar()
        self.Willpower = tk.IntVar()
        self.Presence = tk.IntVar()

        '''
        self.Brawn = self.species_dict["Brawn"]
        self.Agility = self.species_dict["Agility"]
        self.Intellect = self.species_dict["Intellect"]
        self.Cunning = self.species_dict["Cunning"]
        self.Willpower = self.species_dict["Willpower"]
        self.Presence = self.species_dict["Presence"]

        self.starting_XP = int(self.species_dict["starting_XP"])
        self.current_XP = self.starting_XP

        for skill in Eote_manual.skill_list:
            setattr(self, skill[0], Skill(self, skill[1], skill[0], 0))

        # List of all talent trees owned by string
        self.owned_talent_trees = []
        # Dict to hold all owned talent tree objects
        self.talent_tree_dict = {}


    def change_characteristic(self, char, direction):
        current_value = getattr(self, char)
        if direction == "+":
            XP_cost = (current_value + 1) * 10
            after_XP = self.current_XP - XP_cost
            if after_XP >= 0:
                self.current_XP = after_XP
                setattr(self, char, current_value + 1)
            else:
                Error.generic_error_message("Not enough XP.  You need " + str(XP_cost) + " to increase " + char + " to " + str(current_value + 1))
        elif direction == "-":
            XP_refund = current_value * 10
            self.current_XP += XP_refund
            setattr(self, char, current_value - 1)

    def change_skill(self, skill, direction):
        current_skill = getattr(self, skill)
        current_ranks = current_skill.rank
        if direction == "+":
            XP_cost = (current_ranks + 1) * 5
            if current_skill.iscareer == False:
                XP_cost += 5
            after_XP = self.current_XP - XP_cost
            if after_XP >= 0:
                self.current_XP = after_XP
                setattr(current_skill, "rank", current_ranks + 1)
            else:
                Error.generic_error_message(
                    "Not enough XP.  You need " + str(XP_cost) + " to increase " + skill + " to " + str(
                        current_ranks + 1))
        elif direction == "-":
            XP_refund = current_ranks * 5
            if current_skill.iscareer == False:
                XP_refund += 5
            self.current_XP += XP_refund
            setattr(current_skill, "rank", current_ranks - 1)


# Class for skill
class Skill(object):
    def __init__(self, PC, char, skill_name, rank):
        self.PC = PC
        self.char = char
        self.skill_name = skill_name
        self.rank = rank

        if self.skill_name in self.PC.career_skill_list:
            self.iscareer = True
        else:
            self.iscareer = False

class Talent_tree(object):
    def __init__(self, PC, tree_name):
        self.PC = PC
        self.tree_name = Eote_manual[tree_name + "_tree"]


class Talent_node(object):
    def __init__(self, PC, talent_name, position, connection_list):
        self.PC = PC
        self.master = master
        self.talent_name = talent_name
        self.position = position
        self.connection_list = connection_list

        self.talent_tree_matrix = deepcopy(self.PC.talent_tree_matrix)

