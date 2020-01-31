# blog/models.py

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post_images/',null=True,blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContentImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/')


class Bosyu(models.Model):
    bosyu_seq = models.AutoField(primary_key=True)
    bosyu_kbn = models.CharField(max_length=1)
    bosyu_limit = models.DateTimeField(auto_now=True)
    venue = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    main_text = models.CharField(max_length=1000)
    bosyu_people_cnt = models.IntegerField()
    bosyu_peple_kbn = models.CharField(max_length=1)
    post_datetime = models.DateTimeField(auto_now=True)
    post_user_id = models.CharField(max_length=4)
    update_datetime = models.DateTimeField(auto_now=True)
    update_user_id = models.CharField(max_length=4)
    delete_flg = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class Join(models.Model):
    join_seq = models.AutoField(primary_key=True)
    bosyu_seq = models.IntegerField()
    join_user_id = models.CharField(max_length=4)
    join_app_datetime = models.DateTimeField(auto_now=True)
    delete_flg = models.CharField(max_length=1)

    def __int__(self):
        return self.join_seq


class User(models.Model):
    user_id = models.CharField(max_length=4)
    emp_no = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    admin_flg = models.CharField(max_length=1)

    def __str__(self):
        return self.name