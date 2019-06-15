# from kitchen.models import Week
from django.forms import Form, ModelMultipleChoiceField


class OrderForm(Form):
    def __init__(self, *args, **kwargs):
        self.week = kwargs.pop('week')
        self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(self, *args, **kwargs)

        for day in self.week.day.all():
            queryset = day.dish.all()

            if queryset:
                field_kwargs = {
                    'label': day,
                    'queryset': queryset,
                }


