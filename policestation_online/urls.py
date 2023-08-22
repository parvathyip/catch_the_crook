"""
URL configuration for policestation_online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from station_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('users-login/',views.users_login),
    path('public-newmissingcase/',views.public_newmissingcase),
    path('public-newcomplaintcase/',views.public_newcomplaintcase),
    #admin
    path('admin-dashboard/',views.admin_dashboard),
    path('admin-adddgp/',views.admin_adddgp),
    path('admin-viewdgp/',views.admin_viewdgp),
    
    # path('admin-deletedgp/',views.admin_deletedgp),
    #dgp
    path('dgp-dashboard/',views.dgp_dashboard),
    path('dgp-addstation/',views.dgp_addstation),
    path('dgp-viewprofile/',views.dgp_viewprofile),
    path('dgp-updatedgp/',views.dgp_updatedgp),
    path('dgp-viewhistories/',views.dgp_viewhistories),
    #station
    path('station-dashboard/',views.station_dashboard),
    path('station-addwantedcriminal/',views.station_addwantedcriminal),
    path('station-viewcomplaints',views.station_viewcomplaints),
    path('station-viewmissings',views.station_viewmissings),
    path('station-registercomplaint',views.station_registercomplaint),
    path('station-withdrawcomplaint',views.station_withdrawcomplaint),
    path('station-viewregistered',views.station_viewregistered),
    path('station-viewcriminals/',views.station_viewcriminals),
    path('station-viewcriminaldetail/',views.station_viewcriminaldetail),
    path('station-searchcriminal/',views.station_searchcriminal),
    path('station-viewsearchcriminaldetail',views.station_viewsearchcriminaldetail),
    path('station-arrest/',views.station_arrest),
    path('station-viewarrested/',views.station_viewarrested),
    path('station-viewwithdrawed/',views.station_viewwithdrawed),
    path('station-missings/',views.station_missings),
    path('station-addwitness/',views.station_addwitness),
    path('station-closecase/',views.station_closecase),
    path('station-viewclosed/',views.station_viewclosed),
    #public
    path('public-dashboard/',views.public_dashboard),
    path('public-addcomplaint/',views.public_addcomplaint),
    path('public-register/',views.public_register),
    path('public-addmissing/',views.public_addmissing),
    path('public-addcomplaint/',views.public_addcomplaint),
    path('public-viewcomplaints/',views.public_viewcomplaints),
    path('public-viewcriminals/',views.public_viewcriminals),
    path('public-viewcriminaldetail/',views.public_viewcriminaldetail),
    path('public-haveaccount/',views.public_haveaccount),
    path('public-addfeedback/',views.public_addfeedback),
    path('public-viewfeedbacks',views.public_viewfeedbacks),
]
