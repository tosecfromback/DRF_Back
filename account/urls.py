from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # account/
    path('', views.Index.as_view(), name='index'),
    # 회원가입
    path('signin/',views.SignIn.as_view(), name='signin'),
    # 로그인
    path('login/', views.Login.as_view(), name='login'),
    # 로그아웃
    path('', views.Logout.as_view(), name='logout'),
    # 상세프로필
    path('username/profile/', views.Profile_Detail.as_view(), name='profile'),
    # 프로필수정
    path('username/profile/update/', views.Profile_Update.as_view(), name='update'),
    # 비밀번호변경
    path('passchng/', views.PassChange.as_view(), name='passchng'),
    # 회원탈퇴
    path('signout/', views.SignOut.as_view(), name='signout'),
]