from django.shortcuts import render, redirect
from .models import Link
from .forms import LinkForm

from django.core.mail import send_mail
from django.conf import settings

def home(request):
    no_discount = 0
    error = None

    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                form = LinkForm()
        except AttributeError:
            error = "Oops...couldn't get the name or the price"
        except:
            error = "Oops...something went wrong"

    items = Link.objects.all()
    items_count = items.count()

    if items_count > 0:
        discount_list = []
        for item in items:
            if item.old_price > item.current_price:
                discount_list.append(item)
        discounted_count = len(discount_list)

    context = {
        'items': items,
        'items_count': items_count,
        'discounted_count': discounted_count,
        'form': form,
        'error': error
    }
    return render(request, 'links/home.html', context)


def deleteLink(request, pk):
    link = Link.objects.get(id=pk)
    if request.method == 'POST':
        link.delete()
        return redirect("home")
    context = {"object": link}
    return render(request, 'links/delete-template.html', context)

def updatePrices(request):
    items = Link.objects.all()
    for item in items:
        item.save()
        price_difference = float(item.price_difference)

        # Send Mail
        if price_difference < 0:
            subject = f"{item.name[:50]}... - from {item.current_price} to {float(item.current_price) + price_difference}."
            body = f"Hello Vasu,\n{item} item price has decreased from {item.current_price} to {float(item.current_price) + price_difference}\nURL: {item.url}."
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER,],
                fail_silently=False,
                )

    return redirect("home")