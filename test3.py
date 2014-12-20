# coding=utf-8
#from __future__ import unicode_literals


import messaging
import serial

def send_text(number, text, path='/dev/ttyUSB0'):
# encode the SMS
p = messaging.PDU()
# notice how I get the first returned element, this does
# not deal with concatenated SMS.
pdu_length, pdu = p.encode_pdu(number, text)[0]
# open the modem port (assumes Linux)
ser = serial.Serial(path, timeout=1)
# write the PDU length and wait 1 second till the
# prompt appears (a more robust implementation
# would wait till the prompt appeared)
ser.write('AT+CMGS=%d\r' % pdu_length)
print ser.readlines()
# write the PDU and send a Ctrl+z escape
ser.write('%s\x1a' % pdu)
ser.close()








