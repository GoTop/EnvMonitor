# coding=utf-8
#!/usr/bin/env python

"""\
Demo: handle incoming SMS messages by replying to them

Simple demo app that listens for incoming SMS messages, displays the sender's number
and the messages, then replies to the SMS by saying "thank you"
"""


from __future__ import print_function
import logging

PORT = 'COM1'
BAUDRATE = 115200
PIN = None  # SIM card PIN (if any)

from gsmmodem.modem import GsmModem

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

    modem.write('AT+CMGF=0')
    modem.write('AT+CSCS="UCS2"')
    modem.write('AT+CSMP = 17,167,0,8')
    #modem.write('AT+CMGS=\"+8618978609910\"')


    modem.sendSms("+8618978609910", "你好", waitForDeliveryReport=False, deliveryTimeout=15)
    print('Waiting for SMS message...')
    # try:
    #     modem.rxThread.join(
    #         2 ** 31)  # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    # finally:
    #     modem.close();


if __name__ == '__main__':
    main()




