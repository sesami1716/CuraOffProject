# curapff/models.py

from django.db import models
from django.utils import timezone

class Bosyu(models.Model):
    BOSYU_KBN_CHOICES = (
        ('1', '勉強会'),
        ('2', '交流会'),
        ('9', 'その他'),
    )

    BOSYU_PEP_KBN_CHOICES = (
        ('1', '人以上'),
        ('2', '人以下'),
        ('9', '人'),
    )

    bosyu_seq = models.AutoField(primary_key=True)
    bosyu_kbn = models.CharField(max_length=1,choices=BOSYU_KBN_CHOICES)
    bosyu_limit = models.DateTimeField()
    venue = models.CharField(max_length=50)
    venue_datetime = models.DateTimeField()
    title = models.CharField(max_length=100)
    main_text = models.TextField(max_length=1000)
    bosyu_people_cnt = models.IntegerField()
    bosyu_peple_kbn = models.CharField(max_length=1,choices=BOSYU_PEP_KBN_CHOICES)
    status = models.CharField(max_length=1)
    post_datetime = models.DateTimeField(auto_now=True)
    post_user_id = models.CharField(max_length=8)
    post_user_nm = models.TextField(max_length=50)
    update_datetime = models.DateTimeField(auto_now=True)
    update_user_id = models.CharField(max_length=8)
    delete_flg = models.CharField(max_length=1)

    class Meta:
        ordering = ['-bosyu_limit']

    def __str__(self):
        return self.title


class Join(models.Model):
    join_seq = models.AutoField(primary_key=True)
    bosyu_seq = models.ForeignKey(Bosyu, db_column='bosyu_seq', on_delete=models.CASCADE)
    join_user_id = models.CharField(max_length=8)
    join_user_nm = models.TextField(max_length=50)
    join_app_datetime = models.DateTimeField(auto_now=True)
    delete_flg = models.CharField(max_length=1)

    def __int__(self):
        return self.join_seq