# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from schedule.models import (
    Floor,
    Exhibitor,
    Point,
    Installation,
    Event,
    Speaker,
)


class FloorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Floor
        depth = 1
        fields = '__all__'


class ExhibitorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Exhibitor
        depth = 1
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):

    class Meta:

        model = Point
        depth = 1
        fields = '__all__'


class InstallationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Installation
        depth = 1
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = Event
        depth = 1
        fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Speaker
        depth = 1
