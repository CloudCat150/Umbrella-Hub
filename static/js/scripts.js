document.getElementById('rentalForm').addEventListener('submit', function(event) {
    event.preventDefault();
    document.getElementById('formMessage').textContent = "등록이 완료되었습니다!";
    document.getElementById('formMessage').classList.remove('hidden');
});
