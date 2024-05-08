from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, ResponseView, ResponseList

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('responses/', ResponseList.as_view(), name='responses'),
    path('<int:pk>/response/', ResponseView.as_view(), name='response'),

   ]