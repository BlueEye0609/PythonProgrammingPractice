#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dice_visual.py
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

import pygal

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = list(range(die_1.min_num() + die_2.min_num(), die_1.max_num() + die_2.max_num() + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')



