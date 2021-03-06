# Generated by Django 3.1.3 on 2020-12-30 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201227_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='LetsConnect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=55)),
                ('lastname', models.CharField(default='', max_length=55)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.IntegerField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
