#change here for your own firebase url when you have one
firebase_database='https://loraiot-f9e55.firebaseio.com'

#Note how we can indicate a device source addr that are allowed to use the script
#Use decimal between 2-255 and use 4-byte hex format for LoRaWAN devAddr
#leave empty to allow all devices
#source_list=["3", "255", "01020304"]
source_list=[ "6" ]
