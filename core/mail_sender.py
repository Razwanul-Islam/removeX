from django.core.mail import send_mail
from mail.models import ContactUsReceiver, ContactMessage
def send_contact_us_notification(name, phone, email, message):
    sender = "info@bodyartgallery.dk"
    recipient = ["razwanrakib0@gmail.com"]
    # Fetch all ContactUsReceiver emails from the database
    receivers = ContactUsReceiver.objects.all()
    if receivers.exists():
        recipient = [receiver.email for receiver in receivers]
    subject = "RemoveX: New Contact Us Message"
    
    body = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                    background-color: #f9f9f9;
                    padding: 20px;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }}
                h2 {{
                    color: #0044cc;
                }}
                p {{
                    font-size: 14px;
                    line-height: 1.6;
                }}
                .contact-details {{
                    background-color: #e9f1ff;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }}
                .message {{
                    background-color: #f7f7f7;
                    padding: 15px;
                    border-radius: 5px;
                    font-size: 14px;
                    color: #555;
                    border: 1px solid #ddd;
                }}
                .footer {{
                    margin-top: 30px;
                    text-align: center;
                    font-size: 12px;
                    color: #999;
                }}
                .footer a {{
                    color: #0044cc;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <h2>New Contact Us Message</h2>
                <p>You have received a new message from the Contact Us form on RemoveX.</p>
                <div class="contact-details">
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Phone:</strong> {phone}</p>
                    <p><strong>Email:</strong> {email}</p>
                </div>
                <div class="message">
                    <p><strong>Message:</strong></p>
                    <p>{message}</p>
                </div>
                <div class="footer">
                    <p>RemoveX.dk All Rights Reserved</p>
                </div>
            </div>
        </body>
    </html>
    """
    try:
        # Save the contact message to the database
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
    except Exception as e:
        print(f"Error saving contact message: {e}")
    
    s = send_mail(subject, body, sender, recipient, html_message=body)
    print(s)