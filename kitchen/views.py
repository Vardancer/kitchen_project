from django.shortcuts import render
from django.views.generic import ListView, DetailView

from kitchen import models as m


class Index(ListView):
    model = m.Week
    template_name = "week-list.html"


