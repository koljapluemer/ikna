# Generated by Django 5.1.6 on 2025-03-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_word_native_info_alter_word_script_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='answer',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prompt',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
