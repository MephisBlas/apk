# Generated by Django 4.2.2 on 2023-06-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='logo')),
            ],
        ),
        migrations.DeleteModel(
            name='logo',
        ),
    ]