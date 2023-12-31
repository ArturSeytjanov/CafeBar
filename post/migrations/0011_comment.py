# Generated by Django 3.2 on 2023-05-04 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20230502_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Название')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарии',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
