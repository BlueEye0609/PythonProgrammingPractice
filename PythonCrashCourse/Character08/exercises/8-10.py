#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  8-10.py
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


def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	while magicians:
		magician = magicians.pop()
		
		print("Make great of " + magician)
		magician = "the Great " + magician
		great_magicians.append(magician)
			
magicians = ['liu qian', 'Yejing', 'Andre']
great_magicians = [];
make_great(magicians)
show_magicians(great_magicians)
