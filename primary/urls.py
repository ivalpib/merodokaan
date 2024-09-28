from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProdTestView, CategoryTestView

router = DefaultRouter()
router.register(r'anything', ProdTestView)
router.register(r'test', CategoryTestView)
urlpatterns = [
    # path('', views.HomeView, name = 'index'),
    path('login', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),
    path('register', views.RegistrationView, name='register'),
    # path('test/', ProductTestView.as_view({'get': 'list', 'post': 'create'}), name='product-test'),
    # path('', include(router.urls)), # using + router.urls does the same thing
] + router.urls