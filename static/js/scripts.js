// scripts.js

document.getElementById('rentalForm').addEventListener('submit', function(event) {
    event.preventDefault();  // 기본 제출 방지
    // AJAX 요청 또는 폼 처리 로직 추가 (여기서는 생략)
    
    // 등록 완료 메시지 표시
    document.getElementById('formMessage').textContent = "등록이 완료되었습니다!";
    document.getElementById('formMessage').classList.remove('hidden');
});
