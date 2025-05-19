from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse


def send_html_email(subject,from_email,to_email,verification_code,username):
    subject = subject
    from_email = from_email
    to = [to_email]

    verification_link = "https://mbm.uz/verify?code=928341"

    text_content = f"Tasdiqlash kodingiz: {verification_code}"
    html_content = f"""
       <div style="font-family: Arial, sans-serif; background-color: #f5f5f5; padding: 20px;">
         <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); padding: 30px;">
           <h2 style="color: #2c3e50;">Assalomu alaykum!</h2>
           <p>Quyidagi sizning <strong>tasdiqlash kodingiz:</strong></p>
           <div style="font-size: 28px; font-weight: bold; color: #27ae60; margin: 20px 0;">{verification_code}</div>

           <p style="font-size: 15px; color: #444;">Yuqoridagi kodni saytimizga kiriting yoki quyidagi tugmani bosing:</p>

           <a href="http://127.0.0.1:8000/avto/change/?name={username}" style="display: inline-block; padding: 12px 24px; font-size: 16px; background-color: #2980b9; color: #ffffff; text-decoration: none; border-radius: 5px; margin-top: 20px;">✅ Kodni tasdiqlash</a>

           <p style="font-size: 14px; color: #777; margin-top: 30px;">Agar siz bu so‘rovni yubormagan bo‘lsangiz, iltimos, e'tibor bermang.</p>

           <hr style="margin-top: 30px;">
           <p style="font-size: 12px; color: #aaa;">MBM Company — Dasturiy yechimlar markazi</p>
         </div>
       </div>
       """

    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse("✅ HTML formatdagi email yuborildi.")