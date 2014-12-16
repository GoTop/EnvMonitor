# coding=utf-8
#!/usr/bin/env python

"""\
Demo: handle incoming SMS messages by replying to them

Simple demo app that listens for incoming SMS messages, displays the sender's number
and the messages, then replies to the SMS by saying "thank you"
"""

from __future__ import print_function
import logging

from messaging.sms import SmsSubmit, SmsDeliver
from gsmmodem.modem import GsmModem
import messaging
import serial

PORT = 'COM1'
BAUDRATE = 115200
PIN = None  # SIM card PIN (if any)


def handleSms(sms):
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))
    print('Replying to SMS...')
    sms.reply(u'SMS received: "{0}{1}"'.format(sms.text[:20], '...' if len(sms.text) > 20 else ''))
    print('SMS sent.\n')


def main():
    print('Initializing modem...')
    # Uncomment the following line to see what the modem is doing:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handleSms)
    modem.smsTextMode = False
    modem.connect(PIN)

    number = '+8618978609910'

    #设置发送信息的模式，0表示PDU模式，1表示文本模式
    modem.write('AT+CMGF=0')
    modem.write('AT+CSCS=UCS2')
    #modem.write('AT+CSMP = 17,167,0,8')
    modem.write("AT+CMGS=25",waitForResponse=True, timeout=15, expectedResponseTermSeq=None)
    modem.write('0891683108706705F001000D91688179689019F0000806304253F68449\x1a')




    modem.sendSms("+8618978609910", "你好", waitForDeliveryReport=False, deliveryTimeout=15)
    print('Waiting for SMS message...')
    # try:
    #     modem.rxThread.join(
    #         2 ** 31)  # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    # finally:
    #     modem.close();


def send_text(number, text, path='/dev/ttyUSB0'):
    #
    # # open the modem port (assumes Linux)
    # ser = serial.Serial(path, timeout=1)
    # # write the PDU length and wait 1 second till the
    # # prompt appears (a more robust implementation
    # # would wait till the prompt appeared)
    # ser.write('AT+CMGS=%d\r' % pdu_length)
    # print ser.readlines()
    # # write the PDU and send a Ctrl+z escape
    # ser.write('%s\x1a' % pdu)
    # ser.close()

    number = '+8618978609910'
    text = u'工作愉快!'
    csca = '+8613800776500'
    expected = "0891683108706705F011000D916881796890190F0008000A5DE54F5C61095FEBFF01"

    sms = SmsSubmit(number, text)
    sms.ref = 0x0
    sms.csca = csca
    pdu = sms.to_pdu()[0]
    print(pdu.pdu)


if __name__ == '__main__':
    #main()
    send_text('+8618978609910', 'hey how are you?')
