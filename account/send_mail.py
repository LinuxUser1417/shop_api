from django.core.mail import send_mail

HOST = 'localhost:8000'


def send_confirmation_email(user, code):
    dev_link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n{dev_link}'
        f'\nСссылка работает один раз!',
        'iskenderhot@gmail.com',
        [user],
        fail_silently=False,
    )
