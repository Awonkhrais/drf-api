from django.urls import path


from .views import CoffeeDetailsView, CoffeeListView

urlpatterns = [
    path('', CoffeeListView.as_view(), name='coffecurve_api'), 
    path('/<int:pk>', CoffeeDetailsView.as_view(),name='coffecurve_details_api'),  
]