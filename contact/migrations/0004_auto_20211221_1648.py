# Generated by Django 3.1 on 2021-12-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contact', '0003_registertable'),
    ]

    operations = [
        migrations.AddField(
            model_name='registertable',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='registertable',
            name='age',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registertable',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registertable',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='registertable',
            name='gender',
            field=models.CharField(default='Male', max_length=50),
        ),
        migrations.AddField(
            model_name='registertable',
            name='occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registertable',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='profiles/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='registertable',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
