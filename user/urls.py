from django.urls import path
from . import views
from .views import UserDataUpload


urlpatterns = [
  path("data/",UserDataUpload.as_view()  ,name = "Post Data"),
  path("check_username/",views.check_username,name = "Check Username"),
  path("delete_account/<str:username>/",views.delete_account,name = "Delete Account"),
  path("login/<str:mail>/",views.login,name = "Login"),
  path("check_mail/<str:mail>/",views.check_email,name = "Check Mail")
]