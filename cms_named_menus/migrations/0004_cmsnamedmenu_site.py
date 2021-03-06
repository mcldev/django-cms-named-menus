# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 15:23
from __future__ import unicode_literals

import cms_named_menus.models
from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


def get_current_site():
    try:
        return cms_named_menus.models.get_current_site()
    except:
        return settings.SITE_ID


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('cms_named_menus', '0003_auto_20170928_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsnamedmenu',
            name='site',
            field=models.ForeignKey(default=get_current_site, help_text='The site the menu is accessible at.', on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site'),
        ),
    ]
