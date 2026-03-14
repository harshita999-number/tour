from django.shortcuts import render, redirect
from myapp.models import Booknow, Contact, roomBook
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
#from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest, OrdersCaptureRequest
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
import random




# Create your views here.
def index3(request):
    if request.user.is_anonymous:
        return redirect("/login")
    #messages.success(request, 'Welcome To CoolTrips')
    return render(request, 'index3.html')

from django.conf import settings 
def taxi_payment_page(request):
    taxi_booking_data = request.session.get('taxi_booking_data')
    if not taxi_booking_data:
        messages.error(request, "No Booking data or Booking session expired. please submit booking again.")
        return redirect('/login')
    #print("PAYPAL_CLIENT_ID:", settings.PAYPAL_CLIENT_ID)
    messages.success(request, "Welcome! You are on Taxi Payment Page.")
    return render(request, "taxi_payment.html", {"paypal_client_id": settings.PAYPAL_CLIENT_ID})


#@login_required
def booking(request):
    if request.method == "POST":
       request.session['taxi_booking_data'] = {
       'place' : request.POST.get('place'),
       'member_count' : request.POST.get('member_count'),
       'event_date' : request.POST.get('event_date'),
       }
       #booked = Booknow(place=place, member_count=member, event_date=date)
       #booked.save()

       #request.session['taxi_booking_data'] = {
         #   'place': place,
        #    'member_cout': member,
          #  'event_date': date,
        #}
       return redirect("taxi_payment_page") 
    return redirect('/index3/')


from paypalcheckoutsdk.orders import OrdersCreateRequest
from .paypal_client import client
from django.http import JsonResponse

@csrf_exempt
def create_taxi_order(request):

    taxi_booking_data = request.session.get('taxi_booking_data')

    if not taxi_booking_data:
        return JsonResponse({"error": "No taxi booking data"}, status=400)

    order_request = OrdersCreateRequest()
    order_request.prefer('return=representation')
    order_request.request_body({
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": "15.00"
            }
        }]
    })

    response = client.execute(order_request)

    return JsonResponse({
        "orderID": response.result.id
    })


from paypalcheckoutsdk.orders import OrdersCaptureRequest
from .models import Booknow
import json

@csrf_exempt
def capture_taxi_order(request):

    body = json.loads(request.body)
    order_id = body.get("orderID")

    capture_request = OrdersCaptureRequest(order_id)
    capture_request.request_body({})

    response = client.execute(capture_request)

    capture_id = response.result.purchase_units[0].payments.captures[0].id

    taxi_booking_data = request.session.get('taxi_booking_data')

    if taxi_booking_data:

        Booknow.objects.create(
            user=request.user,
            place=taxi_booking_data['place'],
            member_count=taxi_booking_data['member_count'],
            event_date=taxi_booking_data['event_date'],
            payment_status="Paid",
            paypal_order_id=order_id,
            paypal_capture_id=capture_id
        )

        del request.session['taxi_booking_data']

    return JsonResponse({"status": "success"})

def taxi_history(request):
    if request.user.is_anonymous:
        return redirect("/login")
    bookings = Booknow.objects.all()
    return render(request, "taxi_history.html", {"bookings": bookings})


from paypalcheckoutsdk.payments import CapturesRefundRequest
from datetime import timedelta
from django.utils import timezone
#from django.contrib.auth.decorators import login_required

#@login_required
def taxi_cancel(request, id):

    booking = Booknow.objects.get(id=id)

    if timezone.now() - booking.created_at < timedelta(hours=1):

        refund_request = CapturesRefundRequest(booking.paypal_capture_id)
        refund_request.request_body({
            "amount": {
                "value": "15.00",
                "currency_code": "USD"
            }
        })

        client.execute(refund_request)

        booking.payment_status = "Refunded"
        booking.save()

    else:
        booking.payment_status = "Cancel Time Expired"
        booking.save()

    return redirect('/taxi_history')



from django.conf import settings 
def payment_page(request):
    booking_data = request.session.get('booking_data')
    if not booking_data:
        #print("redirect block running")
        messages.error(request, "No Booking data or Booking session expired. please submit booking again.")
        return redirect('/login')
    #print("render block running")
    messages.success(request, "Welcome! You are on Hotel Payment Page.")
    return render(request, "payment.html", {"paypal_client_id": settings.PAYPAL_CLIENT_ID})

   
   
def room_book(request):
    if request.method == "POST":
       your_name = request.POST.get('your_name')
       your_email = request.POST.get('your_email')
       checkin = request.POST.get('checkin')
       checkout = request.POST.get('checkout')
       guests = request.POST.get('guests')
    
       #if roomBook.objects.filter(your_email=your_email).exists():
            #return render(request,'index3.html',{'error': 'Email already exists please fill form again!'})
       #if roomBook.objects.filter(your_name=your_name).exists():
            #return render(request,'payment.html',{'error': 'This name already exists!'})
       #roombooked = roomBook(your_name=your_name, your_email=your_email, checkin=checkin, checkout=checkout, guests=guests)
       #roombooked.save()

       request.session['booking_data'] = {
            'your_name': your_name,
            'your_email': your_email,
            'checkin': checkin,
            'checkout': checkout,
            'guests': guests,
        }
       return redirect("payment_page")   
    return redirect('/index3/')



from paypalcheckoutsdk.orders import OrdersCreateRequest
from django.http import JsonResponse
from .paypal_client import client
import json

