# Generated by Django 3.2.8 on 2021-10-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_alter_link_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
