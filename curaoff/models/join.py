from django.db import models
from .bosyu import Bosyu
from django.utils import timezone

class Join(models.Model):
    join_seq = models.AutoField(primary_key=True)
    bosyu_seq = models.ForeignKey(Bosyu, db_column='bosyu_seq', on_delete=models.CASCADE)
    join_user_id = models.CharField(max_length=8)
    join_user_nm = models.TextField(max_length=50)
    join_app_datetime = models.DateTimeField(auto_now=True)
    delete_flg = models.CharField(max_length=1)

    def __int__(self):
        return self.join_seq
        