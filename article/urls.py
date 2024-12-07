from django.urls import path
from .views import Article_list_view,Article_Delete_view,Article_edit_view,Article_detail_view,Article_create_view

urlpatterns = [
    path('articles',Article_list_view.as_view(),name='article_list'),
    path('articles/edit/<int:pk>',Article_edit_view.as_view(),name='article_edit'),
    path('article/delete/<int:pk>',Article_Delete_view.as_view(),name='article_delete'),
    path('article/<int:pk>',Article_detail_view.as_view(),name='article_detail'),
    path('new/',Article_create_view.as_view(),name='article_new')
]