#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  9-3.py
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

class User():
	
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name  = last_name
		self.age        = age
		
	def describe_user(self):
		full_name = self.first_name + " " + self.last_name
		print(full_name.title() + "'s age is " + str(self.age))
		
	def greet_user(self):
		full_name = self.first_name + " " + self.last_name
		print("Hello, " + full_name.title())
		
user_01 = User('Yejing', 'huang', 20)
user_01.describe_user()
user_01.greet_user()

user_02 = User('jiajun', 'chen', 15)
user_02.describe_user()
user_02.greet_user()

