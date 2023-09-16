import maya.cmds as cmds

cmds.select (clear=True)
cmds.select ('aMasterSkel_M:*')
cmds.select ("Handles", add=True, hierarchy=True)


# Keys on animation curves are identified by either
# their time values or their indices.  Times and indices can
# be given as a range or list of ranges.


# time=('10pal','10pal') means the key at frame 10 (PAL format).
# time=[(1.0,1.0),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
# time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
# Omitting one end of a range means "go to infinity", as in the following examples:
# time=(10,) means all keys from time 10 (in the current time unit) onwards.
# time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
# time=() is a short form to specify all keys.
# index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
# index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
# index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

# To replace the animation driven by an ik handle of joints,
# starting from joint1, with separate animCurves, within the
# time interval 5-44, with a sampling frequency of 2 timeUnits,
# use the following command:
#
firstKey = int(cmds.findKeyframe(time=(0, 100000), which='first'))
lastKey = int(cmds.findKeyframe(time=(0, 100000), which='last')) 

cmds.bakeSimulation( 'aMasterSkel_M:Original', t=(firstKey, lastKey), at=["tx","ty","tz","rx","ry","rz"], hi="below" )