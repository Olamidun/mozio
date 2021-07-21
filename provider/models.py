# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Create your models here.


# class ProviderManager(BaseUserManager):
#     def create_user(self, email, name, phone_number, language, currency, username=None, password=None):
#         if email is None:
#             raise TypeError("Email Address is compulsory")
#         if name is None:
#             raise TypeError("Name is compulsory")
#         if phone_number is None:
#             raise TypeError("Phone_number is compulsory")
#         if language is None:
#             raise TypeError("Language is compulsory")
#         if currency is None:
#             raise TypeError("currency is compulsory")

#         user = self.model(
#             name=name,
#             phone_number=phone_number,
#             language=language,
#             currency=currency,
#             email=self.normalize_email(email)
#             )
        
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

    
#     def create_superuser(self, name, email, language, currency, phone_number, password):
#         user = self.create_user(email, name, phone_number, currency, language, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.is_admin = True
#         user.is_verified = True
#         user.save(using=self._db)
#         return user


# class Provider(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     phone_number = models.CharField(max_length=15)
#     language = models.CharField(max_length=30)
#     currency = models.CharField(max_length=20)
#     is_verified = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'phone_number', 'language', 'currency']

#     objects = ProviderManager()

#     def __str__(self):
#         return self.email