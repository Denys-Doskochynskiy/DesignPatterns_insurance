# Generated by Django 4.0.4 on 2022-05-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=80),
        ),
    ]