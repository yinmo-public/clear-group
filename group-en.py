# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
for inv in yinmo.getGroupIdsInvited():
    yinmo.rejectGroupInvitation(inv)
    print("Reject " + yinmo.getGroup(inv).name)
for groups in yinmo.getGroupIdsJoined():
    yinmo.leaveGroup(groups)
    print("Leave " + yinmo.getGroup(groups).name)
    