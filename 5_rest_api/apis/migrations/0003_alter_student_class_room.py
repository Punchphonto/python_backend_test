# Generated by Django 4.2.10 on 2024-05-19 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_remove_teacherclassroom_date_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='apis.classroom'),
        ),
    ]
