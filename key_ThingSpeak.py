# LoRa test channel
_def_thingspeak_channel_key='FMWF1AMW6SMOBD5Q'

#Note how we can indicate a device source addr that are allowed to use the script
#Use decimal between 2-255 and use 4-byte hex format for LoRaWAN devAddr
#leave empty to allow all devices
#source_list=["6", "7", "01020304"]
source_list=[ "2", "6", "5" ]

key_association=[ ('FMWF1AMW6SMOBD5Q',6), ('FMWF1AMW6SMOBD5Q',2), ('ZCA3JG5VCSFD43R0',5) ]
# key_association=[('AAAAAAAAAAAAAAAA', 8, 9), ('BBBBBBBBBBBBBBBB', 10, 11)]
# node 8 and 9 will use channel AAAAAAAAAAAAAAAA
# node 10 and 11 will use channel BBBBBBBBBBBBBBBB
# other nodes will use default channel

field_association=[ (2,1), (6,4), (5,1) ]
# [(6,1),(7,5)] means data from respectively sensor 6/7 will use starting field index of 1/5
#field_association=[(6,1),(7,5)

nomenclature_association=[ ("T1",0), ("T2",1), ("T0",2), ("P0",4), ("HU",5), ("LT",4), ("LN",5), ("DT",8), ("TM",8), ("BT0", 5), ("IC0", 8), ("BT", 3), ("IC", 4) ]
# ("TC",0) means that if nomemclature is "TC" then the offset for field index will be 0
# nomenclature_association=[("TC",0),("HU",1),("LU",2),("CO2",3)]
