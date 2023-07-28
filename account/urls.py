from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # account/
    path('', views.Index.as_view(), name='index'),
    # 회원가입
    # 로그인
    path('login/', views.Login.as_view(), name='login'),
    # 로그아웃
    # 상세프로필
    # 프로필수정
    # 비밀번호변경
    # 회원탈퇴
]