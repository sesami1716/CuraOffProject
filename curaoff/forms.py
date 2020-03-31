from django.contrib.auth import forms as auth_forms
from django import forms
from .models import Bosyu

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class NewForm(forms.ModelForm):
    bosyu_limit = forms.SplitDateTimeField(label='募集期限')
    venue_datetime = forms.SplitDateTimeField(label='開催日時')

    class Meta:
        model = Bosyu
        fields = (
             'bosyu_kbn'
            ,'bosyu_limit'
            ,'venue'
            ,'venue_datetime'
            ,'title'
            ,'main_text'
            ,'bosyu_people_cnt'
            ,'bosyu_peple_kbn'
            )