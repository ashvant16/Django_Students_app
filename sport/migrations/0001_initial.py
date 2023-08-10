# Generated by Django 4.2.2 on 2023-06-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namelr', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('leave_type', models.CharField(max_length=20)),
                ('reason', models.TextField()),
                ('supporting_docs', models.FileField(upload_to='supdocfolder')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=20)),
                ('confirmPassword', models.CharField(max_length=20)),
            ],
        ),
    ]
