import random
import string

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render,get_list_or_404
from django.utils import timezone
# from django.views.generics import ListView,DetailView,View
# from .forms import CheckoutForm,CouponForm,RefundForm,PaymentForm


# stripe.api_key=settings.STRIPE_SECRET_KEY

