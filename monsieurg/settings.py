#coding:utf8
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
"""
Django settings for monsieurg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q5=2kx4z3)o#$5(d4hy5qt3r(!7a!l4t679vv#p9@r_@x!^il#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.monsieurg.fr',
]


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',

)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'theme.processor.getPublishedThemeBackground',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)


ROOT_URLCONF = 'monsieurg.urls'

WSGI_APPLICATION = 'monsieurg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'monsieur_g',
        'USER': 'jazdelu',
	'PASSWORD':'lushizhao1129',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = '/u/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'u/')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)


# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Monsieur G Website Manager',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU':(
        {'app':'auth','label':u'用户管理','icon':'icon-user'},
        {'app':'theme','label':u'礼盒主题管理','icon':'icon-gift'},
        {'app':'product','label':u'礼盒单品管理','icon':'icon-shopping-cart'},
    ),
    # 'SEARCH_URL': '/admin/auth/user/',

    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),


    # misc
    'LIST_PER_PAGE': 10
}


