import obd
obd.logger.setLevel(obd.logging.DEBUG)
print(obd.__path__)
#ports = obd.scan_serial()       # return list of valid USB or RF ports
#print(ports)
connection = obd.OBD(portstr="COM3") # auto-connects to USB or RF port

cmd = obd.commands.SPEED # select an OBD command (sensor)

while True:
    response = connection.query(cmd) # send the command, and parse the response
    #ports = obd.scan_serial()
    #print(ports)
    print(response.value) # returns unit-bearing values thanks to Pint
    print(response.value.to("mph")) # user-friendly unit conversions
connection.close()