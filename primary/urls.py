from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductView, CategoryView, testClassView

router = DefaultRouter()
router.register(r'product', ProductView)
router.register(r'category', CategoryView)
urlpatterns = [
    path('login', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),
    path('register', views.RegistrationView, name='register'),
    # path('test/', ProductView.as_view({'get': 'list', 'post': 'create'}), name='product-test'),
    # path('', include(router.urls)), # using + router.urls does the same thing
    path('functionapi', views.testView , name="function-based"),
    path('functionapi/<int:pk>', views.testView , name="function-based-pk"),
    path('classapi', testClassView.as_view(), name ="django-class-based"),
] + router.urls