import logging
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RentalForm
from .models import Rental
from django.contrib import messages
from django.views.generic import ListView  # ListView 임포트 추가

# 로거 설정
logger = logging.getLogger(__name__)

def create_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save()
            logger.info(f"이름: {rental.name}, 반: {rental.class_number}, 번호: {rental.student_number}, 반납일: {rental.return_date}")
            messages.success(request, '대여 등록이 완료되었습니다!')
            return redirect('rental_confirmation', pk=rental.pk)  # 확인 페이지로 리다이렉트
    else:
        form = RentalForm()
    
    return render(request, 'rental/rental_form.html', {'form': form})

def rental_confirmation(request, pk):
    rental = get_object_or_404(Rental, pk=pk)  # 대여 정보 가져오기
    return render(request, 'rental/rental_confirmation.html', {'rental': rental})  # 확인 템플릿 렌더링

class RentalListView(ListView):
    model = Rental
    template_name = 'rental_list.html'  # 사용할 템플릿 파일
    context_object_name = 'rentals'

def mark_as_returned(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    rental.delete()  # 대여 항목 삭제 (반납으로 표시)
    return redirect('rental-list')  # 대여 목록 페이지로 리다이렉트