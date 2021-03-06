# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 09:36:40 2010

@author: Ludovic Autin - ludovic.autin@gmail.com
"""
import Blender

#first get epmv
rdict = Blender.Registry.GetKey('mv', False)
epmv = rdict['epmv']

sc=epmv.helper.getCurrentScene()
if epmv.synchro_timeline : 
    traj = epmv.gui.current_traj
    frame = Blender.Get('curframe')
    seconds = int(Blender.Get('curframe')/25.0)+1
    st,ft=epmv.synchro_ratio
    if (frame % ft) == 0:   
        step = frame * st
        epmv.updateData(traj,step)
else :
    #get selected object
    slist = epmv.helper.getCurrentSelection()
    if not slist : 
       #do nothing
       pass
    else :
        for l in slist:
            print(l)
        epmv.updateCoordFromObj(slist,debug=True)
#epmv.helper.update()
