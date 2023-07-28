from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # post/
    # 질의응답 리스트
    path('', views.PostList.as_view(), name='index'),
    # 질의응답 검색
    path('search/keyword/', views.PostSearch.as_view(), name='search'),
    # 질의응답 상세내역
    path('detail/', views.PostDetail.as_view(), name='detail'),
]