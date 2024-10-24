from django.contrib import admin
from .models import Rental

@admin.action(description='반납으로 표시')
def mark_as_returned(modeladmin, request, queryset):
    queryset.delete()  # 선택한 대여 항목 삭제 (반납으로 표시)

class RentalAdmin(admin.ModelAdmin):
    # 관리자가 조회할 수 있는 열을 설정
    list_display = ('name', 'grade', 'class_number', 'student_number', 'phone_number', 'rented_at', 'return_date')
    
    # 정렬 기준
    ordering = ('-rented_at',)

    # 필터링
    list_filter = ('grade', 'class_number', 'rented_at')
    
    # 검색 기능
    search_fields = ('name', 'student_number', 'phone_number')

    # 액션 추가
    actions = [mark_as_returned]

# Admin에 모델 등록
admin.site.register(Rental, RentalAdmin)
