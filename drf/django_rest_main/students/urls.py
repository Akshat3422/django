from django.urls import path
from . import views


urlpatterns = [
    path('', views.students, name="student-list"),
    path('<int:id>/', views.get_student_detail, name="student-detail"),
    path('employees/',views.Employees.as_view()),
    path('employees/<str:pk>',views.Employees.as_view())
    
]