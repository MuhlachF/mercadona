# Generated by Django 4.2.5 on 2023-09-25 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_administrator_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.administrator'),
        ),
    ]
