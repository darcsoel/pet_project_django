# Generated by Django 3.2.7 on 2021-10-23 19:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bills", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="from_user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="from_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="bill",
            name="to_user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="to_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]