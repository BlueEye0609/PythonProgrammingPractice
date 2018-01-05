#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bullet.py
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

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self, ai_settings, screen, ship):
		"""create a bullet object where ship is"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		# create a bullet rect at (0,0), then set its location
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
		   ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# store bullet location with float
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		
		
		
		
		
