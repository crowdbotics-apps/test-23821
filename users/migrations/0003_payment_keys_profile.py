# Generated by Django 2.2 on 2021-01-11 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210101_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
                ('zip_code', models.IntegerField(default=0)),
                ('country', models.CharField(default='', max_length=100)),
                ('card_holder', models.CharField(default='', max_length=100)),
                ('card_number', models.IntegerField(default=1234123412341234)),
                ('cvc', models.IntegerField(default=123)),
                ('expiration_month', models.CharField(default='DECEMBER', max_length=100)),
                ('expiration_year', models.IntegerField(default=2021)),
                ('picture', models.ImageField(null=True, upload_to='profile')),
                ('password_key', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_keys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method_key', models.CharField(default='', max_length=150)),
                ('customer_Id', models.CharField(default='', max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
