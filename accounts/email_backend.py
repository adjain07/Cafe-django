import sib_api_v3_sdk

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class BrevoEmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key["api-key"] = settings.BREVO_API_KEY

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )

        sent_count = 0

        for message in email_messages:
            try:
                sender = sib_api_v3_sdk.SendSmtpEmailSender(
                email=message.from_email or settings.DEFAULT_FROM_EMAIL
                )

                recipients = [
                    sib_api_v3_sdk.SendSmtpEmailTo(
                        email=recipient
                    )
                    for recipient in message.to
                ]

                email_data = sib_api_v3_sdk.SendSmtpEmail(
                    sender=sender,
                    to=recipients,
                    subject=message.subject,
                    text_content=message.body,
                )

                api_instance.send_transac_email(email_data)

                sent_count += 1

            except Exception:
                if not self.fail_silently:
                    raise

        return sent_count

