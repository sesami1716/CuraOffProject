# Generated by Django 3.0.2 on 2020-02-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200204_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bosyu',
            name='bosyu_kbn',
            field=models.CharField(choices=[('1', '勉強会'), ('2', '交流会'), ('9', 'その他')], max_length=1),
        ),
        migrations.AlterField(
            model_name='bosyu',
            name='bosyu_peple_kbn',
            field=models.CharField(choices=[('1', '人以上'), ('2', '人以下'), ('9', '人')], max_length=1),
        ),
        migrations.AlterField(
            model_name='bosyu',
            name='post_user_id',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='bosyu',
            name='update_user_id',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='join',
            name='join_user_id',
            field=models.CharField(max_length=8),
        ),
    ]
