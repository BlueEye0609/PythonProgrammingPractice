#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5-2.py
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

print("string equal?")
print('car' == 'Car')
print('car' == 'car')
print('car' != 'Car')
print('car' != 'car')

print("test lower letter equal?")
car = 'BMW'
print(car.lower() == 'bmw')
print(car.lower() != 'bmw')
print('BMW'.lower() == 'bmw')

print("number equal")
print( 1 == 1 )
print( 1 == 2 )

print( 1 != 1 )
print( 1 != 2 )

print( 2 <= 3 )

print("test in list")
lists = ['test1', 'test2', 'test3']
print('test1' in lists)
print('test4' in lists)
print('test1' not in lists)
print('test4' not in lists)
