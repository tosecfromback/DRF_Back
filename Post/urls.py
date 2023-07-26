from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # post
    # 질의응답 리스트
    path('', views.PostList.as_view(), name='list'),
    # 질의응답 반응
    # 질의응답 댓글
    # 질의응답 대댓글
    # 질의응답 수정
    # 질의응답 삭제
]