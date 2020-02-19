# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:24:14 2020

@author: simiyu
"""

import imaplib
import email

def read(username, password, sender_of_interest=None):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')
    # Use search(), not status()
    # Print all unread messages from a certain sender of interest
    if sender_of_interest:
        status, response = imap.uid('search', None, 'UNSEEN', 'FROM {0}'.format(sender_of_interest))
    else:
        status, response = imap.uid('search', None, 'UNSEEN')
    if status == 'OK':
        unread_msg_nums = response[0].split()
    else:
        unread_msg_nums = []
    data_list = []
    for e_id in unread_msg_nums:
        data_dict = {}
        e_id = e_id.decode('utf-8')
        _, response = imap.uid('fetch', e_id, '(RFC822)')
        html = response[0][1].decode('utf-8')
       # email_message = email.message_from_string(html)
        email_message = email.message_from_bytes(html)
        data_dict['mail_to'] = email_message['To']
        data_dict['mail_subject'] = email_message['Subject']
        data_dict['mail_from'] = email.utils.parseaddr(email_message['From'])

        if email_message.is_multipart():
                data_dict['body'] = ''

                # on multipart we have the text message and
                # another things like annex, and html version
                # of the message, in that case we loop through
                # the email payload
                for part in email_message.get_payload():
                    # if the content type is text/plain
                    # we extract it
                    if part.get_content_type() == 'text/plain':
                        data_dict['body'] += part.get_payload()
        else:
            # if the message isn't multipart, just extract it
            data_dict['body'] = email_message.get_payload()


        data_list.append(data_dict)
    print(data_list)


def main():
    read('**********@gmail.com', 'password***************')


if __name__ == '__main__':
    main()
