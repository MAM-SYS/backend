# Generated by Django 2.1.5 on 2019-04-19 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
        ('company', '0002_auto_20190408_2120'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WORKING', 'WORKING'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT'), ('NORESPONSE', 'NORESPONSE')], max_length=10)),
                ('apply_method', models.CharField(choices=[('COMPANY', 'COMPANY'), ('WEBSITE', 'WEBSITE'), ('FRIEND', 'FRIEND')], max_length=10)),
                ('interviewer_rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('total_rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=40000, null=True)),
                ('asked_salary', models.IntegerField()),
                ('offered_salary', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('interview_date', models.DateField(null=True)),
                ('response_time_before_review', models.CharField(choices=[('1WEEK', '1WEEK'), ('2WEEK', '2WEEK'), ('1MONT', '1MONTH'), ('MORE', 'MORE')], max_length=8)),
                ('response_time_after_review', models.CharField(choices=[('1WEEK', '1WEEK'), ('2WEEK', '2WEEK'), ('1MONT', '1MONTH'), ('MORE', 'MORE')], max_length=8, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('cons', models.ManyToManyField(to='review.Cons')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.Job')),
                ('pros', models.ManyToManyField(to='review.Pros')),
                ('view', models.ManyToManyField(related_name='interview_views', to=settings.AUTH_USER_MODEL)),
                ('vote', models.ManyToManyField(related_name='interview_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='companyreview',
            name='description',
            field=models.CharField(max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='companyreview',
            name='state',
            field=models.CharField(choices=[('FULL', 'FULL TIME'), ('PART', 'PART TIME'), ('CONTRACT', 'CONTRACT'), ('INTERN', 'INTERN'), ('FREELANCE', 'FREELANCE'), ('REMOTE', 'REMOTE')], max_length=10),
        ),
    ]