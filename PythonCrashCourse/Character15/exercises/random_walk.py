#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  random_walk.py
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

from random import choice

class RandomWalk():
	
	def __init__(self, num_points=5000):
		self.num_points = num_points
		
		self.x_values = [0]
		self.y_values = [0]
		
	def get_step(self):
		direction = choice([1, -1])
		distance  = choice(list(range(0,9)))
		step = direction * distance
		return step
		
		
	def fill_walk(self):
		
		while len(self.x_values) < self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()
			
			# forbidden stay
			if x_step == 0 and y_step == 0:
				continue
				
			# compute next point x and y
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
