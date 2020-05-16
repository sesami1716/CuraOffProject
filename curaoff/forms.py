import bootstrap_datepicker_plus as datetimepicker
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
    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

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
        widgets = {
            'bosyu_limit': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'venue_datetime': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }