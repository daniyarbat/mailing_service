# Generated by Django 4.2.7 on 2024-02-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='код подтверждения почты'),
        ),
    ]
