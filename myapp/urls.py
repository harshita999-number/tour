from django.contrib import admin
from django.urls import path
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
    path("payment_page/", views.payment_page, name='payment_page'),
    #path('payment-page', views.payment_page),
    path('create_order', views.create_order, name='create_order'),
    path('capture_order', views.capture_order, name='capture_order'),
    path('history', views.history, name='history'),
    path('cancel/<int:id>/', views.cancel_booking, name='cancel_booking'),
    path('paypal_webhook', views.paypal_webhook, name='paypal_webhook'),
    path('taxi_payment_page/', views.taxi_payment_page, name='taxi_payment_page'),
    path('create_taxi_order', views.create_taxi_order, name='create_taxi_order'),
    path('capture_taxi_order', views.capture_taxi_order, name='capture_taxi_order'),
    path('taxi_history', views.taxi_history, name='taxi_history'),
    path('taxi_cancel/<int:id>/', views.taxi_cancel, name='taxi_cancel'),
    path('paypal/webhook/', views.paypal_webhook, name='paypal_webhook'),

]
