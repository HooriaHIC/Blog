# Generated by Django 2.2.5 on 2019-09-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190913_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='item10',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item10_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item4_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item5',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item5_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item6',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item6_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item7',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item7_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item8',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item8_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item9',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='list',
            name='item9_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='Top Ten', max_length=100),
        ),
    ]