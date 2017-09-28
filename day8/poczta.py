"""Prosty klient pocztowy
    Uwaga! Tylko znaki ASCII"""

import smtplib
from day8 import secrets

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

# tworze silnik mailera
mailer = smtplib.SMTP("smtp.gmail.com", 587)
# witam sie z serwerem / łącze się
mailer.ehlo()
# szyfruje połączenie
mailer.starttls()
# loguje się
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Arek\n"
wiadomosc = "To jest moja wiadomosc"
tresc = temat + wiadomosc

# wysyłam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila!")

mailer.close()
