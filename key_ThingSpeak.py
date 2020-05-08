# LoRa test channel
_def_thingspeak_channel_key='FMWF1AMW6SMOBD5Q'

#Note how we can indicate a device source addr that are allowed to use the script
#Use decimal between 2-255 and use 4-byte hex format for LoRaWAN devAddr
#leave empty to allow all devices
source_list=[ "7" ]

key_association=[ ('1QBNQ62FTEQWW3X7',7) ]
# node 8 and 9 will use channel AAAAAAAAAAAAAAAA
# node 10 and 11 will use channel BBBBBBBBBBBBBBBB
# other nodes will use default channel

field_association=[ (7,1) ]
# [(6,1),(7,5)] means data from respectively sensor 6/7 will use starting field index of 1/5
#field_association=[(6,1),(7,5)

nomenclature_association=[ ("T1",0), ("T2",1), ("T3",2), ("T4",3), ("H1",4), ("H2",5), ("H3",6), ("IC",7) ]
# ("TC",0) means that if nomemclature is "TC" then the offset for field index will be 0
# nomenclature_association=[("TC",0),("HU",1),("LU",2),("CO2",3)]
