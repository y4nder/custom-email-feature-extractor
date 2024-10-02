from email import policy
from email.parser import BytesParser

def extract_email_contents(eml_file_path):
    with open(eml_file_path, 'rb') as file:
        # Parse the .eml file
        msg = BytesParser(policy=policy.default).parse(file)

        # Get the email subject
        subject = msg['subject']
        # Get the sender
        sender = msg['from']
        # Get the receiver
        receiver = msg['to']
        # Get the date
        date = msg['date']
        
        # Extract the email body
        if msg.is_multipart():
            # If the email has multiple parts, extract the plain text part
            for part in msg.iter_parts():
                if part.get_content_type() == 'text/plain':
                    body = part.get_content()
                    break
        else:
            # If it's not multipart, extract the body directly
            body = msg.get_content()

    return {
        'subject': subject,
        'from': sender,
        'to': receiver,
        'date': date,
        'body': body
    }

# Example usage
if __name__ == "__main__":
    eml_file_path = 'email.eml'  # Replace with your .eml file path
    email_contents = extract_email_contents(eml_file_path)
    print(email_contents['body'])
