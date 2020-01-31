# Generated by Django 3.0.2 on 2020-01-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contentimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bosyu',
            fields=[
                ('bosyu_seq', models.AutoField(primary_key=True, serialize=False)),
                ('bosyu_kbn', models.CharField(max_length=1)),
                ('bosyu_limit', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('main_text', models.CharField(max_length=1000)),
                ('bosyu_people_cnt', models.IntegerField()),
                ('bosyu_peple_kbn', models.CharField(max_length=1)),
                ('post_datetime', models.DateTimeField(auto_now=True)),
                ('post_user_id', models.CharField(max_length=4)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('update_user_id', models.CharField(max_length=4)),
                ('delete_flg', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('join_seq', models.AutoField(primary_key=True, serialize=False)),
                ('bosyu_seq', models.IntegerField()),
                ('join_user_id', models.CharField(max_length=4)),
                ('join_app_datetime', models.DateTimeField(auto_now=True)),
                ('delete_flg', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=4)),
                ('emp_no', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('admin_flg', models.CharField(max_length=1)),
            ],
        ),
    ]
