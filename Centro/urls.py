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
    path('eliminar_cita/<id_cita>', views.eliminar_cita, name="eliminar_cita"),
    path('eliminar_medico/<id_medico>', views.eliminar_medico, name="eliminar_medico"),
    path('eliminar_paciente/<id_paciente>', views.eliminar_paciente, name="eliminar_paciente"),
    path('editar_cita/<id_cita>', views.editar_cita, name="editar_cita"),
    path('editar_medico/<id_medico>', views.editar_medico, name="editar_medico"),
    path('editar_paciente/<id_paciente>', views.editar_paciente, name="editar_paciente"),
    path('crear_cita/', views.crear_cita, name="crear_cita"),
    path('crear_medico/', views.crear_medico, name="crear_medico"),
    path('crear_paciente/', views.crear_paciente, name="crear_paciente"),
    path('pdfAdmin_citas/', views.pdfAdmin_citas, name='pdfAdmin_citas'),
    path('excel_citas/',views.excel_citas,name="excel_citas"),
    path('excel_medicos/',views.excel_medicos,name="excel_medicos"),
    path('excel_pacientes/',views.excel_pacientes,name="excel_pacientes"),
    path('pdfAdmin_medicos/', views.pdfAdmin_medicos, name='pdfAdmin_medicos'),
    path('pdfAdmin_pacientes/', views.pdfAdmin_pacientes, name='pdfAdmin_pacientes'),
    path('no-valido/<str:provincia>/<str:departamento>/', views.NoValido, name='NoValido'),
    path('paciente-pdf/<int:paciente_id>/', views.paciente_pdf, name='paciente_pdf'),
]