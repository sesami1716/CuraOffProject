from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from blog.views import IndexView
from blog.views import BosyuListView

app_name = 'blog'
urlpatterns = [
    path('',BosyuListView.as_view(), name='bosyu_list'),
    path('bosyu_list/',BosyuListView.as_view(), name='bosyu_list'),
    path('bosyu/<int:bosyu_seq>/', views.detail, name='bosyu_detail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)