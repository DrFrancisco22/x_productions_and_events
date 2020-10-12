from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Visitors(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('TI', 'tarjeta de identidad'),
        ('CC', 'cedula de ciudadania'),
        ('CE', 'cedula extranjera'),
    ]

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE_CHOICES)
    document_id = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
