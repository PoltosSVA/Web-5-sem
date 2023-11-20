import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from .forms import UserRegisterForm
from .models import Film, CountDown, Coupon
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from .cart import Cart
import pytz
from django.http import HttpRequest
from back_info.models import Review, News
import logging
logger = logging.getLogger(__name__)
import requests



def ScriptTest(request):
    return render(request, 'filmcatalog/TestScripts.html',None)

def index(request):

    try:
        response = requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data["quote"]
        else:
            quote = "Failed to retrieve quote."
    except:
        quote = ""



    films = Film.objects.all()
    num_films = films.count()
    news = News.objects.order_by('created')
    news_data = [
        {
            'title': news_item.title,
            'img_path': news_item.img_path,
            'created': news_item.created.strftime('%Y-%m-%d'),
            'content': news_item.content,
        }
        for news_item in news
    ]

    news_data_json = json.dumps(news_data)

    context = {
        'films': films,
        'news': news,
        'quote': quote,
        'num_films': num_films,
        'news_data_json': news_data_json
    }

    return render(request, 'index.html', context=context)


class FilmListView(generic.ListView):
    model = Film
    template_name = "filmcatalog/film_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.GET.get('filter_type')
        sort_order = self.request.GET.get('sort_order')

        if filter_type == 'name':
            if sort_order == 'ascending':
                queryset = queryset.order_by('name')
            elif sort_order == 'descending':
                queryset = queryset.order_by('-name')
        elif filter_type == 'price':
            if sort_order == 'ascending':
                queryset = queryset.order_by('cost')
            elif sort_order == 'descending':
                queryset = queryset.order_by('-cost')

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_name'] = self.request.GET.get('filter_name')
        context['filter_price'] = self.request.GET.get('filter_price')
        return context


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "filmcatalog/film_details.html"


class RegistrationFormView(generic.FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('film_list')
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)


def users_profile(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        user.save()
        logger.info('User profile info was changed')
        return redirect('users_profile')
    is_customer = request.user.groups.filter(name='Customer').exists()
    reviews = Review.objects.filter(client_id=user.id)
    desired_timezone = pytz.timezone('Europe/Minsk')
    timezone.activate(desired_timezone)
    current_datetime = timezone.now().strftime('%d/%m/%Y')
    current_timezone = timezone.get_current_timezone()


    context = {
        'user': user,
        'reviews': reviews,
        'current_datetime': current_datetime,
        'is_customer': is_customer,
        'current_timezone': current_timezone
    }

    return render(request, 'profile.html', context=context)

@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
@require_POST
def cart_add(request, film_id):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = Cart(request)
    film = get_object_or_404(Film, id=film_id)
    cart.add(film=film)

    print(cart.cart)

    return redirect('cart_detail')

@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
def cart_remove(request, film_id):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = Cart(request)
    film = get_object_or_404(Film, id=film_id)
    cart.remove(film)
    return redirect('cart_detail')

@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
def cart_detail(request):
    if not request.user.is_authenticated:
        return redirect('index')
    cart = Cart(request)

    if request.method == 'POST':
        # Проверяем, был ли отправлен запрос оформления заказа
        if 'checkout' in request.POST:
            # Обработка оформления заказа (подтверждение оплаты и т. д.)
            # Ваш код обработки заказа здесь...

            # Очистка корзины после успешного оформления заказа
            cart.clear()

            # Перенаправление пользователя на страницу "Спасибо за заказ"
            return redirect('index')


    return render(request, 'cart_detail.html', {'cart':cart})




@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def indexx(request):
    films = Film.objects.all()
    return render(request, "list_film.html", {"films": films})


class FilmCreate(generic.CreateView):
    model = Film
    fields = ['name', 'author', 'genre', 'cost', 'duration', 'description', 'photo']
    success_url = reverse_lazy('list_film')
    template_name = 'create_film.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'create'  # Добавляем информацию о типе представления
        return context


class FilmUpdate(generic.UpdateView):
    model = Film
    fields = ['name', 'author', 'genre', 'cost', 'duration', 'description', 'photo']
    success_url = reverse_lazy('list_film')
    template_name = 'create_film.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'update'  # Добавляем информацию о типе представления
        return context


class FilmDelete(generic.DeleteView):
    model = Film
    success_url = reverse_lazy('list_film')
    template_name = "delete_film.html"


def countdown(request):
    session_id = request.session.session_key
    countdown, created = CountDown.objects.get_or_create(session=session_id)

    if created:
        countdown.start_time = datetime.datetime.now(timezone.utc)
        countdown.duration = 3600
        countdown.save()

    # Переместим следующий блок внутрь условия, чтобы использовать countdown только в случае создания
    current_time = datetime.datetime.now(timezone.utc)
    time_elapsed = (current_time - countdown.start_time).total_seconds()
    remaining_time = countdown.duration - time_elapsed

    request.session['remaining_time'] = remaining_time
    return JsonResponse({'remaining_time': int(remaining_time)})




@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
def validate_coupon(request):
    coupon_code = request.GET.get('coupon_code','')
    discount = validate_coupon_code(coupon_code)
    return JsonResponse({'discount':discount})


def validate_coupon_code(coupon_code):
    try:
        coupon = Coupon.objects.get(code=coupon_code)
        if coupon.is_active:
            return coupon.discount
        else:
            return 0
    except Coupon.DoesNotExist:
        return False, 0