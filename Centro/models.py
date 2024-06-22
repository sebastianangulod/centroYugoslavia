from django.db import models

Especialidades = [('Cardiología','Cardiología'),
        ('Dermatología','Dermatología'),
        ('Neurología','Neurología'),
        ('Pediatría','Pediatría'),
        ('Ginecología','Ginecología')]

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=25, choices=Especialidades)
    Telefono = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Contraseña = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    Dni = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Fecha_nacimiento = models.CharField(max_length=50)
    Genero = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contraseña = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora = models.TimeField()
    especialidad = models.CharField(max_length=25, choices=Especialidades)
    motivo = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=50, default="Pendiente")

    def __str__(self):
        return f"Cita #{self.id_cita}"