# Enviando E-mails STMP com Python

import os
from dotenv import load_dotenv
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula303.html'

# dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL','')
destinatario = remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL','')
smtp_password = os.getenv('EMAIL_PASSWORD', '')


# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Pedro')


# Transformar nossa mensagem em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Enviando o email

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')