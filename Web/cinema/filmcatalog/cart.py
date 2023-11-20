from decimal import Decimal
from django.conf import settings
from .models import Film


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, film):
        film_id = str(film.id)
        print(f"Adding film {film_id} to the cart")
        if film_id not in self.cart:
            self.cart[film_id] = {'quantity': 0,
                                  'price': str(film.cost)}
        self.cart[film_id]['quantity'] += 1
        self.save()

    def save(self):
        # cart session update
        self.session[settings.CART_SESSION_ID] = self.cart
        # save updated cart session
        self.session.modified = True

    def remove(self, film):
        film_id = str(film.id)
        if film_id in self.cart:
            del self.cart[film_id]
            self.save()

    def __iter__(self):
        film_ids = self.cart.keys()
        films = Film.objects.filter(id__in=film_ids)
        for film in films:
            self.cart[str(film.id)]['film'] = film

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
