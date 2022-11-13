
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import SubscriberForm


class PromiseCreateView(CreateView):
    model = SubscriberForm
    form_class = SubscriberForm


def shop(request):
    context = {
        'form': SubscriberForm(request.POST or None),
        'a': 'test test test'
    }

    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('date'))
        print(request.POST)

    return render(request, 'shop/index.html', context)
