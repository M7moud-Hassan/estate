# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class Resources(models.Model):
#     name_rsource=models.CharField(max_length=100)

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=30, unique=True)
#     name = models.CharField(max_length=30)  # Add a "name" field
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'