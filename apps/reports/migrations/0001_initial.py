# Generated by Django 4.2.3 on 2023-07-31 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='files.codefile')),
                ('result', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_sent', models.BooleanField(db_index=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
