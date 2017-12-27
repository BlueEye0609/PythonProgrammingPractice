#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5-10.py
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

current_users = ['admin', 'yejing', 'ning', 'Sophie', 'jia jun']
new_users = ['yejing', 'sophie', 'nengjing', 'junyao', 'xiaohui']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Name " + new_user + " already been used. please choose another name.")
	else:
		print("Name " + new_user + " hasn't been used.")
