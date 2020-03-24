import os
from drf_firebase.authentication import BaseFirebaseAuthentication
from firebase_admin import credentials, initialize_app
from django.contrib.auth import get_user_model
print (os.getcwd())
firebase_creds=credentials.Certificate("./api/flowers-api-271300-firebase-adminsdk-vvixh-95aea2aa48.json")
firebase_app=initialize_app(firebase_creds)

class FirebaseAuthentication(BaseFirebaseAuthentication):
    def get_firebase_app(self):
        return firebase_app

    def get_django_user(self, firebase_user_record):
        try:
            print(firebase_user_record.uid)
            return get_user_model().objects.get(firebase_uid=firebase_user_record.uid)
        except get_user_model().DoesNotExist:
            return get_user_model().objects.create(firebase_uid=firebase_user_record.uid,email=firebase_user_record.email,photo_url=firebase_user_record.photo_url)