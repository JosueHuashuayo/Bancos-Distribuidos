
from django.db import models
from apps.Cliente.models import Cliente 
from apps.Banco.models import Banco  

class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuenta = models.CharField(max_length=10, unique=True)
    numero_cuenta_interbancario = models.CharField(max_length=20, unique=True)
    fecha_apertura = models.DateField()
    activa = models.BooleanField(default=True) 

    def __str__(self):
        return f'{self.numero_cuenta} - {self.banco.nombre} - {self.cliente.nombre}'

    class Meta:
        verbose_name_plural = 'Cuentas'
    def to_json(self):
        cuenta_dict = {
            'cliente': {
                'id': self.cliente.id,
                'nombre': self.cliente.nombre,
                # Agrega otros campos del modelo Cliente si es necesario
            },
            'banco': {
                'id': self.banco.id,
                'nombre': self.banco.nombre,
                # Agrega otros campos del modelo Banco si es necesario
            },
            'saldo': str(self.saldo),  # Convertir Decimal a str
            'numero_cuenta': self.numero_cuenta,
            'numero_cuenta_interbancario': self.numero_cuenta_interbancario,
            'fecha_apertura': str(self.fecha_apertura),  # Convertir Date a str
            'activa': self.activa,
        }
        return cuenta_dict

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('DEPOSITO', 'Depósito'),
        ('RETIRO', 'Retiro'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('TRANSFERENCIA INTERBANCARIA', 'Transferencia Interbancaria')
    ]

    cuenta_origen = models.ForeignKey(Cuenta, related_name='transacciones_origen', on_delete=models.CASCADE)
    cuenta_destino = models.ForeignKey(Cuenta, related_name='transacciones_destino', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_tipo_display()} de {self.cuenta_origen} a {self.cuenta_destino}'
    
    def to_json(self):
        return {
            'cuenta_origen': str(self.cuenta_origen),
            'cuenta_destino': str(self.cuenta_destino),
            'tipo': self.tipo,
            'monto': str(self.monto),
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S'),
        }


    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = 'Transacciones'