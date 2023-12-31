# Generated by Django 5.0 on 2023-12-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothapp', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('mobile', models.BigIntegerField(null=True)),
                ('address', models.CharField(max_length=350, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
    ]
