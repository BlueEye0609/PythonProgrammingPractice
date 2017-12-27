#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  7-5.py
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

active = True
while active:
	age = input("How old are you? ")
	age = int(age)
	if 0 < age < 3:
		print("Free")
	elif 3 <= age <= 12:
		print("Pay 10 dollars")
	elif age > 12:
		print("Pay 15 dollars")
	else:
		active = False
