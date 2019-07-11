from kitchen.models import Week, Order, Dish, OrdersTransit, Day
from django.forms import Form, ModelMultipleChoiceField, CheckboxSelectMultiple, CheckboxInput, Select, \
    MultipleChoiceField, ChoiceField


class OrderForm(Form):
    def __init__(self, *args, **kwargs):
        self.week = kwargs.pop('week')
        self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(*args, **kwargs)

        days = Day.objects.filter(week=self.week).prefetch_related('dish')
        for d in days:
            queryset = d.dish.all()
            if queryset:
                print('iii')
                field_kwargs = {
                    'label': d,
                    'queryset': queryset,
                    'widget': CheckboxSelectMultiple,
                    'required': False,
                }
                self.fields.update({
                    d.slug: ModelMultipleChoiceField(**field_kwargs)
                })

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

