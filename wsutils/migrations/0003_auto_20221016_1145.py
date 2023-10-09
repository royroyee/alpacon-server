# Generated by Django 4.1.1 on 2022-10-16 02:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wsutils', '0002_alter_websocketsession_client'),
    ]

    operations = [
        migrations.DeleteModel('WebSocketSession'),
        migrations.CreateModel(
            name='WebSocketSession',
            fields=[
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='added at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(editable=False, null=True, verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_ip', models.GenericIPAddressField(verbose_name='remote IP')),
                ('channel_id', models.CharField(editable=False, max_length=128, verbose_name='channel ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', related_query_name='session', to='wsutils.websocketclient', verbose_name='WebSocket client')),
            ],
            options={
                'verbose_name': 'WebSocket session',
                'verbose_name_plural': 'WebSocket sessions',
                'get_latest_by': 'added_at',
            },
        ),
    ]