
from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.TextField()

    def __str__(self):
        return self.name

class CheckoutLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(default=timezone.now)
    return_time = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.TextField()
    return_condition = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.employee} - Checked out: {self.checkout_time}"

    def check_in(self):
        self.return_time = timezone.now()
        self.save()
