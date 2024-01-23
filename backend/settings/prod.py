import os
import dj_database_url

from .base import *


DATABASES = {
    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