@csrf_exempt
def create_order(request):

    booking_data = request.session.get('booking_data')

    if not booking_data:
        return JsonResponse({"error": "No booking data"}, status=400)

    order_request = OrdersCreateRequest()
    order_request.prefer('return=representation')
    order_request.request_body({
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": "10.00"
            }
        }]
    })

    response = client.execute(order_request)

    return JsonResponse({
        "orderID": response.result.id
    })




from paypalcheckoutsdk.orders import OrdersCaptureRequest
from .models import roomBook

@csrf_exempt
def capture_order(request):

    body = json.loads(request.body)
    order_id = body.get("orderID")

    capture_request = OrdersCaptureRequest(order_id)
    capture_request.request_body({})

    response = client.execute(capture_request)

    capture_id = response.result.purchase_units[0].payments.captures[0].id

    booking_data = request.session.get('booking_data')


    if booking_data:
        
        roomBook.objects.create(
                user=request.user,
                your_name=booking_data['your_name'],
                your_email=booking_data['your_email'],
                checkin=booking_data['checkin'],
                checkout=booking_data['checkout'],
                guests=booking_data['guests'],
                payment_status="Paid",
                paypal_order_id=order_id,
                paypal_capture_id=capture_id
        )

        del request.session['booking_data']

    return JsonResponse({"status": "success"})



def history(request):
    if request.user.is_anonymous:
        return redirect("/login")
    bookings = roomBook.objects.all()#filter(your_email=request.user.email)
    return render(request, "history.html", {"bookings": bookings})



from datetime import timedelta
from django.utils import timezone
from paypalcheckoutsdk.payments import CapturesRefundRequest

def cancel_booking(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    booking = roomBook.objects.get(id=id)

    if timezone.now() - booking.created_at < timedelta(hours=1):

        refund_request = CapturesRefundRequest(booking.paypal_capture_id)
        refund_request.request_body({
            "amount": {
                "value": "10.00",
                "currency_code": "USD"
            }
        })

        client.execute(refund_request)

        booking.payment_status = "Refunded"
        booking.save()

    else:
        booking.payment_status = "Cancel Time Expired"
        booking.save()

    return redirect('/history')



def next(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'next.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')    
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if User.objects.filter(username=username).exists():
            messages.error(request, "This Username is already registered!")
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered!")
            return render(request, 'register.html')
        my_user=User.objects.create_user(username,email,pass1)
        my_user.save()
        messages.success(request, "you registered successfully")
        return redirect("/login")
    return render(request, 'register.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials
        
        username_exists = User.objects.filter(username=username).exists()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome To CoolTrips')
            return redirect("/index3")
        if not username_exists and user is None:
            messages.error(request, 'Invalid Username')
        else:
            messages.error(request, 'Invalid Password')
        return redirect('/login')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def connect(request):
    if request.method == "POST":
       username = request.POST.get('username')
       my_email = request.POST.get('my_email')
       message = request.POST.get('message')
       #if Contact.objects.filter(my_email=my_email).exists():
            #return render(request,'index3.html',{'error': 'Email already exists!'})
       con = Contact(user=request.user, username=username, my_email=my_email, message=message)
       con.save()
    return redirect('/index3')

def explored(request):
    return render(request, 'explored.html')




from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import roomBook, Booknow
import json
from django.http import HttpResponse

@csrf_exempt
def paypal_webhook(request):
  if request.method != "POST":
    return HttpResponse("Invalid request", status=200)
  try:
    data = json.loads(request.body)
        #payload = json.loads(request.body)
        #print("===Webhook Event Received===")
        #print("event_type:",
             #payload.get("event_type"))
        #print("full payload:", payload)
    #except json.JSONDecodeError:
        #print("invalid json received")
   # return HttpResponse(status=200)
    
    event_type = data.get("event_type")
    print("Webhook received:", event_type)

    capture_id = data.get("resource", {}).get("id")

    order_id = data.get("resource", {}).get("supplementary_data",
                                    {}).get("related_ids",
                                    {}).get("order_id")

    if event_type == "CHECKOUT.ORDER.APPROVED":
        order_id = data.get("resource", {}).get("id")

    if not capture_id and not order_id:  
        return JsonResponse({"status": "no i foundd"})

    # Room booking check
    room_booking = roomBook.objects.filter(paypal_capture_id=capture_id).first() or roomBook.objects.filter(paypal_order_id=order_id).first()

    # Taxi booking check
    taxi_booking = Booknow.objects.filter(paypal_capture_id=capture_id).first() or Booknow.objects.filter(paypal_order_id=order_id).first()

    booking = room_booking if room_booking else taxi_booking

    if not booking:
        return JsonResponse({"status": "booking not found"})
  
    if event_type == "CHECKOUT.ORDER.APPROVED":
        booking.payment_status = "Approved"
        booking.paypal_order_id = order_id
        booking.save()

    # ✅ SUCCESS
    elif event_type == "PAYMENT.CAPTURE.COMPLETED":
        booking.payment_status = "Paid"
        booking.paypal_capture_id = capture_id
        booking.save()

    # ❌ FAILED
    elif event_type == "PAYMENT.CAPTURE.DENIED":
        booking.payment_status = "Failed"
        booking.save()

    # 🔄 REFUND
    elif event_type == "PAYMENT.CAPTURE.REFUNDED":
        booking.payment_status = "Refunded"
        booking.save()

    return JsonResponse({"status": "ok"})
  
  except Exception as e:
    print("Webhook Error:", str(e))
    return HttpResponse(status=400)









