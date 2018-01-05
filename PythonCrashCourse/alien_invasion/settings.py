#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  settings.py
#  
#  Copyright 2018 c5220056 <c5220056@GMPTIC>
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

class Settings():
	# store all alien invasion's settings
	
	def __init__(self):
		"""init game settings"""
		# screen setting
		self.screen_width  = 1200
		self.screen_height = 800
		self.bg_color      = (230, 230, 230)
		
		# ship setting
		self.ship_speed_factor = 1.5
		
		# bullet setting
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
