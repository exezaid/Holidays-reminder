#! /usr/bin/env python
# -*- coding: utf8 -*-

import datetime
import sqlite3
import smtplib
import mimetypes

from email.MIMEText import MIMEText
from email.Encoders import encode_base64

a = datetime.date.today() + datetime.timedelta(14)
fer = a.strftime('%Y-%m-%d')

mensaje = MIMEText("El feriado del dia " + fer + " esta proximo")
mensaje['Subject'] = "Informe de feriado"

conn = sqlite3.connect('/sitio/holidays.db')
c = conn.cursor()
c.execute("select dia, email from feriados_feriados where dia = (?)", (fer,))
for aviso in c:
    mail = aviso[1]
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("mail","pass")
    mailServer.sendmail("no-reply@gmail.com",
        mail,
        mensaje.as_string())
    mailServer.close()
    print mail
c.close()
