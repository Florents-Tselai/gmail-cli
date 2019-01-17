from argparse import ArgumentParser
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from pathlib import Path


def send_email(receiver_email, subject, body,
               sender_email='florents.tselai@gmail.com',
               attachments=None, bcc=None):
    try:
        password = environ['GMAIL_PASSWORD']
    except KeyError:
        raise KeyError("You should set the GMAIL_PASSWORD environment variable!")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = bcc

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    if attachments:

        for filename in attachments:
            # Open PDF file in binary mode
            with open(filename, "rb") as att:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(att.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename.name}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def main():
    from argparse import ArgumentParser
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-f', '--sender', help='Gmail address to send from')
    arg_parser.add_argument('-t', '--to', help='Send email to this address')
    arg_parser.add_argument('-s', '--subject', help='Subject Text')
    arg_parser.add_argument('-b', '--body', help='Body Text')
    arg_parser.add_argument('-a', '--attachments', nargs='*', help='Paths to attachment files', default=[])
    args = arg_parser.parse_args()

    if args.attachments:
        args.attachments = map(Path, args.attachments)
    send_email(receiver_email=args.to,
               subject=args.subject,
               body=args.body,
               sender_email=args.sender,
               attachments=args.attachments
               )


if __name__ == '__main__':
    main()
