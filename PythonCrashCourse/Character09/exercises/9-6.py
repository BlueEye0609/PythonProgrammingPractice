#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  9-6.py
#  
#  Copyright 2017 c5220056 <c5220056@GMPTIC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type    = cuisine_type
		self.number_served   = 0
		
	def describe_restaurant(self):
		print("Restaurant name is " + self.restaurant_name)
		print("Cuisine type is " + self.cuisine_type)
		print("Has served " + str(self.number_served) + " people.")
		
	def open_restaurant(self):
		print("Restaurant " + self.restaurant_name + " is opening.")
		
	def set_number_served(self, number):
		self.number_served = number
		
	def increment_number_served(self, incre_number):
		self.number_served += incre_number	
	
class IceCreamStand(Restaurant):
	
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []
		
	def print_flavors(self, flavors):
		print("\nThis ice-cream includes flavors: ")
		for flavor in flavors:
			print("- " + flavor)
			
icecreameStand_01 = IceCreamStand('Snow Flower', 'Leng Yin')
icecreameStand_01.print_flavors(['chocolate', 'xiang cao'])


