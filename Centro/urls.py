from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('ver_citas/<paciente_id>', views.usuario_citas, name='ver_citas'),
    path('registrar_citas/', views.usuario_registro, name="registrar_citas"),
    path('cerrar_sesion/',views.cerrar_sesion, name="cerrar_sesion"),
    path('citas_admin/',views.citas_admin, name="citas_admin"),
    path('pacientes_admin',views.pacientes_admin, name="pacientes_admin"),
    path('main_admin/',views.main_admin, name="main_admin"),
    path('medicos_admin/', views.medicos_admin, name="medicos_admin"),
]