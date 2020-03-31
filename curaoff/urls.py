from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from curaoff.views import BosyuListView

app_name = 'curaoff'
urlpatterns = [
    path('',BosyuListView.as_view(), name='bosyu_list'),
    path('bosyu_list/',BosyuListView.as_view(), name='bosyu_list'),
    path('bosyu/<int:bosyu_seq>/', views.detail, name='bosyu_detail'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    url(r'^logout/$', views.MyLogoutView.as_view(), {'template_name': 'index.html'}, name='logout'), 
    path('join_add/<int:bosyu_seq>/', views.join_add, name='join_add'),
    path('new/', views.bosyu_new, name='new'),
]