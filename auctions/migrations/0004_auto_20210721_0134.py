# Generated by Django 3.2.5 on 2021-07-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210720_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alllisting',
            name='image',
            field=models.ImageField(blank=True, default='default_auction_image.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default='default_auction_image.jpg', null=True, upload_to='images/'),
        ),
    ]