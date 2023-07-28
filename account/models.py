from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

    # default User Create
    def _create_user(self, username, password, **extra_fields):
        now = timezone.now()
        # if not email:
        #     raise ValueError('User must have an email!')
        user = self.model(
            username = username,
            # email = self.normalize_email(email),
            joined_date = now,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)
    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, is_staff=True, is_superuser=True, **extra_fields)
        

# User
class User(AbstractBaseUser):
    # login_id          로그인ID
    # email             E-Mail
    # nickname          별명
    # password          비밀번호
    # username          이름 / 초기테스트용으로 다른 명칭 안 씀
    username = models.CharField(unique=True, max_length=155)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # admin 권한 여부    기본 값은 false
    is_superuser = models.BooleanField(default=False)
    # signup_time       가입일자
    joined_date = models.DateTimeField(auto_now_add=True)
    # last_login        마지막 접속시간
    last_login = models.DateTimeField(blank=True, null=True)
    # daily_write       일일 작성 횟수
    daily_post = models.IntegerField(default=0)


