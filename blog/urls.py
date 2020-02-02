from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blog.views import IndexView, PostDetailView, CategoryListView, TagListView, CategoryPostView, TagPostView
from blog.views import BosyuListView, BosyuDetailView

app_name = 'blog'
urlpatterns = [
    path('',BosyuListView.as_view(), name='bosyu_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/',CategoryPostView.as_view(), name='category_post'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
    path('bosyu_list/',BosyuListView.as_view(), name='bosyu_list'),
    path('bosyu/<int:pk>/', BosyuDetailView.as_view(), name='bosyu_detail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)