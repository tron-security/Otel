# Generated by Django 4.2.6 on 2023-10-25 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OtelYonetim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Otel Adı')),
                ('image', models.ImageField(upload_to='Logo', verbose_name='Otel Logosu')),
                ('address', models.CharField(max_length=50, verbose_name='Otel Adresi')),
                ('telephone', models.CharField(max_length=13, verbose_name='Otel Telefon Numarası')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Otel Sahibi')),
            ],
        ),
    ]