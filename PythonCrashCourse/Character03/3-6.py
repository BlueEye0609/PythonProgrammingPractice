#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  3-6.py
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


names = ['Jin rui', 'TJJ', 'CJJ', 'XZF']
print("I'd like to invite " + names[0] + " for dinner")
print("I'd like to invite " + names[1] + " for dinner")
print("I'd like to invite " + names[2] + " for dinner")
print("I'd like to invite " + names[3] + " for dinner")

print(names[0] + " can't join, SHY will come")
names[0] = "SHY"
print("I'd like to invite " + names[0] + " for dinner")
print("I'd like to invite " + names[1] + " for dinner")
print("I'd like to invite " + names[2] + " for dinner")
print("I'd like to invite " + names[3] + " for dinner")

print("I found a bigger table, I'll invite three more people")
names.insert(0, 'haha')
names.insert(2, 'xixi')
names.append('wuwuwu')
print("I'd like to invite " + names[0] + " for dinner")
print("I'd like to invite " + names[1] + " for dinner")
print("I'd like to invite " + names[2] + " for dinner")
print("I'd like to invite " + names[3] + " for dinner")
print("I'd like to invite " + names[4] + " for dinner")
print("I'd like to invite " + names[5] + " for dinner")
print("I'd like to invite " + names[6] + " for dinner")

