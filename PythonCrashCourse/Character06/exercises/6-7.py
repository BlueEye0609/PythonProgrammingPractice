#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  6-7.py
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

person_0 = {
    'first_name': 'yejing',
    'last_name': 'Huang',
    'age': 20,
    'city': 'Shanghnai',
}

person_1 = {
    'first_name': 'merry',
    'last_name': 'lv',
    'age': 22,
    'city': 'nantong',
}

person_2 = {
    'first_name': 'jiajun',
    'last_name': 'chen',
    'age': 20,
    'city': 'shanghai',
}

people = [person_0, person_1, person_2]

for person in people:
	print(person['first_name'].title() + ' ' + 
		   person['last_name'].title() + 
		   "'s age is " + str(person['age']) +
		   ", city is " + person['city'].title()
	)
