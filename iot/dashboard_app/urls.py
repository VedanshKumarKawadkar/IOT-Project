from dashboard_app import views
from django.urls import path

urlpatterns = [
    path("", view=views.login_signup_page, name="test"),
    path("login", view=views.login, name="login"),
    path("signup", view=views.signup, name="signup"),
    path("dashboard", view=views.dashboard, name="dashboard")
]
