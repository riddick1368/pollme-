from django.urls import path,re_path
from . import views
app_name = "account"
urlpatterns = [
    path('login/',views.login_user,name = "login_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path ("register/",views.registration_form,name = "register")

]