# auto_unsunbscriber.py - goes trough all emails in the inbox and looks for any unsubscribe button.
# For each of them opens separated web browser tab with the unsubscribe link.

import imapclient, pyzmail


def check_for_email():
    mails = imapclient.IMAPClient('imap.wp.pl', ssl=True)
    mails.login('', '')
    mails.select_folder('INBOX', readonly=True)
    raw_mails = mails.search(['BODY unsubscribe'])
    for mail in raw_mails:
        raw_mail = raw_mails.fetch(mail, ['BODY', 'FLAGS'])
        print(raw_mail.html_part.get_payload().decode(mail.html_part.charset))

check_for_email()
