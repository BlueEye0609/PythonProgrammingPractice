#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dgp.py
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

# Year 2016 GDP
#0 Country Name
#1 Country Code
#2 Year
#3 Value

import csv
import pygal
from country_codes import get_country_code

# prepare json data of GDP for year 2016
filename = 'gdp_csv.csv'
with open(filename) as f:
	reader = csv.reader(f) 
	reader_now = next(reader)
	
	country_gdps = {}
	
	for row in reader:
		if row[2] == '2016':
			country_name = row[0]
			gdp  = int(float(row[3]))
			code = get_country_code(country_name)
			
			if code:
				country_gdps[code] = gdp
				
cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in country_gdps.items():
	if gdp < 1e+10:
		cc_gdps_1[cc] = gdp	
	elif gdp < 1e+13:
		cc_gdps_2[cc] = gdp
	else:
		cc_gdps_3[cc] = gdp				
	
print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))
		
wm = pygal.maps.world.World()
wm.title = "World GDP in 2016, by Country"
wm.add('<1e+10', cc_gdps_1)
wm.add('1e+10 - 1e+13', cc_gdps_2)
wm.add('>1e+13', cc_gdps_3)

wm.render_to_file('world_gdps.svg')
