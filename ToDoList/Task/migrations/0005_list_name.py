# Generated by Django 4.0.6 on 2022-12-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_alter_list_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
