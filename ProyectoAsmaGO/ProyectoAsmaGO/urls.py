# """ProyectoAsmaGO URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import static
# from AsmaGOwebapp import views
# from ProyectoAsmaGO import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('addData',views.addData,name='add_data'),
#     path('add_student',views.add_student, name='add_student'),
#     path('show_all_data',views.show_all_data,name='show_all_data'),
#     path('update_student/<str:student_id>',views.update_student,name="update_student"),
#     path('edit_student', views.edit_student, name="edit_student"),
#     path('delete_student/<str:student_id>', views.delete_student, name="delete_student"),
#     path('register/',views.RegisterUser,name="register"),
#     path('login_user/', views.LoginUser, name="login_user"),
#     path('save_user',views.SaveUser,name="save_user"),
#     path('do_loginn_user',views.DoLoginUser,name="do_login_user"),
#     path('homePage/',views.HomePage,name="homepage"),
#     path('logout/',views.LogoutUser,name="logout"),
#     path('exercises/<str:student_id>',views.exercises,name='exercises'),
#     ]
  
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from AsmaGOwebapp import views
from ProyectoAsmaGO import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage,name="home"),
    path('insert_student', views.InsertStudent,name="insert"),
    path('update_all', views.update_all,name="update_all"),
    path('delete_data', views.delete_data,name="delete_data"),
    path('exercises/<str:student_id>',views.exercises,name='exercises'),
]