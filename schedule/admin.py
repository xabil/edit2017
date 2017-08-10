# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from schedule.models import (
    Floor,
    Exhibitor,
    Point,
    Installation,
    Event,
    Speaker,
)

admin.site.register(Floor)
admin.site.register(Exhibitor)
admin.site.register(Point)
admin.site.register(Installation)
admin.site.register(Event)
admin.site.register(Speaker)
