from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from getpaid.backends.pagseguro.views import NotificationsView, SuccessView

urlpatterns = [
    url(r'^notifications/$',
        csrf_exempt(NotificationsView.as_view()),
        name='notifications'),
    url(r'^success/(?P<pk>\d+)/$',
        csrf_exempt(SuccessView.as_view()),
        name='success'),
]
