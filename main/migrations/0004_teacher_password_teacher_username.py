# Generated by Django 4.0.2 on 2022-02-28 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_grade_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]