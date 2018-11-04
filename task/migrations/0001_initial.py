# Generated by Django 2.1.3 on 2018-11-04 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('alert_time', models.TimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('parent_task_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.TodoTask')),
            ],
        ),
    ]
