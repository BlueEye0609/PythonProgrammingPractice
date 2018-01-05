#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  15-3.py
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


import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	rw = RandomWalk()
	rw.fill_walk()
	
	# set windows size
	plt.figure(dpi=128, figsize=(10, 6))
	
	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, linewidth=1)
	
	# standout starting and end position
	plt.scatter(0, 0, c='green', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
	    edgecolor='none', s=100)
	    
	# hide axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
