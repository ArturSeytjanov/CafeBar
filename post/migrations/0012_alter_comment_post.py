# Generated by Django 3.2 on 2023-05-04 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Пост'),
        ),
    ]