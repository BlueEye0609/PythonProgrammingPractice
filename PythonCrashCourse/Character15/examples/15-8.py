#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  15-8.py
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

from die import Die
import pygal

# three dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# get results
results = []
for roll_num in range(5000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)
	
# analyze
frequencies = []
max_result = die_1.max_num() + die_2.max_num() + die_3.max_num()

for value in range(3, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	

# visual
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = list(range(
	die_1.min_num() + die_2.min_num() + die_3.min_num(), 
	die_1.max_num() + die_2.max_num() + die_3.max_num() + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add('D6+D6+D6', frequencies)
hist.render_to_file('three_dice_visual.svg')
