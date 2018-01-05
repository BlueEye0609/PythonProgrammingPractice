#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  blue_sky.py
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

import sys
import pygame

def run_games():
	pygame.init()
	screen = pygame.display.set_mode((600,600))
	pygame.display.set_caption("BLue Sky")
	
	bg_color = (230, 255, 255)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()
	
run_games()
	
