"""mywebpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from checkin import views as checkin_module
from dashboard import views as dashboard_module
from student import views as student_module
from subject import views as subject_module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/<teacher>/', checkin_module.checkteachid),
    path('course/<sub>/<int:amt>/<int:stu>/<int:abt>/',
         checkin_module.checkcourse),
    path('checkin/<qrCode>/', checkin_module.checkin),
    path('dashboard', dashboard_module.dashboard),
    path('search/<semisterId>', dashboard_module.searchDailyCheckIn),
    path('student/views', student_module.views),
    path('student/add', student_module.add),
    path('student/edit', student_module.edit),
    path('subject/views', subject_module.views),
    path('subject/add', subject_module.add),
    path('subject/edit', subject_module.edit)
]
