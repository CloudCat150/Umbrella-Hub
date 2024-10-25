# forms.py

from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['name', 'grade', 'class_number', 'student_number', 'phone_number']
        labels = {
            'name': '이름',              # 'name' 필드를 '이름'으로 레이블 변경
            'grade': '학년',            # 'grade' 필드를 '학년'으로 레이블 변경
            'class_number': '반',       # 'class_number' 필드를 '반'으로 레이블 변경
            'student_number': '번호',    # 'student_number' 필드를 '학번'으로 레이블 변경
            'phone_number': '전화번호',  # 'phone_number' 필드를 '전화번호'로 레이블 변경
        }
