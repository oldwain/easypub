from multiprocessing.connection import Client

def sendmail(subj, msg):
    address = ('localhost', 6002)

    with Client(address, authkey=b'mail_auth_key') as conn:
        mail = dict()
        mail['subj'] = subj
        mail['msg'] = msg

        conn.send(mail)

