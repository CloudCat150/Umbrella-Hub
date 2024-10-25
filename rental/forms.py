# forms.py

from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['name', 'grade', 'class_number', 'student_number', 'phone_number']
        labels = {
            'name': '이름',
            'grade': '학년',
            'class_number': '반',
            'student_number': '번호',
            'phone_number': '전화번호',
        }
