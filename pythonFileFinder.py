import os
from os.path import join

lookfor = "avl"
for root, dirs, files in os.walk('/'):
    #print "searching", root
    if lookfor in files:
        print "found: %s" % join(root, lookfor)
        break
