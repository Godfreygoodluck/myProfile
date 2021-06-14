from django.db import models

# Create your models here.


# recieving messages and mail links to contact clients from
class ClientsMessage(models.Model):
    name = models.CharField(max_length=60)
    from_email = models.EmailField()
    subject = models.CharField(max_length=60, blank=True)
    message = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

class Number(models.Model):
    num = models.ForeignKey('ClientsMessage', on_delete=models.CASCADE)