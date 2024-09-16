from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ProductTestView, CategoryTestView

router = routers.DefaultRouter()
router.register(r'test', ProductTestView)
urlpatterns = [
    # path('', views.HomeView, name = 'index'),
    path('login', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),
    path('register', views.RegistrationView, name='register'),
    # path('test/', ProductTestView.as_view({'get': 'list', 'post': 'create'}), name='product-test'),
    path('', include(router.urls)),
]