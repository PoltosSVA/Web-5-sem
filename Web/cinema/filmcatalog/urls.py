from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('countdown/', views.countdown, name="countdown"),
    path('test/',views.ScriptTest, name='script-test'),
    path('films/', views.FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film_details'),
    path('register/', views.RegistrationFormView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('users_profile/', views.users_profile, name='users_profile'),
    path('cart/', views.cart_detail, name="cart_detail"),
    path('cart/add/<int:film_id>/', views.cart_add, name="cart_add"),
    path('cart/remove/<int:film_id>/', views.cart_remove, name="cart_remove"),
    path('administrator/', views.indexx, name='list_film'),
    path('administrator/create/', views.FilmCreate.as_view(), name='create_film'),
    path('administrator/delete/<int:pk>/', views.FilmDelete.as_view(), name='delete_film'),
    path('administrator/edit/<int:pk>/', views.FilmUpdate.as_view(), name='edit_film'),
    path('cart/validate_coupon/', views.validate_coupon, name='validate_coupon'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)