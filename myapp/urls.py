from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from myapp import views
urlpatterns = [
    path("", views.explored, name='explored'),
    path("index3", views.index3, name='index3'),
    path("next", views.next, name='next'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("register", views.register, name='register'),
    path("booking", views.booking, name='booking'),
    path("connect", views.connect, name='connect'),
    path("room_book", views.room_book, name='room_book'),
    path("payment_page", views.payment_page, name='payment_page'),
    #path('payment-page', views.payment_page),
    path('create_order', views.create_order, name='create_order'),
    path('capture_order', views.capture_order, name='capture_order'),
    path('history', views.history, name='history'),
    path('cancel_booking/<int:id>/', views.cancel_booking, name='cancel_booking'),
    #path('paypal_webhook', views.paypal_webhook, name='paypal_webhook'),
    path('taxi_payment_page', views.taxi_payment_page, name='taxi_payment_page'),
    path('create_taxi_order', views.create_taxi_order, name='create_taxi_order'),
    path('capture_taxi_order', views.capture_taxi_order, name='capture_taxi_order'),
    path('taxi_history', views.taxi_history, name='taxi_history'),
    path('taxi_cancel/<int:id>/', views.taxi_cancel, name='taxi_cancel'),
    path('paypal/webhook/', views.paypal_webhook, name='paypal_webhook'),
    path('profile', views.profile, name='profile'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="password_reset"),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",success_url=reverse_lazy("password_reset_complete")),name="password_reset_confirm"),
    path("reset_done/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),

]

