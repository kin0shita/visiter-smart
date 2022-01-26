# Generated by Django 3.0.8 on 2022-01-25 13:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('患者様と面会', '患者様と面会'), ('荷物の受け渡しのみ', '荷物の受け渡しのみ'), ('医師と面談', '医師と面談')], max_length=20, verbose_name='来院目的')),
                ('accompany', models.BooleanField(choices=[(True, 'はい'), (False, 'いいえ')], default=True, verbose_name='同行者はいらっしゃいますか？')),
                ('visited_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('companion_last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='同行者様の姓')),
                ('companion_first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='同行者様の名')),
                ('relationship2', models.CharField(blank=True, choices=[('配偶者', '配偶者'), ('子', '子'), ('父・母', '父・母'), ('兄・弟・姉・妹', '兄・弟・姉・妹'), ('兄・弟・姉・妹の配偶者', '兄・弟・姉・妹の配偶者'), ('子の配偶者', '子の配偶者'), ('子の子', '子の子'), ('配偶者の兄・弟・姉・妹', '配偶者の兄・弟・姉・妹'), ('その他', 'その他')], max_length=30, null=True, verbose_name='続柄')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='email')),
            ],
            options={
                'verbose_name': '0面会事前登録情報',
                'verbose_name_plural': '0面会事前登録データベース',
            },
        ),
        migrations.CreateModel(
            name='Reception3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OutHospital', models.DateTimeField(blank=True, default=None, null=True, verbose_name='帰棟時間')),
                ('active', models.BooleanField(default=True, verbose_name='面会番号が有効か無効か')),
                ('r_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visit.Reception0', verbose_name='id')),
            ],
            options={
                'verbose_name': '3帰院時刻情報',
                'verbose_name_plural': '3帰院時刻データベース',
            },
        ),
        migrations.CreateModel(
            name='Reception1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bt1', models.DecimalField(blank=True, decimal_places=1, default=36.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(34.0), django.core.validators.MaxValueValidator(43.0)], verbose_name='体温')),
                ('bt2', models.DecimalField(blank=True, decimal_places=1, default=36.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(34.0), django.core.validators.MaxValueValidator(43.0)], verbose_name='体温')),
                ('InHospital', models.DateTimeField(blank=True, default=None, null=True, verbose_name='来棟時間')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='email')),
            ],
            options={
                'verbose_name': '1面会時登録情報',
                'verbose_name_plural': '1面会時登録データベース',
            },
        ),
    ]
