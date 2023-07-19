from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from .models import Pump, Review, Puffer

from .forms import ReviewForm
from django.http import HttpResponseRedirect

from django.views import View
from django.views.generic.base import TemplateView

from django.core.mail import send_mail
from django.conf import settings


# Search
""" only called bi the search bar under action """


class SearchResultView(View):
    def get(self, request):
        return render(request, "shop/search-results.html")

    def post(self, request):
        searched_data = request.POST["search_field"]
        print("{{{{{{{{INFO}}}}}}}} - SEARCHED FOR:", searched_data)

        if Pump.objects.all().filter(model__contains=searched_data) or Puffer.objects.all().filter(model__contains=searched_data):
            matched_data = Pump.objects.all().filter(model__contains=searched_data)
            matched_data_2 = Puffer.objects.all().filter(model__contains=searched_data)

            return render(request, "shop/search-results.html", {
                "matched_data": matched_data,
                "matched_data_2": matched_data_2,
                "searched_data": searched_data,
            })

        else:
            return render(request, "shop/search-results.html", {
                "searched_data": searched_data,
                "no_result": True
            })


class NoResultView(TemplateView):
    template_name = "shop/no-search-results.html"


# Index

class IndexView(View):

    def get(self, request):
        pumps = Pump.objects.all().order_by("-price")
        pump_block_1 = pumps[:3]
        pump_block_2 = pumps[3:6]

        puffers = Puffer.objects.all().order_by("-price")
        puffer_block_1 = puffers[:3]
        puffer_block_2 = puffers[3:]
        return render(request, 'shop/index.html', {
            "pumps": pumps,
            "pump_block_1": pump_block_1,
            "pump_block_2": pump_block_2,
            "puffers": puffers,
            "puffer_block_1": puffer_block_1,
            "puffer_block_2": puffer_block_2,

        })


# Products

class AllPumpsView(View):

    def get(self, request):
        return render(request, 'shop/all-pumps.html', {
            "all_pumps": Pump.objects.all()
        })


class AllPufferView(View):

    def get(self, request):
        return render(request, 'shop/all-puffer.html', {
            "all_puffer": Puffer.objects.all()
        })

    def post(self, request):
        searched_data = request.POST["search_field"]  # fetch data from <input>

        matched_data = Puffer.objects.all().filter(model__contains=searched_data)

        return render(request, "shop/search-results.html", {
            "matched_data": matched_data
        })


def detail_pump(request, slug):
    pump = get_object_or_404(Pump, slug=slug)

    return render(request, 'shop/detail-pump.html', {
        "pump": pump
    })


def detail_puffer(request, slug):
    puffer = get_object_or_404(Puffer, slug=slug)

    return render(request, 'shop/detail-puffer.html', {
        "puffer": puffer
    })


# Ratings

class ReviewListView(TemplateView):
    template_name = 'shop/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fetched_data = Review.objects.all()
        context["fetched_data"] = fetched_data
        return context


class MakeReviewView(View):

    def get(self, request):
        form = ReviewForm
        return render(request, 'shop/give_review.html', {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you-for-rating')
        return render(request, 'shop/give_review.html', {
            "form": form
        })


class ThankYouRatingView(TemplateView):
    template_name = "shop/after-review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Marcus"
        return context


# Pages
def about_us(request):
    return render(request, 'shop/pages/page-about-us.html')
