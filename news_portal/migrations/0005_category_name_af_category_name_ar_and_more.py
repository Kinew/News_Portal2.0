# Generated by Django 5.0.4 on 2024-04-20 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0004_news_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_af',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ar',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ar_dz',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ast',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_be',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_bg',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_bn',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_br',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_bs',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ca',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ckb',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_cs',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_cy',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_da',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_de',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_dsb',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_el',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en_au',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en_gb',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_eo',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es_ar',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es_co',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es_mx',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es_ni',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es_ve',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_et',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_eu',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fa',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fi',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fy',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ga',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_gd',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_gl',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_he',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_hi',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_hr',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_hsb',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_hu',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_hy',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ia',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ig',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ind',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_io',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_is',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_it',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ja',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ka',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_kab',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_kk',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_km',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_kn',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ko',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ky',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_lb',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_lt',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_lv',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_mk',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ml',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_mn',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_mr',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ms',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_my',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_nb',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ne',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_nl',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_nn',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_os',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pa',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pl',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pt',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pt_br',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ro',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sk',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sl',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sq',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sr',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sr_latn',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sv',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sw',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ta',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_te',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_tg',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_th',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_tk',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_tr',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_tt',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_udm',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ug',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ur',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_vi',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_zh_hans',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_zh_hant',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_af', models.CharField(max_length=200, null=True)),
                ('name_ar', models.CharField(max_length=200, null=True)),
                ('name_ar_dz', models.CharField(max_length=200, null=True)),
                ('name_ast', models.CharField(max_length=200, null=True)),
                ('name_az', models.CharField(max_length=200, null=True)),
                ('name_bg', models.CharField(max_length=200, null=True)),
                ('name_be', models.CharField(max_length=200, null=True)),
                ('name_bn', models.CharField(max_length=200, null=True)),
                ('name_br', models.CharField(max_length=200, null=True)),
                ('name_bs', models.CharField(max_length=200, null=True)),
                ('name_ca', models.CharField(max_length=200, null=True)),
                ('name_ckb', models.CharField(max_length=200, null=True)),
                ('name_cs', models.CharField(max_length=200, null=True)),
                ('name_cy', models.CharField(max_length=200, null=True)),
                ('name_da', models.CharField(max_length=200, null=True)),
                ('name_de', models.CharField(max_length=200, null=True)),
                ('name_dsb', models.CharField(max_length=200, null=True)),
                ('name_el', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_en_au', models.CharField(max_length=200, null=True)),
                ('name_en_gb', models.CharField(max_length=200, null=True)),
                ('name_eo', models.CharField(max_length=200, null=True)),
                ('name_es', models.CharField(max_length=200, null=True)),
                ('name_es_ar', models.CharField(max_length=200, null=True)),
                ('name_es_co', models.CharField(max_length=200, null=True)),
                ('name_es_mx', models.CharField(max_length=200, null=True)),
                ('name_es_ni', models.CharField(max_length=200, null=True)),
                ('name_es_ve', models.CharField(max_length=200, null=True)),
                ('name_et', models.CharField(max_length=200, null=True)),
                ('name_eu', models.CharField(max_length=200, null=True)),
                ('name_fa', models.CharField(max_length=200, null=True)),
                ('name_fi', models.CharField(max_length=200, null=True)),
                ('name_fr', models.CharField(max_length=200, null=True)),
                ('name_fy', models.CharField(max_length=200, null=True)),
                ('name_ga', models.CharField(max_length=200, null=True)),
                ('name_gd', models.CharField(max_length=200, null=True)),
                ('name_gl', models.CharField(max_length=200, null=True)),
                ('name_he', models.CharField(max_length=200, null=True)),
                ('name_hi', models.CharField(max_length=200, null=True)),
                ('name_hr', models.CharField(max_length=200, null=True)),
                ('name_hsb', models.CharField(max_length=200, null=True)),
                ('name_hu', models.CharField(max_length=200, null=True)),
                ('name_hy', models.CharField(max_length=200, null=True)),
                ('name_ia', models.CharField(max_length=200, null=True)),
                ('name_ind', models.CharField(max_length=200, null=True)),
                ('name_ig', models.CharField(max_length=200, null=True)),
                ('name_io', models.CharField(max_length=200, null=True)),
                ('name_is', models.CharField(max_length=200, null=True)),
                ('name_it', models.CharField(max_length=200, null=True)),
                ('name_ja', models.CharField(max_length=200, null=True)),
                ('name_ka', models.CharField(max_length=200, null=True)),
                ('name_kab', models.CharField(max_length=200, null=True)),
                ('name_kk', models.CharField(max_length=200, null=True)),
                ('name_km', models.CharField(max_length=200, null=True)),
                ('name_kn', models.CharField(max_length=200, null=True)),
                ('name_ko', models.CharField(max_length=200, null=True)),
                ('name_ky', models.CharField(max_length=200, null=True)),
                ('name_lb', models.CharField(max_length=200, null=True)),
                ('name_lt', models.CharField(max_length=200, null=True)),
                ('name_lv', models.CharField(max_length=200, null=True)),
                ('name_mk', models.CharField(max_length=200, null=True)),
                ('name_ml', models.CharField(max_length=200, null=True)),
                ('name_mn', models.CharField(max_length=200, null=True)),
                ('name_mr', models.CharField(max_length=200, null=True)),
                ('name_ms', models.CharField(max_length=200, null=True)),
                ('name_my', models.CharField(max_length=200, null=True)),
                ('name_nb', models.CharField(max_length=200, null=True)),
                ('name_ne', models.CharField(max_length=200, null=True)),
                ('name_nl', models.CharField(max_length=200, null=True)),
                ('name_nn', models.CharField(max_length=200, null=True)),
                ('name_os', models.CharField(max_length=200, null=True)),
                ('name_pa', models.CharField(max_length=200, null=True)),
                ('name_pl', models.CharField(max_length=200, null=True)),
                ('name_pt', models.CharField(max_length=200, null=True)),
                ('name_pt_br', models.CharField(max_length=200, null=True)),
                ('name_ro', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('name_sk', models.CharField(max_length=200, null=True)),
                ('name_sl', models.CharField(max_length=200, null=True)),
                ('name_sq', models.CharField(max_length=200, null=True)),
                ('name_sr', models.CharField(max_length=200, null=True)),
                ('name_sr_latn', models.CharField(max_length=200, null=True)),
                ('name_sv', models.CharField(max_length=200, null=True)),
                ('name_sw', models.CharField(max_length=200, null=True)),
                ('name_ta', models.CharField(max_length=200, null=True)),
                ('name_te', models.CharField(max_length=200, null=True)),
                ('name_tg', models.CharField(max_length=200, null=True)),
                ('name_th', models.CharField(max_length=200, null=True)),
                ('name_tk', models.CharField(max_length=200, null=True)),
                ('name_tr', models.CharField(max_length=200, null=True)),
                ('name_tt', models.CharField(max_length=200, null=True)),
                ('name_udm', models.CharField(max_length=200, null=True)),
                ('name_ug', models.CharField(max_length=200, null=True)),
                ('name_uk', models.CharField(max_length=200, null=True)),
                ('name_ur', models.CharField(max_length=200, null=True)),
                ('name_uz', models.CharField(max_length=200, null=True)),
                ('name_vi', models.CharField(max_length=200, null=True)),
                ('name_zh_hans', models.CharField(max_length=200, null=True)),
                ('name_zh_hant', models.CharField(max_length=200, null=True)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='news_portal.category', verbose_name='This is the help text')),
            ],
        ),
    ]
