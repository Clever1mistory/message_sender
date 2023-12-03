from django.db import models


class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    message_text = models.TextField()
    client_filter_operator_code = models.CharField(max_length=10)
    client_filter_tag = models.CharField(max_length=255)
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, unique=True)
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_number


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
