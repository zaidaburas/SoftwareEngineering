from django.db import models

# Create your models here.

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField(default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    hire_date = models.DateField()
    start_time = models.TimeField()
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
