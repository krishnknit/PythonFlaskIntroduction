import os
basedir = os.path.abspath(os.path.dirname(__file__))

# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xfb\xa5\xc0\xe3\xf4\xc2\xa8"z\x8d\x8d|:\xd5VPg7\x01\x13;\x97%\xbb'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False