from config.settings.base import *

ENV_PATH = os.path.join(BASE_DIR, '.envs/.development')
env.read_env(ENV_PATH)

DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', cast=str)
DATABASES['default'] = env.db()
