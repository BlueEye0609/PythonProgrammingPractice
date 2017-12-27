#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  9-2.py
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
		
	def describe_restaurant(self):
		print("Restaurant name is " + self.restaurant_name)
		print("Cuisine type is " + self.cuisine_type)
		
	def open_restaurant(self):
		print("Restaurant " + self.restaurant_name + " is opening.")
		
restaurant_1 = Restaurant('KFC', 'fastfood')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('Ma La You Huo', 'Sichuan')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()



