from django.urls import path
from . import views



urlpatterns = [


    # Index                                                                 
    path('index', views.IndexView.as_view(),  name='index-path'),

    # Rating
    path('thank-you-for-rating', views.ThankYouRatingView.as_view(), name="thank-you-rating-path"),
    path('give_review', views.MakeReviewView.as_view(), name="make-review-path"), 

    # Search
    path('search-results', views.SearchResultView.as_view(), name="search-results-path"),
    path('no-results', views.NoResultView.as_view(), name="no-search-results-path"),

    # Products
    path('all-pumps', views.AllPumpsView.as_view(), name='all-pumps-path'),
    path('all-puffer', views.AllPufferView.as_view(), name='all-puffer-path'),
    path('review_list', views.ReviewListView.as_view(), name='review-list-path'),
    path('puffer/<slug:slug>', views.detail_puffer, name='detail-puffer-path'), 
    path('pump/<slug:slug>', views.detail_pump, name='detail-pump-path'),

    # Pages
    path('about-us/', views.about_us, name='about-us-path'),
    path('landing-page/', views.landing, name='landing-page-path'),

    # Testing
    path('test/', views.TestView.as_view(), name='test-path'),
]   
