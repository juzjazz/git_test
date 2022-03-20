# Generated by Django 2.2.11 on 2022-02-18 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=128, verbose_name='考试批次')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=128, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Kecheng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kecheng_name', models.CharField(max_length=128, verbose_name='课程名称')),
            ],
        ),
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('usertype', models.CharField(max_length=32, verbose_name='用户类型')),
            ],
        ),
        migrations.CreateModel(
            name='Zhuanye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhuanye_name', models.CharField(max_length=128, verbose_name='专业名称')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(max_length=128, verbose_name='学号')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('birth', models.CharField(max_length=128, verbose_name='生日')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('study_time', models.CharField(max_length=128, verbose_name='入学时间')),
                ('password', models.CharField(max_length=64, verbose_name='登陆密码')),
                ('addr', models.CharField(max_length=128, verbose_name='家庭地址')),
                ('number', models.CharField(max_length=128, verbose_name='身份证')),
                ('other', models.CharField(max_length=128, verbose_name='备注')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Grade', verbose_name='所属班级')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(max_length=128, verbose_name='学号')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('birth', models.CharField(max_length=128, verbose_name='生日')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('study_time', models.CharField(max_length=128, verbose_name='入学时间')),
                ('password', models.CharField(max_length=64, verbose_name='登陆密码')),
                ('addr', models.CharField(max_length=128, verbose_name='家庭地址')),
                ('number', models.CharField(max_length=128, verbose_name='身份证')),
                ('other', models.CharField(max_length=128, verbose_name='备注')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Grade', verbose_name='所属班级')),
            ],
        ),
        migrations.CreateModel(
            name='SelectGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('kecheng_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Kecheng', verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=128, verbose_name='科目')),
                ('score', models.IntegerField(max_length=128, verbose_name='成绩')),
                ('batch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Batch', verbose_name='所属考试批次')),
                ('grade_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Grade', verbose_name='所属班级')),
                ('stu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Student', verbose_name='选择学生姓名')),
            ],
        ),
    ]
