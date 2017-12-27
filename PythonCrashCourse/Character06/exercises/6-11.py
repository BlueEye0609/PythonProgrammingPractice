#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  6-11.py
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

cities = {
    'shanghai': {
        'country': 'china',
        'population': '10000w',
        'fact': 'famous city',
    },
    'new york': {
        'country': 'america',
        'population': '150W',
        'fact': 'dangerous but beautiful'
    }
}

for city, city_info in cities.items():
	print("\nCityname: " + city)
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']
	
	print("\tCountry: " + country.title())
	print("\tPopulation: " + population)
	print("\tfact: " + fact)
