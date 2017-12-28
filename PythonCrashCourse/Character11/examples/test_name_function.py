#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_name_function.py
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

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""test name_function.py"""
	
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis', 'jpplin')
		self.assertEqual(formatted_name, 'Janis Jpplin')
		
unittest.main()
