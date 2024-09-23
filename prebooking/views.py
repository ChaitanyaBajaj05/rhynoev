from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
import paypalrestsdk

# Configure PayPal
paypalrestsdk.configure({
    "mode": "sandbox",  # Sandbox mode for demo
    "client_id": "AX8ocAnnloUCe1iVxPcybI0OLtepZ88R483jQ0jDJg8PjolWg1bs9KXjE02-MBTKVzsp__t8Am5wy5KK",
    "client_secret": "EC44gZV3reBdbEjke9Jbm5Th_d3BDZ4nlfS4baLcoPd6dKQAI6q5_XbA-n4x6b1fqzzZ2eEP6BVYA-_b"
})

def pre_book(request):
    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        vehicle = request.POST.get('vehicle')
        amount = request.POST.get('amount')

        # Create a PayPal payment
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [{
                "amount": {"total": amount, "currency": "USD"},
                "description": f"Pre-booking for {vehicle}"
            }],
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/pre-booking/paypal/success/'),
                "cancel_url": request.build_absolute_uri('/pre-booking/paypal/cancel/')
            }
        })

        if payment.create():
            # Redirect to PayPal for payment
            for link in payment.links:
                if link.rel == 'approval_url':
                    return redirect(link.href)
        else:
            return JsonResponse({'error': 'Payment creation failed'}, status=500)
    
    return render(request, 'prebooking/pre_book.html')

def paypal_success(request):
    return render(request, 'prebooking/paypal_success.html')

def paypal_cancel(request):
    return render(request, 'prebooking/paypal_cancel.html')
