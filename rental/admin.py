from django.contrib import admin
from .models import Rental

@admin.action(description='반납으로 표시')
def mark_as_returned(modeladmin, request, queryset):
    queryset.delete()

class RentalAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'class_number', 'student_number')
    actions = [mark_as_returned]

admin.site.register(Rental, RentalAdmin)
