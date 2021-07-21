from .models import User 
from django.conf import settings

# requires to define two functions authenticate and get_user

class PasswordlessAuthentication:  

    def authenticate(self, request, email=None):
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
    
