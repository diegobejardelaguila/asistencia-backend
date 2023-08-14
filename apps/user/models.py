
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    
    first_name = models.CharField(max_length=255)
    image_profile = models.ImageField(upload_to='user/profile', blank=True, null=True)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=9, blank=True, null=True)
    dni = models.CharField(len=8, blank=True, null=True)
    img_profile = models.ImageField(upload_to='user/profile', blank=True, null=True)
    expected_entry_time = models.TimeField(blank=True, null=True)
    expected_exit_time = models.TimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'dni', 'expected_entry_time', 'expected_exit_time']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Cuenta de usuario'
        verbose_name_plural = 'Cuentas de usuario'







