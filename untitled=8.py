# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:00:55 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

w = 100
h = 500
l = 100

x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+w,h+w,z+l,46)