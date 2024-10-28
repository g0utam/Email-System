# Email System Using Python

This project implements a simple Email System in Python that allows users to send, read, and delete emails. It uses the `smtplib` library for sending emails via the SMTP protocol, and `imaplib` and `email` libraries for accessing and managing emails through IMAP.

## Features

- **Send Email**: Allows users to send an email to any valid recipient.
- **Read Emails**: Fetches and displays emails from the inbox.
- **Delete Email**: Deletes an email by specifying its ID.
- **Quit**: Closes the email session securely.

## Requirements

- Python 3.x
- Gmail account (with "Allow less secure apps" enabled if using non-OAuth)
- Modules: `smtplib`, `imaplib`, and `email` (These are standard libraries in Python)

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.

No additional dependencies are required.

## Usage

### 1. Setup

Replace the placeholder values `"your_email_address@gmail.com"` and `"your_password"` in the main section with your own Gmail credentials.

```python
email_system = EmailSystem("your_email_address@gmail.com", "your_password")
```

### 2. Running the Program

Run the script:

```bash
python email_system.py
```

### 3. Interface Options

After running, you'll see the following menu:

- **1. Send an email**: Prompts you to input recipient email, subject, and message.
- **2. Read your emails**: Displays the subject, sender, date, and body of each email in your inbox.
- **3. Delete an email**: Prompts you to enter the ID of the email you want to delete.
- **4. Quit**: Closes the SMTP and IMAP connections.

## Code Overview

### `EmailSystem` Class

- **`__init__`**: Initializes the email session and logs into the SMTP and IMAP servers.
- **`send_email`**: Sends an email using the provided recipient, subject, and message.
- **`read_emails`**: Retrieves and displays all emails from the inbox.
- **`get_email_body`**: Extracts the body of an email message.
- **`delete_email`**: Marks an email as deleted on the server and expunges it.
- **`quit`**: Closes and logs out from SMTP and IMAP servers.

## Note

This code currently only supports Gmail accounts and basic authentication with email and password. Using application-specific passwords or OAuth2 is recommended for added security.
