# Generated by Django 5.0.1 on 2024-07-04 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=64)),
                ('categories', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.comment'),
        ),
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=450)),
                ('img', models.ImageField(upload_to='')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.bids')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.comment')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.item')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='auctions.item')),
            ],
        ),
    ]
