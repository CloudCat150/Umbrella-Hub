# models.py
from django.db import models
from django.utils import timezone
from datetime import timedelta

class Rental(models.Model):
    name = models.CharField(max_length=100)
    class_number = models.CharField(max_length=50)
    student_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    grade = models.CharField(max_length=10, blank=True, null=True)  # 학년 필드 추가
    rented_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.return_date = timezone.now() + timedelta(days=5)  # 자동으로 5일 후 날짜 설정
        super().save(*args, **kwargs)
