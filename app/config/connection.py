from mongoengine import connect, disconnect
from app.config.settings import settings


connect_mongo = connect(settings.mongo_database, host=settings.mongo_url)
disconnect_mongo = disconnect

def on_application_startup():
    connect_mongo()

def on_application_shutdown():
    disconnect_mongo()