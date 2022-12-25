from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_image_size(image):
    min_width = 700
    max_width = 1000
    min_height = 700
    max_height = 1000

    error_min_width = False
    error_max_width = False
    error_min_height = False
    error_max_height = False

    error_message_min_width = 'El ancho es menor al mínimo aceptado'
    error_message_max_width = 'El ancho es mayor al máximo aceptado'
    error_message_min_height = 'La altura es menor al mínimo aceptado'
    error_message_max_height = 'La altura es mayor al máximo aceptado'

    error_message = ''

    if image.width < min_width:
        error_min_width = True
        error_message+='\n'+error_message_min_width+'('+str(image.width)+'px).'
    if max_width < image.width:        
        error_max_width = True
        error_message+='\n'+error_message_max_width+'('+str(image.width)+'px).'
    if image.height < min_height:        
        error_min_height = True
        error_message+='\n'+error_message_min_height+'('+str(image.height)+'px).'
    if max_height < image.height:        
        error_max_height = True
        error_message+='\n'+error_message_max_height+'('+str(image.height)+'px).'
        
    if error_min_width or error_max_width or error_min_height or error_max_height:
        raise ValidationError(
            [f'{error_message}\nEl tamaño de imagen debe cumplir con ancho entre {min_width} y {max_width} pixeles, y altura entre {min_height} y { max_height} pixeles.']
            )

def validar_dimensiones_imagen(image):
    min_width = 700
    max_width = 1000
    min_height = 700
    max_height = 1000

    error_min_width = False
    error_max_width = False
    error_min_height = False
    error_max_height = False

    error_message_min_width = 'El ancho es menor al mínimo aceptado'
    error_message_max_width = 'El ancho es mayor al máximo aceptado'
    error_message_min_height = 'La altura es menor al mínimo aceptado'
    error_message_max_height = 'La altura es mayor al máximo aceptado'

    error_message = ''

    if image.width < min_width:
        error_min_width = True
        error_message+='\n'+error_message_min_width+'('+str(image.width)+'px).'
    if max_width < image.width:        
        error_max_width = True
        error_message+='\n'+error_message_max_width+'('+str(image.width)+'px).'
    if image.height < min_height:        
        error_min_height = True
        error_message+='\n'+error_message_min_height+'('+str(image.height)+'px).'
    if max_height < image.height:        
        error_max_height = True
        error_message+='\n'+error_message_max_height+'('+str(image.height)+'px).'
        
    if error_min_width or error_max_width or error_min_height or error_max_height:
        raise ValidationError(
            [f'{error_message}\nEl tamaño de imagen debe cumplir con ancho entre {min_width} y {max_width} pixeles, y altura entre {min_height} y { max_height} pixeles.']
            )

def validar_dimensiones_foto(foto):

    error_escala = False
    if foto.width == None or foto.height== None:
        raise ValidationError(
            [f'Ingrese una imagen información válida.']
            )

    if foto.width/foto.height < 0.9 or foto.width/foto.height > 1.1:
        error_escala = True
    if error_escala:
        raise ValidationError(
            [f'El tamaño de imagen debe cumplir con una escala entre ancho y altura de entre 0.9 y 1.1']
            )

def validar_numero_entero(precio_total:str):
    try:
        int(precio_total) 
    except:
        raise ValidationError(
            [f'Solo se permiten valores enteros.']
            )

def validar_nombre_producto(nombre:str):
    error_isnotalpha = False
    error_message_isnotalpha = 'El nombre no debe poseer carácteres extraños '
    error_message = ''
    if not nombre.isalpha():
        error_isnotalpha = True
        error_message+='\n'+error_message_isnotalpha+'('+str(nombre)+').'
            
    if error_isnotalpha:
        raise ValidationError(
            [f'{error_message} El nombre debe ser solo alfabético.']
            )

