"""
URL configuration for pet_adoption project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pet_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('user_reg/',views.user_reg,name='user_reg'),
    path('breeder_reg/',views.breeder_reg,name='breeder_reg'),
    path('veterinary_reg/',views.veterinary_reg,name='veterinary_reg'),
    path('trainer_reg/',views.trainer_reg,name='trainer_reg'),
    path('shop_reg/',views.shop_reg,name='shop_reg'),
    path('login/',views.login,name='login'),
    path('userhome/',views.userhome,name='userhome'),
    path('breederhome/',views.breederrhome,name='breederrhome'),  
    path('veterinaryhome/',views.veterinaryhome,name='veterinaryhome'),
    path('trainerhome/',views.trainerhome,name='trainerhome'),
    path('shophome/',views.shophome,name='shophome'),
    path('shop_product_add/',views.shop_product_add,name='shop_product_add'),
    path('shop_product_delete/<int:id>/',views.shop_product_delete,name='shop_product_delete'),
    path('shop_pet_add/',views.shop_pet_add,name='shop_pet_add'),
    path('user_product_view/',views.user_product_view,name='user_product_view'),
    path('user_pets_view/',views.user_pets_view,name='user_pets_view'),
    path('adopt_pet/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('product_add_quantity/',views.product_add_quantity,name='product_add_quantity'),
    path('user_cart_page/',views.user_cart_page,name='user_cart_page'),
    path('remove_from_cart/',views.remove_from_cart,name='remove_from_cart'),
    path('user_make_payment',views.user_make_payment,name='user_make_payment'),
    path('user_view_bookings/',views.user_view_bookings,name='user_view_bookings'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('user_adoption_request/', views.user_adoption_request, name='user_adoption_request'),
    path('manage_adoption_requests/',views.manage_adoption_requests, name="manage_adoption_requests"),
    path('update_adoption_requests/',views.update_adoption_request, name="update_adoption_request"),
    path('breeder_add_pet/',views.breeder_add_pet,name='breeder_add_pet'),
    path('breeder_adoption_requests/',views.breeder_adoption_requests,name='breeder_adoption_requests'),
    path('update_adoption_requestb/',views.update_adoption_requestb,name='update_adoption_requestb'),
    path('requester_data/',views.requester_data,name='requester_data'),
    path('breeder_chat/',views.breeder_chat,name='user_chat'),
    path('user_view_breeders/',views.user_view_breeders,name='user_view_breeders'),
    path('user_breeder_bookings/',views.user_breeder_bookings,name='user_breeder_bookings'),
    path('breeder_booking_requests/',views.breeder_booking_requests,name='breeder_booking_requests'),
    path('update_booking_status/<int:booking_id>/<str:status>/', views.update_booking_status, name='update_booking_status'),
    path('user_chat/',views.user_chat,name='user_chat'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('admin_view_users/',views.admin_view_users,name='admin_view_users'),
    path('user_update_status/', views.user_update_status, name='user_update_status'),
    path('admin_view_breeders/',views.admin_view_breeders,name='admin_view_breeders'),
    path('breeder_update_status/', views.breeder_update_status, name='breeder_update_status'),
    path('admin_view_shops/',views.admin_view_shops,name='admin_view_shops'),
    path('shop_update_status/', views.shop_update_status, name='shop_update_status'),
]
    # path('breeder_chat/',views.breeder_chat,name='breeder_chat'),
    
   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)