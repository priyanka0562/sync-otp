import smtplib
import random
import string

# Generate a random OTP
def generate_otp(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Email configuration (using Gmail SMTP)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'priya2225priyanka@gmail.com'
sender_password = 'dmqr xalj dyii uuyf'  # Use an app-specific password for security

# Generate and send OTP via email
def send_otp_via_email(recipient_email, otp):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        subject = 'Your OTP Verification Code'
        message = f'Your OTP is: {otp}'
        msg = f'Subject: {subject}\n\n{message}'

        server.sendmail(sender_email, recipient_email, msg)
        server.quit()
        print(f"OTP sent successfully to {recipient_email}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("OTP sending failed. Please check your email configuration.")

# Main program
def main():
    recipient_email = input("Enter the recipient's email address: ")

    otp = generate_otp()
    
    send_otp_via_email(recipient_email, otp)

if __name__ == "__main__":
    main()
