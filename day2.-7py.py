# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:21:23 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


name = input("what is your name")
message = input("Your Messsage: ")

mc.postToChat("["+name+"]"+message)