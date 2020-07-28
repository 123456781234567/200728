# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:41:44 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"I love","Minecraft","and Python")