# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Headlines(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    time_added = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = "Headlines"

    def __str__(self):
        return self.title