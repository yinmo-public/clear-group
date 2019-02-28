# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
for inv in yinmo.getGroupIdsInvited():
    yinmo.rejectGroupInvitation(inv)
    print("reject "+inv)
for groups in yinmo.getGroupIdsJoined():
    yinmo.leaveGroup(groups)
    print("leave "+groups)