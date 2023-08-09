
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = 'k1l8gsqp&&glb@%qafi26xb-y4%xjf60g)2!6bspqc+@xjl7me'

DEBUG = True

ALLOWED_HOSTS = ['.vercel.app','.now.sh' ,'127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    'post',
    'crispy_forms',
    'authy',
    'comment',
    'directs',
    'notification',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ig_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ig_prj.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        # 'URL': os.getenv('POSTGRES_URL'),
        # 'NAME': os.getenv('PGNAME'),
        # 'USER': os.getenv('PGUSER'),
        # 'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        # 'HOST': os.getenv('PGHOST'),
        # # 'PORT': os.getenv('PGPORT),
        'URL':"postgres://default:O5mJiAW4FPtD@ep-bitter-forest-20208669-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb",
# POSTGRES_PRISMA_URL="postgres://default:O5mJiAW4FPtD@ep-bitter-forest-20208669-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb?pgbouncer=true&connect_timeout=15",
# POSTGRES_URL_NON_POOLING="postgres://default:O5mJiAW4FPtD@ep-bitter-forest-20208669.us-east-1.postgres.vercel-storage.com:5432/verceldb",
        'USER':"default",
        'HOST':"ep-bitter-forest-20208669-pooler.us-east-1.postgres.vercel-storage.com",
        'PASSWORD':"O5mJiAW4FPtD",
        'NAME':"verceldb",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build','static')



MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = 'sign-in'

LOGIN_URL = 'sign-in'

CRISPY_TEMPLATE_PACK = 'bootstrap4'