# Generated by Django 4.2.2 on 2023-07-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_delete_csvdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tregistration',
            name='confirmPassword',
        ),
        migrations.AlterField(
            model_name='tregistration',
            name='email',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
