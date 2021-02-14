import win32com.client as win32

def _parse(args):
    recipients = args.get('--recipients', '')
    cc = args.get('--cc', '')
    bcc = args.get('--bcc', '')
    subject = args.get('--subject', '')
    body = args.get('--body', '')
    attachments = args.get('--attachments', '')
    return [recipients, cc, bcc, subject, body, attachments]

def _send_to(df, recipients, cc, bcc, subject, body, attachments):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipients
    if cc:
        mail.CC = cc
    if bcc:
        mail.BCC = bcc
    mail.Subject = subject
    mail.Body = body
    #mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    for a in attachments:
        mail.Attachments.Add(a)

    mail.Send()

    return df

name = 'send-email'

def operator(df, args):
    return _send_to(None, *_parse(args))

if __name__ == '__main__':
    operator(None, {
        '--recipients' : 'founders@digolds.cn;service@digolds.cn',
        '--cc' : 'founders@digolds.cn;service@digolds.cn',
        '--bcc': 'founders@digolds.cn;service@digolds.cn',
        '--subject' : 'My Great Subject',
        '--body' : 'My Great Body',
        '--attachments' : ['file1.xlsx', 'file2.pptx']
    })