def validar_tipo_producto(tipo:str):
    tipos = ["vasija","macetero","planta"]
    
    error_isnotvalid = False
    error_message_isnotvalid = 'No es un tipo válido.'
    error_message = ''

    if not tipo in tipos:
        error_isnotvalid = True
        error_message+='\n'+error_message_isnotvalid+'('+str(tipo)+').'
            
    if error_isnotvalid:
        raise ValidationError(
            [f'{error_message}\n.Ingrese: "vasija", "macetero" o "planta".']
            )


class Producto(models.Model):

    tipos = [
        ('vasija','vasija'),
        ('macetero','macetero'),
        ('planta','planta'),
        ]

    tipo = models.CharField(    max_length=100,
                                choices=tipos,
                                validators=[validar_tipo_producto])
    nombre = models.CharField(  max_length=100)
    precio = models.IntegerField(validators=[validar_numero_entero])
    descripcion = models.CharField(max_length=1024)
    imagen = models.ImageField(upload_to='productos', 
                                null=True, blank=True,
                                validators=[validar_dimensiones_imagen],)
    activo = models.BooleanField(default=True)


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(validators=[validar_numero_entero])
    descripcion = models.CharField(max_length=1024)
    imagen = models.ImageField(upload_to='servicios', 
                                null=True, blank=True,
                                validators=[validar_dimensiones_imagen],)
    activo = models.BooleanField(default=True)


class PedidoCarrito(models.Model):

    estados = [
        ('En espera','En espera'),
        ('Pagar','Pagar'),
        ('Pagado','Pagado'),
        ('Retirado','Retirado')
        ]

    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_retiro = models.DateField(null=True, blank=True)
    precio_total = models.IntegerField(null=True, blank=True, validators=[validar_numero_entero])
    estado = models.CharField( max_length=100,
                                choices=estados, default='En espera')


class CarritoBoleta(models.Model):
    tipos = [
        ('vasija','vasija'),
        ('macetero','macetero'),
        ('planta','planta'),
        ]
    carrito = models.IntegerField(null=True, blank=True, validators=[validar_numero_entero])
    producto = models.CharField( max_length=100)
    tipo = models.CharField(    max_length=100,
                                choices=tipos,
                                validators=[validar_tipo_producto])
    imagen = models.ImageField(upload_to='boletas', 
                                null=True, blank=True,
                                validators=[validar_dimensiones_imagen],)
    precio = models.IntegerField(validators=[validar_numero_entero])
    cantidad = models.IntegerField(validators=[validar_numero_entero])


class PedidoServicio(models.Model):

    estados = [
        ('En espera','En espera'),
        ('Realizar Primer Pago','Realizar Primer Pago'),
        ('Pagado Primer Pago','Pagado Primer Pago'),
        ('Realizar Segundo Pago','Realizar Segundo Pago'),
        ('Pagado Segundo Pago','Pagado Segundo Pago'),
        ('Finalizado','Finalizado')
        ]

    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_termino = models.DateField(null=True, blank=True)
    terminos_acordados = models.CharField(max_length=1024, null=True, blank=True)
    precio_total = models.IntegerField(validators=[validar_numero_entero])
    estado = models.CharField( max_length=100,
                                choices=estados, default='En espera')


class DatosCuenta(models.Model):
    usuario = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    apellido = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)


class Testimonio(models.Model):
    foto = models.ImageField(upload_to='testimonios', 
                                null=True, blank=True,
                                validators=[validar_dimensiones_foto],)
    nombre_cliente = models.CharField(max_length=1024)
    profesion_cliente = models.CharField(max_length=1024)
    testimonio_cliente = models.CharField(max_length=1024)


class ItemCarrusel(models.Model):
    foto = models.ImageField(upload_to='carrusel', 
                                null=True, blank=True,
                                validators=[validar_dimensiones_imagen],)
    item_titulo = models.CharField(max_length=1024)
    item_parrafo = models.CharField(max_length=1024)


 