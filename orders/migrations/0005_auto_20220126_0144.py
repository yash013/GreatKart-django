# Generated by Django 3.1 on 2022-01-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20220126_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variation',
            new_name='variations',
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
