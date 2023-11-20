import requests
from django.shortcuts import render, redirect
from .models import News, Review
from .forms import ReviewForm
def about_us(request):



    return render(request, 'back_info/about_us.html')


def coupons(request):

    return render(request, 'back_info/coupons.html')


def policy(request):

    return render(request, 'back_info/policy.html')


def openings(request):

    return render(request, 'back_info/openings.html')


def news(request):

    return render(request, 'back_info/news.html')


def news_0(request):

    news = News.objects.all().first()

    return render(request, 'back_info/news_0.html', {'news': news})


def news_1(request):

    news = News.objects.all()[1]

    return render(request, 'back_info/news_1.html', {'news': news})


def news_2(request):
    news = News.objects.all()[2]

    return render(request, 'back_info/news_2.html', {'news': news})


def news_3(request):
    news = News.objects.all()[3]

    return render(request, 'back_info/news_3.html', {'news': news})


def news_4(request):
    news = News.objects.all()[4]
    return render(request, 'back_info/news_4.html', {'news': news})


def news_5(request):
    news = News.objects.all()[5]
    return render(request, 'back_info/news_5.html', {'news': news})


def contacts(request):

    return render(request, 'back_info/contacts.html')


def terms_conditions(request):

    return render(request, 'back_info/terms_definitions.html')


def reviews(request):
    reviews = Review.objects.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user
            review.save()
            return redirect('back_info:reviews')
    else:
        form = ReviewForm()

    is_customer = request.user.groups.filter(name='Customer').exists()
    user = request.user

    context = {
        'user': user,
        'form': form,
        'reviews': reviews,
        'is_customer': is_customer,

    }
    return render(request, 'back_info/reviews.html', context=context)