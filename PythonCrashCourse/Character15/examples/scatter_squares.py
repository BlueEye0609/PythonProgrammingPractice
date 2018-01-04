#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scatter_squares.py
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

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# c is color, c='red' or c=(0,0,0.8)
# plt.scatter(x_values, y_values, c='red', edgecolor='none',s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none',s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
    edgecolor='none',s=40)

# set titles
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

# set quzhi fan wei
plt.axis([0, 1100, 0, 1100000])

plt.show()

# save automatically
# plt.savefig('squares_plot.png', bbox_inches='tight')
