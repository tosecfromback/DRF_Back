from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # account/
    path('', views.Index.as_view(), name='logIndex'),
    # 로그인
    path('login/', views.Login.as_view(), name='login'),
    # 회원가입
    path('signup/', views.Signup.as_view(), name='signup'),
    # 로그아웃
    path('logout/', views.Logout.as_view(), name='logout'),
    # 프로필보기
    path('profile/<str:pk>/', views.ProfileDetail.as_view(), name='profile'),
    # 프로필수정
    path('profile/<str:pk>/update/', views.ProfileUpdate.as_view(), name='profileUp'),
]