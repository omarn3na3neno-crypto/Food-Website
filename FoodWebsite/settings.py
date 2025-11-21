import os
from pathlib import Path

# مسار المشروع الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent


# SECRET_KEY و DEBUG
SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = False  # لازم False على Render

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['foodwebsite.onrender.com']  # عدل الاسم حسب الدومين اللي Render هيديهولك

# لو محتاج تشغل الموقع محلياً كمان نفس الوقت:
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'foodwebsite.onrender.com']


# التطبيقات المثبتة
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu',
    'reservation',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # مهم للستاتيك على Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# قاعدة البيانات (SQLite مؤقتة)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# إعدادات الملفات الثابتة
STATIC_URL = '/static/'

# فولدرات المشروع اللي فيها static محليًا
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "menu" / "static",
]

# فولدر هيتم إنشاءه تلقائيًا بعد collectstatic على Render
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ملفات الميديا
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

ROOT_URLCONF = 'FoodWebsite.urls'


# اللغة والتوقيت
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# نوع الـ primary key الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

