#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  11-3.py
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
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
	
	def setUp(self):
		self.employee = Employee('jiajun', 'chen', 9000)
		
	def test_give_default_raise(self):
		newsalary = self.employee.give_raise()
		self.assertEqual(newsalary, 14000)
		
	def test_give_custom_raises(self):
		newsalary = self.employee.give_raise(increase=6000)
		self.assertEqual(newsalary, 15000)
		
unittest.main()
