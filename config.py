import os
CSRF_ENABLED = True
SECRET_KEY = os.environ.get('DOPE_SECRET_KEY')
basedir = os.path.abspath(os.path.dirname(__file__))
baseurl = os.environ.get('DOPE_BASE_URL', None)
SQLALCHEMY_DATABASE_URI = os.environ.get('DOPE_DATABASE_URL',
                                         os.environ.get('DATABASE_URL', 
                                                        'postgresql+psycopg2://postgres@localhost:5432/hintofdope'))
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_ACC')
