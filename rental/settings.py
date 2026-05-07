import os
from pathlib import Path

# 1. 경로 설정: C#의 BaseDirectory와 같습니다.
# 파일 위치가 바뀌었으므로 상위 폴더 구조를 잘 잡아야 합니다.
BASE_DIR = Path(__file__).resolve().parent.parent

# 보안 키 (실제 배포 시에는 환경변수로 분리하는 것이 좋습니다)
SECRET_KEY = 'django-insecure-ssnb1uqdl(vx!-qu7rjh-50@(8z%n8=3*daulqql34qy=j&@t%'

DEBUG = True

# 허용할 호스트 (C#의 CORS 설정과 유사)
ALLOWED_HOSTS = ['umbrella-hub.onrender.com', 'localhost', '127.0.0.1']


# 2. 애플리케이션 정의
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rental',  # 메인 모듈 등록
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 3. 중요!! 라우팅 설정 변경
# 기존 umbrella_hub.urls 에서 rental.urls 로 변경합니다.
ROOT_URLCONF = 'rental.urls' 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # 공통 템플릿 폴더 지정
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 4. 서버 통신 설정 변경
WSGI_APPLICATION = 'rental.wsgi.application'


# 5. Database (SQLite 사용)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 나머지 설정 (비밀번호 검증, 로깅 등)은 그대로 유지해도 무방합니다.
LANGUAGE_CODE = 'ko-kr' # 한국어로 변경
TIME_ZONE = 'Asia/Seoul' # 한국 시간으로 변경
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
