# Generated by Django 2.2.17 on 2021-01-06 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20210105_0624'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('manufacture_year', models.DateField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=20, null=True)),
                ('make', models.PositiveIntegerField(choices=[(1, 'Volve'), (2, 'BMW')], null=True)),
                ('model', models.PositiveIntegerField(choices=[(1, 'CS6'), (2, 'CS7'), (3, 'CS8'), (4, 'CS9')], null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('listing_type', models.PositiveIntegerField(choices=[(0, 'Regular'), (1, 'No Reserve'), (2, 'Returning'), (3, 'Royalty')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.ListingCategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListingFaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Question that display in the form', max_length=500)),
                ('input_type', models.CharField(choices=[('S', 'Select'), ('I', 'Input'), ('T', 'Textarea'), ('C', 'Checkbox'), ('D', 'Date'), ('R', 'Radio')], default=('I', 'Input'), help_text='Select type of Questions', max_length=1)),
                ('sort_order', models.PositiveSmallIntegerField(help_text='Question are display on the base of Sort order Number')),
                ('step_choice', models.CharField(default=('N', 'None'), help_text='Add step if you want to display Question in specific step', max_length=1)),
                ('required', models.BooleanField(default=False, help_text='Checked if this Questions required')),
                ('category', models.ForeignKey(help_text='Select category where this Questions display', on_delete=django.db.models.deletion.CASCADE, to='categories.ListingCategory')),
            ],
        ),
        migrations.CreateModel(
            name='OptionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ListingFaqAttached',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.Listing')),
                ('listing_faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.ListingFaq')),
            ],
        ),
        migrations.AddField(
            model_name='listingfaq',
            name='option',
            field=models.ManyToManyField(blank=True, help_text='This option used when your input type select , radio or checkbox', to='listing.OptionList'),
        ),
    ]
