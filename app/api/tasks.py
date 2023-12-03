from celery import shared_task
import requests
from django.utils import timezone
from .models import Mailing, Client, Message


@shared_task
def send_message_to_external_api(client_filter_operator_code, message_text):
    current_time = timezone.now()
    mailings = Mailing.objects.filter(start_time__lte=current_time, end_time__gte=current_time)

    for mailing in mailings:
        eligible_clients = Client.objects.filter(mobile_operator_code=client_filter_operator_code,
                                                 tag=mailing.client_filter_tag)

        for client in eligible_clients:
            message = Message.objects.create(
                mailing=mailing,
                client=client,
                status='pending'
            )

            url = "https://probe.fbrq.cloud/api/send"
            headers = {
                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzIwOTgxMDEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9QbG9uUXVpIn0.Eoj8DZhyl8DW1f0S5kasyfN157YXXTIytmns75rBJ8g",
                "Content-Type": "application/json"
            }
            data = {
                "phone": client.phone_number,
                "message": message_text
            }

            # Если текущее время находится в интервале рассылки
            if mailing.start_time <= current_time <= mailing.end_time:
                # Отправка запроса к внешнему API
                response = requests.post(url, headers=headers, json=data)

                # Обработка ответа и обновление статуса сообщения
                if response.status_code == 200:
                    message.status = 'sent'
                    message.save()
                else:
                    message.status = 'failed'
                    message.save()

