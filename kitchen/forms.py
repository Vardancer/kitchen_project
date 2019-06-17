from kitchen.models import Week, Order, Dish, OrdersTransit
from django.forms import Form, ModelMultipleChoiceField, CheckboxSelectMultiple


class OrderForm(Form):
    def __init__(self, *args, **kwargs):
        self.week = kwargs.pop('week')
        self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(*args, **kwargs)

        for day in self.week.day.all():
            queryset = day.dish.all()

            if queryset:
                field_kwargs = {
                    'label': day,
                    'queryset': queryset,
                    'widget': CheckboxSelectMultiple,
                }
                if self.initial.get(day.slug):
                    field_kwargs.update({
                        'initial': self.initial.get(day.slug)
                    })
                self.fields.update({
                    day.slug: ModelMultipleChoiceField(**field_kwargs)
                })

    def save(self):
        pass
        q = Order.objects.filter(
            user=self.user,
            week=self.week
        )
        # print(q.query)
        if q:
            print("111")
        else:
            print("222")
            total_cost = 0

            # prices = []
            for m in self.week.day.all():
                response = self.cleaned_data.get(m.slug)
                """sasasa"""
                for pr in response:
                    total_cost += pr.price

            ordr, o_log = Order.objects.get_or_create(user=self.user, week=self.week, total_cost=total_cost)
            for m in self.week.day.all():
                response = self.cleaned_data.get(m.slug)
                for pr in response:
                    rdtr = OrdersTransit.objects.create(dish_id=pr.id, order=ordr, cost=pr.price, is_half=False)
                    print(rdtr)

        return ordr
