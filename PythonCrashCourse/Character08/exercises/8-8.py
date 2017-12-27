#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  8-8.py
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


def make_album(singer, album, number=''):
	singer_album = {'singer': singer, 'album': album}
	if number:
		singer_album['number'] = number
	return singer_album
	
while True:
	print("(Enter 'q' at any time to quit)")
	singer = input("Please enter a singer's name: ")
	
	if singer == 'q':
		break
		
	album = input("Please enter album name for this singer: ")
	
	if album == 'q':
		break
		
	info = make_album(singer, album)
	print(info)