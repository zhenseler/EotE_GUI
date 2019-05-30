

species = ['Bothan', 'Droid', 'Gand', 'Human', 'Rodian', 'Trandoshan', 'Twi\'lek', 'Wookie']

species_dict = {"Bothan": {"Brawn": 1, "Agility": 2, "Intellect": 2, "Cunning": 3, "Willpower": 2,
                "Presence": 2, "wound_threshold": 10, "strain_threshold": 11, "starting_XP": 100}}




career = ['Bounty Hunter', 'Colonist', 'Explorer', 'Hired Gun', 'Smuggler', 'Technician']



specialization = {'Bounty Hunter': ('','Assassin', 'Gadgeteer', 'Survivalist'), 'Colonist': ('','Doctor', 'Politico', 'Scholar'),
                 'Explorer': ('','Fringer', 'Scout', 'Trader'), 'Hired Gun': ('','Bodyguard', 'Marauder', 'Mercenary Soldier'),
                  'Smuggler': ('','Pilot', 'Scoundrel', 'Thief'), 'Technician': ('','Mechanic', 'Slicer', 'Outlaw Tech')}

specialization_default = ["Select a career"]



career_skills = {'Bounty Hunter': ['Athletics', 'Brawl', 'Perception', 'Piloting_Planetary', 'Piloting_Space', 'Ranged_Heavy', 'Streetwise', 'Vigilance']}

bonus_career_skills = {'Assassin': ['Melee', 'Ranged_Heavy', 'Skulduggery', 'Stealth']}


skill_list = [('Astrogation', 'Intellect'), ('Athletics', 'Brawn'), ('Charm', 'Presence'), ('Coercion', 'Willpower'),
              ('Computers', 'Intellect'), ('Cool', 'Presence'), ('Coordination', 'Agility'), ('Deception', 'Cunning'),
              ('Discipline', 'Willpower'), ('Leadership', 'Presence'), ('Mechanics', 'Intellect'), ('Medicine', 'Intellect'),
              ('Negotiation', 'Presence'), ('Perception', 'Cunning'), ('Piloting_Planetary', 'Agility'),
              ('Piloting_Space', 'Agility'), ('Resilience', 'Brawn'), ('Skulduggery', 'Cunning'), ('Stealth', 'Agility'),
              ('Streetwise', 'Cunning'), ('Survival', 'Cunning'), ('Vigilance', 'Willpower'), ('Brawl', 'Brawn'),
              ('Gunnery', 'Agility'), ('Melee', 'Brawn'), ('Ranged_Light', 'Agility'), ('Ranged_Heavy', 'Agility'),
              ('Knowledge_CoreWorlds', 'Intellect'), ('Knowledge_Education', 'Intellect'),
              ('Knowledge_Lore', 'Intellect'), ('Knowledge_OuterRim', 'Intellect'), ('Knowledge_Underworld', 'Intellect'),
              ('Knowledge_Xenology', 'Intellect')]

general_skill_list = [('Astrogation', 'Intellect'), ('Athletics', 'Brawn'), ('Charm', 'Presence'), ('Coercion', 'Willpower'),
              ('Computers', 'Intellect'), ('Cool', 'Presence'), ('Coordination', 'Agility'), ('Deception', 'Cunning'),
              ('Discipline', 'Willpower'), ('Leadership', 'Presence'), ('Mechanics', 'Intellect'), ('Medicine', 'Intellect'),
              ('Negotiation', 'Presence'), ('Perception', 'Cunning'), ('Piloting_Planetary', 'Agility'),
              ('Piloting_Space', 'Agility'), ('Resilience', 'Brawn'), ('Skulduggery', 'Cunning'), ('Stealth', 'Agility'),
              ('Streetwise', 'Cunning'), ('Survival', 'Cunning'), ('Vigilance', 'Willpower')]

combat_skill_list = [('Brawl', 'Brawn'),('Gunnery', 'Agility'), ('Melee', 'Brawn'),
                     ('Ranged_Light', 'Agility'), ('Ranged_Heavy', 'Agility')]

knowledge_skill_list = [('Knowledge_CoreWorlds', 'Intellect'), ('Knowledge_Education', 'Intellect'),
              ('Knowledge_Lore', 'Intellect'), ('Knowledge_OuterRim', 'Intellect'), ('Knowledge_Underworld', 'Intellect'),
              ('Knowledge_Xenology', 'Intellect')]


skills_by_char_dict = {"Brawn": ["Athletics", "Resilience", "Brawl", "Melee"],
   "Agility": ['Coordination', 'Piloting_Planetary','Piloting_Space', 'Stealth', 'Gunnery', 'Ranged_Light', 'Ranged_Heavy'],
   'Intellect': ['Astrogation', 'Computers', 'Mechanics', 'Medicine', 'Knowledge_CoreWorlds', 'Knowledge_Education', 'Knowledge_Lore', 'Knowledge_OuterRim', 'Knowledge_Underworld', 'Knowledge_Xenology'],
   'Cunning': ['Deception', 'Perception', 'Skulduggery', 'Streetwise', 'Survival'],
   'Willpower': ['Coercion', 'Discipline', 'Vigilance'],
   'Presence': ['Charm', 'Cool', 'Leadership', 'Negotiation']}

