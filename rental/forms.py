from django import forms
from .models import Rental
from django.utils import timezone
from datetime import timedelta

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['name', 'grade', 'class_number', 'student_number', 'phone_number']

    def save(self, commit=True):
        rental = super().save(commit=False)
        rental.return_date = timezone.now() + timedelta(days=5)  # 5일 후 반납일 설정
        if commit:
            rental.save()
        return rental
