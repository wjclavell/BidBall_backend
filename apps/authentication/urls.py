from django.conf.urls import url
from apps.authentication.views import RegistrationAPIView, LoginAPIView, SingleUser

urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
    url(r'^users/profile/$', SingleUser.as_view(), name='single_user')
]
