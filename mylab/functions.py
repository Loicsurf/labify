from django.core.mail import EmailMessage
from django.conf import settings



def emailResultsPatient(to_email, from_client, filepath):
    from_email = settings.EMAIL_HOST_USER
    subject = '[St-Therese] Results Notification'
    body = """
    Good day,

    Please find attached results from {} for your immediate attention.

    regards,
    Hopital Catholique St-Therese
    """.format(from_client)

    message = EmailMessage(subject, body, from_email, [to_email])
    message.attach_file(filepath)
    message.send()
