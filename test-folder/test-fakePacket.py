import sys

#regular data packet from device 6, without appkey
#payload is \!TC/22.5
print "^p1,16,6,86,11,5,-24"
print "^r125,5,7"
print "^t2018-05-09T15:17:50.123"
print "\xFF\xFE\!##TC/22.5"

sys.stdout.flush()
