# Generated by Django 2.2 on 2020-05-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('model_pic', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
