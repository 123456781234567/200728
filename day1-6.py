# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:15:15 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x+1,y,z,213)
mc.setBlock(x-1,y,z,213)
mc.setBlock(x,y,z+1,213)
mc.setBlock(x,y,z-1,213)
mc.setBlock(x+1,y,z+1,213)
mc.setBlock(x+1,y,z-1,213)
mc.setBlock(x-1,y,z-1,213)
mc.setBlock(x-1,y,z+1,213)