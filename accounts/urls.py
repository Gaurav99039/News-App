from django.urls import path
from .views import SignUpView,custom_logout_view
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('logout/', custom_logout_view, name='logout'),
    path('accounts/password_change',PasswordChangeView.as_view(),name='password_change')
]