# Generated by Django 4.0.6 on 2022-12-13 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0008_alter_task_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.AddField(
            model_name='list',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='List',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='Task.list'),
        ),
    ]