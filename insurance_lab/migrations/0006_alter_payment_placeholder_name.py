# Generated by Django 4.0.4 on 2022-05-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_lab', '0005_payment_placeholder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='placeholder_name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]