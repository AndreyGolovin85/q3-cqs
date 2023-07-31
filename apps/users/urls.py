from django.urls import path

from users.views import RegistrationView

urlpatterns = [
    path('user/create/', RegistrationView.as_view(), name='user_create'),
]

