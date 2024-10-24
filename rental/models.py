from django.db import models
from django.utils import timezone

class Rental(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    class_number = models.IntegerField()
    student_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    return_date = models.DateTimeField()
    rented_at = models.DateTimeField(default=timezone.now)  # 현재 시간으로 기본값 설정

    def __str__(self):
        return self.name
