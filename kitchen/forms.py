from kitchen.models import Week, Order, Dish
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
            for m in self.week.day.all():
                response = self.cleaned_data.get(m.slug)
                # r = Dish.objects.filter(days__slug=m.slug)
                # print(r)
                for pr in response:
                    print(pr.price)

