from django.conf import settings
from django.core.mail import send_mail


def send_email(customer, robot):
    """
    Функция отправляет сообщение на электронную почту покупателя.

    """
    # Текст письма
    subject = 'Появился новый робот по вашему запросу'
    html_content = 'Добрый день!\n'
    html_content += f'Недавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}.\n' \
                    f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'
    # Получение почты сервиса и отправка письма покупателю
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject=subject, message=html_content, from_email=email_from, recipient_list=[customer.email],)
