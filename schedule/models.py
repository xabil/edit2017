# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Floor(models.Model):

    number = models.IntegerField(
        unique=True)
    theme = models.CharField(
        max_length=1024)
    plan = models.ImageField(
        upload_to='medida/plans/',
        blank=True,
        null=True)

    def __unicode__(self):

        return self.theme


class Speaker(models.Model):

    first_name = models.CharField(
        max_length=1024)
    last_name = models.CharField(
        max_length=1024)
    bio = RichTextUploadingField()
    website = models.URLField(
        max_length=1024,
        null=True,
        blank=True)
    facebook = models.URLField(
        max_length=1024,
        null=True,
        blank=True)
    twitter = models.URLField(
        max_length=1024,
        null=True,
        blank=True)
    email = models.CharField(
        max_length=1024,
        null=True,
        blank=True)
    photo = models.ImageField(
        upload_to='media/speakers/')
    publish = models.BooleanField(
        default=True)

    def __unicode__(self):

        return self.first_name + ' ' + self.last_name


class Exhibitor(models.Model):

    name = models.CharField(
        max_length=1024)
    address = models.CharField(
        max_length=2048)
    facebook = models.URLField(
        max_length=1024,
        null=True,
        blank=True)
    twitter = models.URLField(
        max_length=1024,
        null=True,
        blank=True)
    email = models.CharField(
        max_length=1024,
        null=True,
        blank=True)
    website = models.CharField(
        max_length=2048,
        null=True,
        blank=True)
    logo = models.ImageField(
        upload_to='media/exhibitors/')
    publish = models.BooleanField(
        default=True)

    def __unicode__(self):

        return self.name


class Point(models.Model):

    floor = models.ForeignKey(
        Floor,
        related_name='point',
        on_delete=models.CASCADE)
    name = models.CharField(
        max_length=2048)
    description = RichTextUploadingField()
    photo = models.ImageField(
        upload_to='media/points/',
        blank=True,
        null=True)

    def __unicode__(self):

        return self.name


class Installation(models.Model):

    point = models.ForeignKey(
        Point,
        related_name='booth',
        on_delete=models.CASCADE)
    exhibitor = models.ForeignKey(
        Exhibitor,
        related_name='booth',
        on_delete=models.CASCADE)
    name = models.CharField(
        max_length=1024)
    number = models.IntegerField(
        unique=True)
    publish = models.BooleanField(
        default=True)
    photo = models.ImageField(
        upload_to='media/installations/')

    def __unicode__(self):

        return self.name


class Event(models.Model):

    point = models.ForeignKey(
        Point,
        null=True,
        blank=True,
        related_name='event',
        on_delete=models.CASCADE)
    installation = models.ForeignKey(
        Installation,
        null=True,
        blank=True,
        related_name='event',
        on_delete=models.CASCADE)
    speaker = models.ForeignKey(
        Speaker,
        null=True,
        blank=True,
        related_name='speaker',
        on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20148)
    description = RichTextUploadingField(
        null=True,
        blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    photo = models.ImageField(
        upload_to='media/evenets')
    publish = models.BooleanField(
        default=True)

    def __unicode__(self):

        return self.name
