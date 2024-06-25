from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.urls import reverse
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
                    return redirect('main_admin')
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
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    cita = Cita.objects.filter(paciente=paciente)
    context = {'cita': cita, 'paciente':paciente, 'id':paciente_id}
    return render(request, 'Usuario.html', context)


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
        return redirect(reverse('ver_citas', args=[paciente.id_paciente]))
    Medicos=Medico.objects.all()
    return render(request, 'Rcitas.html', context={'medicos':Medicos})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def main_admin(request):
    citas=Cita.objects.all()
    return render(request, 'Admin.html', context={'citas':citas})

@login_required
def citas_admin(request):
    citas = Cita.objects.all()
    context = {'citas': citas}
    return render(request, 'citas.html', context)

@login_required
def pacientes_admin(request):
    pacientes = Paciente.objects.all()
    print(pacientes)
    context = {'pacientes': pacientes}
    return render(request, 'Pacient.html', context)

@login_required
def medicos_admin(request):
    medicos= Medico.objects.all()
    context = {'medicos':medicos}
    return render(request, 'Especiali.html', context)

def eliminar_cita(request,id_cita):
    cita = Cita.objects.get(id_cita=id_cita)
    cita.delete()
    messages.success(request, 'Cita eliminada.')
    return redirect('citas_admin')

def eliminar_medico(request,id_medico):
    medico = Medico.objects.get(id_medico=id_medico)
    medico.delete()
    messages.success(request, 'Medico eliminado.')
    return redirect('medicos_admin')

def eliminar_paciente(request,id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    paciente.delete()
    messages.success(request, 'Paciente eliminado.')
    return redirect('pacientes_admin')

def crear_paciente(request):
    if request.method == 'POST':
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
        return redirect('pacientes_admin')
    return render(request, 'Crear_paciente.html')

def crear_cita(request):
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
        return redirect('citas_admin')
    Medicos=Medico.objects.all()
    return render(request, 'Crear_cita.html', context={'medicos':Medicos})

def crear_medico(request):
    if request.method == 'POST':
        Nombre = request.POST.get('nombre')
        Apellido = request.POST.get('apellido')
        especialidad = request.POST.get('especialidad')
        Telefono = request.POST.get('telefono')
        Email = request.POST.get('email')
        Contraseña = request.POST.get('contrasena')

        # Crear un nuevo objeto Medico
        medico = Medico.objects.create(
            Nombre=Nombre,
            Apellido=Apellido,
            especialidad=especialidad,
            Telefono=Telefono,
            Email=Email,
            Contraseña=Contraseña
        )
        medico.save()
        messages.success(request, 'Registro exitoso.')
        return redirect('medicos_admin')
    return render(request, 'Crear_medico.html')

def editar_paciente(request,id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    if request.method == 'POST':
        paciente.Dni = request.POST.get('dni')
        paciente.Nombre = request.POST.get('nombre')
        paciente.Apellido = request.POST.get('apellido')
        paciente.Fecha_nacimiento = request.POST.get('fecha_nacimiento')
        paciente.Genero = request.POST.get('genero')
        paciente.Direccion = request.POST.get('direccion')
        paciente.Telefono = request.POST.get('telefono')
        paciente.Email = request.POST.get('email')
        paciente.Contraseña = request.POST.get('contrasena')
        paciente.save()
        messages.success(request, 'Paciente editado.')
        return redirect('pacientes_admin')
    return render(request, 'Editar_paciente.html', context={'paciente':paciente})

def editar_medico(request,id_medico):
    medico = Medico.objects.get(id_medico=id_medico)
    if request.method == 'POST':
        medico.Nombre = request.POST.get('nombre')
        medico.Apellido = request.POST.get('apellido')
        medico.especialidad = request.POST.get('especialidad')
        medico.Telefono = request.POST.get('telefono')
        medico.Email = request.POST.get('email')
        medico.Contraseña = request.POST.get('contrasena')
        medico.save()
        messages.success(request, 'Medico editado.')
        return redirect('medicos_admin')
    return render(request, 'Editar_medico.html', context={'medico':medico})

def editar_cita(request,id_cita):
    cita = Cita.objects.get(id_cita=id_cita)
    if request.method == 'POST':
        cita.medico = Medico.objects.get(Nombre=request.POST.get('Medico'))
        cita.paciente = Paciente.objects.get(Dni=request.POST.get('dni'))
        cita.fecha_cita = request.POST.get('Fechadedisponibilidad')
        cita.hora = request.POST.get('hora')
        cita.especialidad = request.POST.get('especialidad')
        cita.motivo = request.POST.get('Motivo')
        cita.estado = request.POST.get('estado')
        cita.save()
        messages.success(request, 'Cita editada.')
        return redirect('citas_admin')
    Medicos=Medico.objects.all()
    return render(request, 'Editar_cita.html', context={'cita':cita, 'medicos':Medicos})