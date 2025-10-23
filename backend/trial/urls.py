from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, employee_list_ui

router = DefaultRouter()
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),                   # API endpoints
    path('employees-ui/', employee_list_ui, name='employee_list_ui'),  # UI
]
