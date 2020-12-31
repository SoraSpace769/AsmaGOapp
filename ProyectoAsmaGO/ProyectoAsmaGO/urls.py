
  
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from AsmaGOwebapp import views
from ProyectoAsmaGO import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPageController, name="index_page"),
    path('homePage/',views.HomePage,name="homepage"),
    path('insert_student', views.InsertStudent,name="insert"),
    path('update_all', views.update_all,name="update_all"),
    path('delete_data', views.delete_data,name="delete_data"),
    path('exercises/<str:student_id>/',views.exercises,name='exercises'),
    path('register_user/',views.RegisterUser,name="register_user"),
    path('login_user/', views.LoginUser, name="login_user"),
    path('save_user',views.SaveUser,name="save_user"),
    path('do_loginn_user',views.DoLoginUser,name="do_login_user"),
    path('logout/',views.LogoutUser,name="logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)