from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, login_id, nickname, password, is_staff, is_superuser, daily_post, **extra_fields):
        now = timezone.localtime()
        # if not email:
        #     raise ValueError('User must have an email!')
        # email = self.normalize_email(email)
        user = self.model(
            login_id = login_id,
            nickname = nickname,
            is_active = True,
            is_staff = is_staff,
            is_superuser = is_superuser,
            date_joined = now,
            last_login = now,
            daily_post = daily_post,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    #create_user
    def create_user(self, login_id, nickname, password, **extra_fields):
        return self._create_user(login_id, nickname, password, False, False, 0, **extra_fields)
    #create_superuser
    def create_superuser(self, login_id, nickname, password, **extra_fields):
        return self._create_user(login_id, nickname, password, True, True, 0, **extra_fields)
    

class User(AbstractUser):
    login_id = models.CharField(unique=True, max_length=25)
    nickname = models.CharField(unique=True, max_length=155)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    daily_post = models.IntegerField(default=0)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.nickname

