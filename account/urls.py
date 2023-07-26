from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # account/
    path('', views.Index.as_view(), name='logIndex'),
    # 로그인
    # 회원가입
    # 로그아웃
    # 프로필보기
    # 프로필수정
]