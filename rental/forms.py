# forms.py
from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['name', 'grade', 'class_number', 'student_number', 'phone_number']  # 학년 필드 추가
