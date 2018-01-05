#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_survey.py
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
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	def setUp(self):
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Chinese', 'Spanish']
	
	def test_store_single_response(self):
		
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
		
	def test_store_responses(self):
		
		for response in self.responses:
			self.my_survey.store_response(response)
			
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
		
		
		
unittest.main()
