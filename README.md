# Send e-mails through the command line

## Usage
```bash
usage: gmail_cli.py [-h] [-f SENDER] [-t TO] [-s SUBJECT] [-b BODY]
                    [-a [ATTACHMENTS [ATTACHMENTS ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -f SENDER, --sender SENDER
                        Gmail address to send from
  -t TO, --to TO        Send email to this address
  -s SUBJECT, --subject SUBJECT
                        Subject Text
  -b BODY, --body BODY  Body Text
  -a [ATTACHMENTS [ATTACHMENTS ...]], --attachments [ATTACHMENTS [ATTACHMENTS ...]]
                        Paths to attachment files
```

## Examples
```bash
 python gmail_cli.py -f <you-address>@gmail.com -t <any-address@anygsdfg.com> -s test_subject -b test_body -a ~/data.txt
```