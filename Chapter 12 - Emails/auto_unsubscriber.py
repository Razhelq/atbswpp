# auto_unsunbscriber.py - goes trough all emails in the inbox and looks for any unsubscribe button.
# For each of them opens separated web browser tab with the unsubscribe link.


import imapclient, pyzmail, re, webbrowser
from datetime import date


def check_for_email():
    imap_obj = imapclient.IMAPClient('imap.wp.pl', ssl=True)
    imap_obj.login('', '')
    imap_obj.select_folder('INBOX', readonly=True)
    UIDs = imap_obj.search([u'SINCE', date(2017, 1, 1)])
    domains = []
    for UID in UIDs:
        raw_mail = imap_obj.fetch([UID], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_mail[UID][b'BODY[]'])
        try:
            mess = message.html_part.get_payload().decode(message.html_part.charset)
            print(mess.get_subject())
            if re.search(r'unsubscribe', mess):
                try:
                    domain = re.search(r'(?<=unsubscribe).*((?<=<a href=\"https://)|(?<=<a href=\"http://))(.+?(?=/))', mess).group(2)
                    if domain not in domains:
                        domains.append(domain)
                        link = re.search(r'(?<=unsubscribe).*(?<=<a href=\")(.+?(?=\"))', mess).group(1)
                        print(link)
                        webbrowser.open(link)
                except:
                    pass
        except:
            pass

check_for_email()
