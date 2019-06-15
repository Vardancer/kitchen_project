from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, FormMixin


from kitchen import models as m
from kitchen.forms import OrderForm


class Index(ListView):
    model = m.Week
    template_name = "week-list.html"


class WeekForm(FormView):
    form_class = OrderForm
    template_name = 'order.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.week = m.Week.objects.get(pk=kwargs.get('pk'))
        except m.Week.DoesNotExist:
            raise Http404
        return super(WeekForm, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'week': self.week})
        return context

    def get_form_kwargs(self):
        kwargs = super(WeekForm, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'week': self.week,
        })
        return kwargs


class WeekDetailView(DetailView):
    template_name = 'week-detail.html'
    model = m.Week
