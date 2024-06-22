from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # Verificar si la solicitud es para el inicio de sesión o el registro
        if 'login_email' in request.POST and 'login_contrasena' in request.POST:
            email = request.POST.get('login_email')
            contrasena = request.POST.get('login_contrasena')
            try:
                useradmin = User.objects.get(email=email)
                if useradmin:
                    messages.success(request, 'Inicio de sesión de administrador exitoso.')
                    login(request,useradmin)
                    request.session['is_logged_in'] = True
                    return redirect('citas_admin')
            except:
                pass
            paciente = Paciente.objects.filter(Email=email, Contraseña=contrasena).first()

            if paciente:
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('ver_citas', paciente_id=paciente.id_paciente)
            else:
                messages.error(request, 'Correo electrónico o contraseña incorrectos.')

        else:
            dni = request.POST.get('dni')
            Nombre = request.POST.get('nombre')
            Apellido = request.POST.get('apellido')
            Fecha_nacimiento = request.POST.get('fecha_nacimiento')
            Genero = request.POST.get('genero')
            Direccion = request.POST.get('direccion')
            Telefono = request.POST.get('telefono')
            Email = request.POST.get('email')
            Contraseña = request.POST.get('contrasena')

            # Verificar si el DNI ya está registrado
            if Paciente.objects.filter(Dni=dni).exists():
                messages.error(request, 'El DNI ya está registrado.')
                return redirect('login')

            # Crear un nuevo objeto Paciente
            paciente = Paciente.objects.create(
                Dni=dni,
                Nombre=Nombre,
                Apellido=Apellido,
                Fecha_nacimiento=Fecha_nacimiento,
                Genero=Genero,
                Direccion=Direccion,
                Telefono=Telefono,
                Email=Email,
                Contraseña=Contraseña
            )
            paciente.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('login')
    return render(request, 'index.html')

def usuario_citas(request, paciente_id):
    admin=User.objects.all()
    print(admin[0].username)
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    cita = Cita.objects.filter(paciente=paciente)
    context = {'cita': cita, 'paciente':paciente}
    return render(request, 'usuariocitas.html', context)


def usuario_registro(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        especialidad = request.POST.get('especialidad')
        medico = request.POST.get('Medico')
        Fechadedisponibilidad = request.POST.get('Fechadedisponibilidad')
        hora = request.POST.get('hora')
        Motivo = request.POST.get('Motivo')
        select_medico = Medico.objects.get(Nombre=medico)
        paciente = Paciente.objects.get(Dni=dni)
        cita = Cita.objects.create(
            medico = select_medico,
            paciente = paciente,
            fecha_cita = Fechadedisponibilidad,
            hora = hora,
            especialidad = especialidad,
            motivo = Motivo
        )
        cita.save()
        messages.success(request, 'Registro exitoso.')
        return redirect('ver_citas')
    Medicos=Medico.objects.all()
    return render(request, 'usuarioregistro.html', context={'medicos':Medicos})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required()
def citas_admin(request):
    cita = Cita.objects.all()
    context = {'cita': cita}
    return render(request, 'citasadmin.html', context)