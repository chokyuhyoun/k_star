# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:33:43 2022

@author: choky
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import csv
from glob import glob
from mylib import misc


path = r'C:\Users\choky\Desktop\k_star'
os.chdir(path)
f = glob(path+r'/simbad.tsv')

star_list = []
with open(f[0], newline = '') as simbad:                                                                                          
   	lists = csv.reader(simbad, delimiter='\t')
   	for dum in lists:
   		star_list.append(dum)
#%%
name, typ, ra, dec, ecl_lon, ecl_lat, mag_u, sptype \
    = [], [], [], [], [], [], [], []
for i, star in enumerate(star_list[10:-3]):
    name.append(star[1])
    typ.append(star[2])
    dum = star[3].split(' ')
    ra.append(float(dum[0]))
    dec.append(float(dum[1]))
    dum = star[5].split(' ')
    ecl_lon.append(float(dum[0]))
    ecl_lat.append(float(dum[1]))
    if type(star[6]) is str : star[6] = 0.
    mag_u.append(float(star[6]))
    sptype.append(star[11])

ra = np.array(ra)
dec = np.array(dec)
ecl_lon = np.array(ecl_lon)
ecl_lat = np.array(ecl_lat)

fig1, ax1 = plt.subplots()
p01 = ax1.plot(ecl_lon, ecl_lat, '.')
near = np.where(ecl_lat <= 21./60.)



