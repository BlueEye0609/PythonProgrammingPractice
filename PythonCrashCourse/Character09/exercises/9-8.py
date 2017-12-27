#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  9-8.py
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
		self.login_attempts = 0
		
	def describe_user(self):
		full_name = self.first_name + " " + self.last_name
		print(full_name.title() + "'s age is " + str(self.age))
		
	def greet_user(self):
		full_name = self.first_name + " " + self.last_name
		print("Hello, " + full_name.title())
		
	def print_login_attempt(self):
		full_name = self.first_name + " " + self.last_name
		print(full_name.title() + " tried to login " + str(self.login_attempts) + " times")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0


class Privileges():
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def show_privileges(self, user):
		full_name = user.first_name + " " + user.last_name
		print("Admin " + full_name.title() + " has below privileges:")
		for privilege in self.privileges:
			print("- " + privilege)
			
class Admin(User):
	
	def __init__(self, first_name, last_name, age):
		super().__init__(first_name, last_name, age)
		self.privileges = Privileges()
			
			
admin01 = Admin('yejing', 'huang', 20)
admin01.privileges.show_privileges(admin01)



