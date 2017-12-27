#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  6-4.py
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


vocabulary = {
   'key': 'direcotry key',
   'value': 'the value of directory key',
   'variable': 'a variable',
   'list': 'a list to store multipl;e variables',
   'string': 'contains alphiebt', 
   'directory ;list': 'I dont know what it is'
}

for word, description in vocabulary.items():
	print(word + ": " + description)
