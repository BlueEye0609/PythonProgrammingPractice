#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ship.py
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

class Ship():
	
	def __init__(self, ai_settings, screen):
		"""init ship and init its location"""
		self.screen = screen
		self.ai_settings = ai_settings
		
		# load ship pic and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# put new ship at the center bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		
		# move sign
		self.moving_right = False
		self.moving_left  = False
		
	def update(self):
		"""update ship location"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		self.rect.centerx = self.center
		
	def blitme(self):
		"""blit ship in specific location"""
		self.screen.blit(self.image, self.rect)
		
		
		
