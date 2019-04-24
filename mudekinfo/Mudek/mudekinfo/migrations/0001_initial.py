# Generated by Django 2.1.4 on 2019-01-01 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_code', models.PositiveIntegerField(verbose_name='Bölüm Kodu')),
                ('d_name', models.CharField(max_length=60, verbose_name='Bölüm Adı')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_code', models.PositiveIntegerField(verbose_name='Fakülte Kodu')),
                ('f_name', models.CharField(max_length=60, verbose_name='Fakülte Adı')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_code', models.CharField(max_length=10, verbose_name='Dersin Kodu')),
                ('l_name', models.CharField(max_length=50, verbose_name='Dersin Adı')),
                ('l_academician', models.CharField(max_length=70, verbose_name='Dersin Veren Akademisyen')),
                ('l_status', models.CharField(choices=[('COMPULSORY', 'Zorunlu'), ('OPTIONAL', 'Seçmeli')], max_length=15, verbose_name='Ders Durumu')),
                ('l_period', models.CharField(choices=[('AUTUMN', 'Güz'), ('SPRING', 'Bahar')], max_length=15, verbose_name='Ders Dönemi')),
                ('l_class', models.PositiveIntegerField(verbose_name='Ders Sınıfı')),
                ('l_order', models.PositiveIntegerField(verbose_name='Dönemin Kaçıcı Dersi')),
                ('l_possitive', models.CharField(choices=[('DEPARTMENT', 'Bölüm Dersi'), ('SERVICE', 'Bölüm Dışı')], max_length=25, verbose_name='Dersin Aitliği')),
                ('l_language', models.CharField(choices=[('TURKISH', 'Türkçe'), ('ENGLİSH', 'Ingilizce')], max_length=25, verbose_name='Dersin Dili')),
                ('l_ects', models.PositiveIntegerField(verbose_name='Ders ECTS')),
                ('l_akts', models.PositiveIntegerField(verbose_name='Ders AKTS')),
                ('l_credit', models.PositiveIntegerField(verbose_name='Ders Kredi')),
                ('l_theory', models.PositiveIntegerField(verbose_name='Ders Teori Saati')),
                ('l_application', models.PositiveIntegerField(verbose_name='Ders Uygulama Saati')),
                ('l_lab', models.PositiveIntegerField(verbose_name='Ders Laboratuvar Saati')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lesson',
            },
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_no', models.PositiveIntegerField(verbose_name='Çıktı Numarası')),
                ('o_comment', models.TextField(max_length=250, verbose_name='Açıklaması')),
                ('general_version', models.PositiveIntegerField(verbose_name='Genel Sürüm')),
                ('lower_version', models.PositiveIntegerField(verbose_name='Alt Sürüm')),
                ('side_version', models.PositiveIntegerField(verbose_name='Yan Sürüm')),
            ],
            options={
                'verbose_name': 'Output',
                'verbose_name_plural': 'Output',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='output',
            field=models.ManyToManyField(to='mudekinfo.Output'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mudekinfo.Faculty'),
        ),
    ]