from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from curaoff.models import Bosyu, Join
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.utils import timezone
from django.urls import reverse

class BosyuListView(ListView):
    model = Bosyu
    template_name = 'curaoff/index.html'

    def index(request):
        bosyu_list = Bosyu.objects.all()
        context = {'bosyu_list': bosyu_list}
        return render(request, 'curaoff/index.html', context)


@login_required
def detail(request,bosyu_seq):
    if request.method == 'POST':
        b1=Bosyu()
        b1.bosyu_seq = bosyu_seq

        t1 = Join()
        t1.bosyu_seq = b1
        t1.join_user_id = request.user.username
        t1.join_user_nm = request.user.last_name + request.user.first_name
        t1.join_app_datetime = timezone.datetime.now()
        t1.delete_flg = '0'

        t1.save()
        messages.success(request, '参加しました！')

        bosyuObj = Bosyu.objects.get(bosyu_seq = bosyu_seq)
        joinList = Join.objects.filter(bosyu_seq = bosyu_seq)
        context = {'joinList' : joinList,'bosyuObj' : bosyuObj,}

        return render(request,'curaoff/bosyu_detail.html',context)
    else:
        bosyuObj = Bosyu.objects.get(bosyu_seq = bosyu_seq)
        joinList = Join.objects.filter(bosyu_seq = bosyu_seq)
        context = {'joinList' : joinList,'bosyuObj' : bosyuObj,}
        return render(request,'curaoff/bosyu_detail.html',context)


@login_required
def join_add(request,bosyu_seq):
    b1=Bosyu()
    b1.bosyu_seq = bosyu_seq

    t1 = Join()
    t1.bosyu_seq = b1
    t1.join_user_id = request.user.username
    t1.join_user_nm = request.user.last_name + request.user.first_name
    t1.join_app_datetime = timezone.datetime.now()
    t1.delete_flg = '0'

    t1.save()
    messages.success(request, '登録内容を保存しました。')
    return render(request,'curaoff/bosyu_detail.html')


class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "curaoff/login.html"
    

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "curaoff/logout.html"