from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import FormView, FormMixin


from kitchen import models as m
from kitchen.forms import OrderForm
from kitchen.models import Order, OrdersTransit


class Index(ListView):
    model = m.Week
    template_name = "week-list.html"


class OrderFormView(FormView):
    form_class = OrderForm
    template_name = 'order.html'
    success_url = '.'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.week = m.Week.objects.get(pk=kwargs.get('pk'))
        except m.Week.DoesNotExist:
            raise Http404
        return super(OrderFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'week': self.week})
        return context

    def get_form_kwargs(self):
        kwargs = super(OrderFormView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'week': self.week,
        })
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        context = self.get_context_data(form=form)
        context.update({'success': True})
        return self.render_to_response(context)


class WeekDetailView(DetailView):
    template_name = 'week-detail.html'
    model = m.Week


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order-edit.html'
    fields = ['dish']

    # def get_queryset(self):
    #     # queryset = super(OrderUpdateView, self).get_queryset()
    #     queryset = Order.objects.prefetch_related('dish')
    #     return queryset


class OrderListView(ListView):
    model = Order
    template_name = 'orders-list.html'


