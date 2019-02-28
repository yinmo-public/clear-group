# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
for inv in yinmo.getGroupIdsInvited():
    yinmo.rejectGroupInvitation(inv)
    print("拒絕群組邀請 " + yinmo.getGroup(inv).name)
for groups in yinmo.getGroupIdsJoined():
    yinmo.leaveGroup(groups)
    print("退出群組 " + yinmo.getGroup(groups).name)
    