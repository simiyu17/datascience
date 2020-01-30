# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:50:12 2020

@author: simiyu
"""

from twilio.rest import Client
from string import Template
import pandas as pd


def get_sms_recipients(file_path):
    names = []
    rec_number = []
    data = pd.read_excel(file_path)
    for index, row in data.iterrows():
        names.append(row['Name'])
        rec_number.append(row['SMS Number'])
    return names, rec_number

def parse_template(file_name):
    with open(file_name, 'r', encoding='utf-8') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)

def main():
    names, rec_numbers = get_sms_recipients('recipients.xlsx')
    message_template = parse_template('sms_template.txt')

    # Your Account SID from twilio.com/console
    account_sid = "AC2f5b389596543bf0efde9087b323c09b"
    # Your Auth Token from twilio.com/console
    auth_token  = "your_auth_token"

    client = Client(account_sid, auth_token)

    # Get each user detail and send the email:
    for name, sms_num in zip(names, rec_numbers):
        # add in the actual person name to the message template
        sms_message = message_template.substitute(NAME=name.title())

        # Prints out the message body for our sake
        print(sms_message)

        print(sms_num)

        message = client.messages.create(
            to='+'+str(sms_num),
            from_="+********************",
            body=sms_message)
        print(message.sid)


if __name__ == '__main__':
    main()