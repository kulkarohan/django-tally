# Generated by Django 3.0.2 on 2020-01-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YelpBusiness',
            fields=[
                ('business_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('stars', models.FloatField(blank=True, null=True)),
                ('review_count', models.IntegerField(blank=True, null=True)),
                ('is_closed', models.BooleanField(blank=True, null=True)),
                ('is_claimed', models.BooleanField(blank=True, null=True)),
                ('display_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('data_source', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'business',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YelpReview',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('review_id', models.CharField(blank=True, max_length=50, null=True)),
                ('business_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('stars', models.FloatField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('data_source', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YelpYelpScraping',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('review_id', models.CharField(blank=True, max_length=50, null=True)),
                ('business_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('stars', models.FloatField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'yelp_scraping',
                'managed': False,
            },
        ),
    ]
