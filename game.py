"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random
import numpy as np
import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	
	def __init__(self, name, power, min_level):
		self.__nom = name
		self.power = power
		self.min_level = min_level
	
	def make_unarmed():
		UNARMED_POWER = 20
		return Weapon('Unarmed', UNARMED_POWER)
    	

class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level, weapon, hp):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp = hp
	
	def compute_damage(a:Character(), d:Character()):
		crit = np.random.choice([1,2], p=[15/16, 1/16])
		rand = random.randint(85,100) / 100
		return ((((2 * a.level() / 5 + 2) * a.weapon.power * (a.attack / d.defense)) / 50) + 2) * crit * rand


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	defender.max_hp -= attacker.compute_damage(attacker, defender)
	


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	tour = 0

	while c1.

	return tour
