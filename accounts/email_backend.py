import resend

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMultiAlternatives


class ResendEmailBackend(BaseEmailBackend):

    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently, **kwargs)

        resend.api_key = settings.RESEND_API_KEY

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        sent_count = 0

        for message in email_messages:
            try:
                params = {
                    "from": message.from_email or settings.DEFAULT_FROM_EMAIL,
                    "to": message.to,
                    "subject": message.subject,
                    "text": message.body,
                }

                # HTML alternative ho to Resend ko HTML bhi bhejo
                if isinstance(message, EmailMultiAlternatives):
                    for alternative, mimetype in message.alternatives:
                        if mimetype == "text/html":
                            params["html"] = alternative
                            break

                resend.Emails.send(params)

                sent_count += 1

            except Exception:
                if not self.fail_silently:
                    raise

        return sent_count