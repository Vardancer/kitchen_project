from kitchen.models import Week, Order, Dish, OrdersTransit, Day
from django.forms import Form, ModelMultipleChoiceField, CheckboxSelectMultiple, CheckboxInput, Select


class OrderForm(Form):
    def __init__(self, *args, **kwargs):
        self.week = kwargs.pop('week')
        self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(*args, **kwargs)

        days = Day.objects.filter(week=self.week).prefetch_related('dish')

        print(days)
        # print(dishes)
        for d in days:
            # print(d.dish.name)
            queryset = d.dish.all()
            # print(d)
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

    def save(self):
        days = Day.objects.filter(week=self.week).prefetch_related('dish__dishes')
        vals = []
        t_price = 0
        for day in days.all():
            # print(day.slug)
            resp = self.cleaned_data.get(day.slug)
            for r in resp:
                # r.update({'cost': 111.01})
                t_price += r.price
                vals.append((r.id, r.price,))
            print(resp)
        # ord, ordlog = Order.objects.get_or_create(week=self.week, user=self.user, total_cost=t_price)
        vals2 = []
        for v in vals:
            vals2.append(v)
        # todo tuple dish_obj(got id), order_obj(done), dish_price(done), optional_is_half(bool)
        # OrdersTransit.objects.update_or_create()
        print(vals2)
