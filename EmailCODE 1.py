import smtplib
import imaplib
import email

class EmailSystem:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        self.smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp_server.starttls()
        self.smtp_server.login(email_address, password)
        self.imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
        self.imap_server.login(email_address, password)
        self.imap_server.select("inbox")

    def send_email(self, recipient, subject, message):
        email_message = f'Subject: {subject}\n\n{message}'
        self.smtp_server.sendmail(self.email_address, recipient, email_message)
        print("Email sent successfully!")

    def read_emails(self):
        _, email_ids = self.imap_server.search(None, "ALL")
        email_ids = email_ids[0].split()
        emails = []
        for id in email_ids:
            _, email_data = self.imap_server.fetch(id, "(RFC822)")
            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            email_data = {
                "subject": email_message["subject"],
                "from": email_message["from"],
                "date": email_message["date"],
                "body": self.get_email_body(email_message)
            }
            emails.append(email_data)
        return emails

    def get_email_body(self, email_message):
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode("UTF-8")
        else:
            return email_message.get_payload(decode=True).decode("UTF-8")

    def delete_email(self, email_id):
        self.imap_server.store(email_id, "+FLAGS", "\\Deleted")
        self.imap_server.expunge()
        print("Email deleted successfully!")

    def quit(self):
        self.smtp_server.quit()
        self.imap_server.close()
        self.imap_server.logout()

if __name__ == "__main__":
    email_system = EmailSystem("your_email_address@gmail.com", "your_password")
    while True:
        print("\nWhat do you want to do?")
        print("1. Send an email")
        print("2. Read your emails")
        print("3. Delete an email")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            recipient = input("Enter recipient email address: ")
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            email_system.send_email(recipient, subject, message)
        elif choice == 2:
            emails = email_system.read_emails()
            for i, email_data in enumerate(emails):
                print(f"\nEmail {i+1}")
                print(f"Subject: {email_data['subject']}")
                print(f"From: {email_data['from']}")
                print(f"Date: {email_data['date']}")
                print(f"Body: {email_data['body']}")
        elif choice == 3:
            email_id = input("Enter the email ID of the email you want to delete: ")
            email_system.delete_email(email_id)
        elif choice == 4:
            email_system.quit()
            break
        else:
            print("Invalid choice")
