from kitchen.models import Week, Order, Dish, OrdersTransit, Day
from django.forms import Form, ModelMultipleChoiceField, CheckboxSelectMultiple, CheckboxInput, Select
from django.db.models import Prefetch


class OrderForm(Form):
    def __init__(self, *args, **kwargs):
        self.week = kwargs.pop('week')
        self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(*args, **kwargs)

        days = Day.objects.filter(week=self.week).prefetch_related('dish')
        # dishes = Dish.objects.prefetch_related('name')
        # print(days)
        # print(dishes)
        for d in days.all():
            # print(d.dish.name)
            queryset = d.dish.all()
            # print(queryset.query)
            if queryset:
                field_kwargs = {
                    'label': d,
                    'queryset': queryset,
                    'widget': CheckboxSelectMultiple,
                }
                self.fields.update({
                    d.slug: ModelMultipleChoiceField(**field_kwargs)
                })

        # for day in self.week.day.all():
        #     queryset = day.dish.all()
        #     # print(queryset)
        #     if queryset:
        #         field_kwargs = {
        #             'label': day,
        #             'queryset': queryset,
        #             'widget': CheckboxSelectMultiple,
        #         }
        #         if self.initial.get(day.slug):
        #             field_kwargs.update({
        #                 'initial': self.initial.get(day.slug)
        #             })
        #         self.fields.update({
        #             day.slug: ModelMultipleChoiceField(**field_kwargs)
        #         })

    # def save(self):
    #     days = Day.objects.prefetch_related(self.week)
    #     for day in days:
    #         # print(day)
    #         resp = self.cleaned_data.get(day.slug)
    #         # ordr, ordrlog = Order.objects.get_or_create()
    #         print(resp)
    #     # ord, ordlog = Order.objects.get_or_create(week=self.week, user=self.user)
