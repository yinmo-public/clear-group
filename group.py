# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
for inv in yinmo.getGroupIdsInvited():
    yinmo.rejectGroupInvitation(inv)   #拒絕群組邀請
    print("Reject " + yinmo.getGroup(inv).name)
for groups in yinmo.getGroupIdsJoined():
    yinmo.leaveGroup(groups)   #退出群組
    print("Leave " + yinmo.getGroup(groups).name)