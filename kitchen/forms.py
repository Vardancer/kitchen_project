from kitchen.models import Week, Order, Dish, OrdersTransit, Day
from django.forms import Form, ModelMultipleChoiceField, CheckboxSelectMultiple, CheckboxInput, Select


class OrderForm(Form):
    def __init__(self, *args, **kwargs):
        self.week = kwargs.pop('week')
        self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(*args, **kwargs)

        days = Day.objects.filter(week=self.week).prefetch_related('dish')

        for d in days:
            queryset = d.dish.all()
            if queryset:
                field_kwargs = {
                    'label': d,
                    'queryset': queryset,
                    'widget': CheckboxSelectMultiple,
                }
                if self.initial.get(d.slug):
                    field_kwargs.update({
                        'initial': self.initial.get(d.slug)
                    })
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

    def get_initial(self):
        initial = {}
        if self.user:
            orders = Order.objects.filter(week=self.week).prefetch_related('dish')
            days = Day.objects.filter(week=self.week).prefetch_related('dish')
            for day in days:
                initial[day.slug] = [dish.pk for dish in orders.dish.all()]
        return initial

    def save(self):
        days = Day.objects.filter(week=self.week).prefetch_related('dish__dishes')
        vals = []
        t_price = 0
        for day in days.all():
            resp = self.cleaned_data.get(day.slug)
            for r in resp:
                t_price += r.price
                vals.append(OrdersTransit(dish_id=r.id, cost=r.price))
        ord, ordlog = Order.objects.get_or_create(week=self.week, user=self.user, total_cost=t_price)

        for v in vals:
            v.order = ord
        OrdersTransit.objects.bulk_create(vals)

