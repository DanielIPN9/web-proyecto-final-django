from django.urls import path
from .views import SignUpView, ProfieldUpdate,EmailUpdate

urlpatterns = [
    path('signup/',SignUpView.as_view(), name="signup"),
    path('profile/', ProfieldUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),

]