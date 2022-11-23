from django.shortcuts import render, redirect

from rest_framework.views import APIView
# Create your views here.
import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
webhook_secret = settings.STRIPE_WEBHOOK_SECRET
YOUR_DOMAIN = settings.STRIPE_FRONTEND_DOMAIN
FRONTEND_SUBSCRIPTION_SUCCESS_URL = settings.SUBSCRIPTION_SUCCESS_URL
FRONTEND_SUBSCRIPTION_CANCEL_URL = settings.SUBSCRIPTION_FAILED_URL


class CreateSubscription(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': request.data['app_id'],
                        'quantity': 1
                    }
                ],
                mode='subscription',
                success_url=FRONTEND_SUBSCRIPTION_SUCCESS_URL,
                cancel_url=FRONTEND_SUBSCRIPTION_CANCEL_URL)
            return redirect(checkout_session.url, code=303)
        except Exception as err:
            msg = "Exception Error"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            resp_json = {"message": msg, "status_code": status_code}
            return Response(resp_json, status=status_code)


class webhook(APIView):
    def post(self, request):
        """
            This API handling the webhook .
            :return: returns event details as json response .
        """
        request_data = json.loads(request.body)
        # print(request_data)
        if webhook_secret:
            # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
            signature = request.META['HTTP_STRIPE_SIGNATURE']
            print("❤️❤️❤️❤️❤️",webhook_secret)
            print()
            try:
                event = stripe.Webhook.construct_event(
                    payload=request.body, 
                    sig_header=signature, 
                    secret=webhook_secret
                    )
                data = event['data']
            except ValueError as err:
                pass
                # raise err
            # except stripe.error.SignatureVerificationError as err:
            #     raise err
            # Get the type of webhook event sent - used to check the status of PaymentIntents.
            event_type = event['type']
        else:
            data = request_data['data']
            event_type = request_data['type']
        data_object = data['object']

        print(">>>>>>>>>>>>>>>>>> \n\n",event['type'])
        if event_type == 'payment_intent.succeeded':
        # Payment is successful and the subscription is created.
        # You should provision the subscription and save the customer ID to your database.
            print("-----checkout.session.completed----->",data['object']['customer'])
        elif event_type == 'invoice.paid':
        # Continue to provision the subscription as payments continue to be made.
        # Store the status in your database and check when a user accesses your service.
        # This approach helps you avoid hitting rate limits.
            print("-----invoice.paid----->", data)
        elif event_type == 'invoice.payment_failed':
        # The payment failed or the customer does not have a valid payment method.
        # The subscription becomes past_due. Notify your customer and send them to the
        # customer portal to update their payment information.
            print("-----invoice.payment_failed----->",data)
        else:
            print('Unhandled event type {}'.format(event_type))
        
        return Response(200)