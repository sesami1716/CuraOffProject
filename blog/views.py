from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404

from blog.models import Post, Category, Tag, Bosyu, Join, User


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'


class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))


class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagPostView(ListView):
    model = Post
    template_name = 'blog/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class BosyuListView(ListView):
    model = Bosyu
    template_name = 'blog/index.html'

    def index(request):
        bosyu_list = Bosyu.objects.all()
        context = {'bosyu_list': bosyu_list}
        return render(request, 'blog/index.html', context)

class BosyuDetailView(DetailView):
    model = Bosyu

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

