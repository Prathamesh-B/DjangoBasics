# Generated by Django 5.0.6 on 2024-06-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_no', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6)),
                ('hobbies', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('india', 'India'), ('usa', 'United States'), ('canada', 'Canada'), ('uk', 'United Kingdom')], max_length=20)),
                ('bio', models.TextField()),
            ],
        ),
    ]
