# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from schedule.models import (
    Floor,
    Exhibitor,
    Point,
    Installation,
    Event,
    Speaker,
)
from schedule.serializers import (
    FloorSerializer,
    ExhibitorSerializer,
    PointSerializer,
    InstallationSerializer,
    EventSerializer,
    SpeakerSerializer,
)


class FloorViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class ExhibitorViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Exhibitor.objects.filter(publish=True).all()
    serializer_class = ExhibitorSerializer


class PointViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Point.objects.all()
    serializer_class = PointSerializer


class InstallationViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Installation.objects.filter(publish=True).all()
    serializer_class = InstallationSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Event.objects.filter(publish=True).all()
    serializer_class = EventSerializer


class SpeakerViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Speaker.objects.filter(publish=True).all()
    serializer_class = SpeakerSerializer
