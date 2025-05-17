from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse


def send_html_email(request):
    subject = "MBM company"
    from_email = "sodiqomahkam56@gmail.com"
    to = ["sodiqomahkam56@gmail.com","snappungm@gmail.com",]

    text_content = "Bu oddiy email matni."
    html_content = """
        <h2>Assalomu alaykum!</h2>
        <p>Bu <strong>Yoo</strong> Whassup bro.</p>
        <strong><p style="color:green;">Bugun dars qale boladi</p></strong>
    """

    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse("✅ HTML formatdagi email yuborildi.")
