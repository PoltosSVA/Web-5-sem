from django.urls import path
from . import views

app_name = 'back_info'

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('policy/', views.policy, name='policy'),
    path('openings/', views.openings, name='openings'),
    path('news/', views.news, name='news'),
    path('news/news_0/', views.news_0, name='news_0'),
    path('news/news_1/', views.news_1, name='news_1'),
    path('news/news_2/', views.news_2, name='news_2'),
    path('news/news_3/', views.news_3, name='news_3'),
    path('news/news_4/', views.news_4, name='news_4'),
    path('news/news_5/', views.news_5, name='news_5'),
    path('news/news_5/', views.news_5, name='news_5'),
    path('contacts/', views.contacts, name='contacts'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('reviews/', views.reviews, name='reviews'),
    path('coupons/', views.coupons, name='coupons'),
]
