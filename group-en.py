# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
yinmo = LINE()
for inv in yinmo.getGroupIdsInvited():
    sleep(0.5)
    yinmo.rejectGroupInvitation(inv)
    print("Reject " + yinmo.getGroup(inv).name)
for groups in yinmo.getGroupIdsJoined():
    sleep(0.5)
    yinmo.leaveGroup(groups)
    print("Leave " + yinmo.getGroup(groups).name)
    
