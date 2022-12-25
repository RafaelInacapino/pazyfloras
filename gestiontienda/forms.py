from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm, UsernameField
from tienda.models import Producto, Servicio, PedidoCarrito, PedidoServicio
from django.contrib.auth.models import User

class ProductoForm(ModelForm):

    class_attr_inputs = 'form-control input_for_form mt-2 bg-light bg-gradient border-0'
    tipos = [
        ('vasija','vasija'),
        ('macetero','macetero'),
        ('planta','planta'),
        ]

    tipo = forms.CharField(label=("Tipo de Producto *"),
                widget=forms.Select(attrs={'class':class_attr_inputs,'placeholder':'Elegir el tipo de producto'},choices=tipos),
                help_text=(""))

    nombre = forms.CharField(label=("Nombre *"),
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar el nombre a mostrar del producto'}),
                help_text=(""))

    precio = forms.IntegerField(label="Precio del Producto (CLP) *",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del producto'}),
                help_text=(""))
    
    descripcion = forms.CharField(label=("Descripción *"),
                widget=forms.Textarea(attrs={'class':class_attr_inputs,'placeholder':'Ingresar la descripción del producto','rows':'3'}),
                help_text=(""))

    imagen = forms.ImageField(label="Imagen del Producto *",
                widget=forms.FileInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del producto'}),
                help_text=(""),required=False)
    
    activo = forms.BooleanField(label='Activo',widget=forms.CheckboxInput(attrs={'class':'form-control input_for_form mt-2 form-check-input','checked':''}),required=False)

    class Meta:
        model = Producto
        fields = '__all__'


class ServicioForm(ModelForm):

    class_attr_inputs = 'form-control input_for_form mt-2'

    nombre = forms.CharField(label=("Nombre *"),
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar el nombre a mostrar del servicio'}),
                help_text=(""))

    precio = forms.IntegerField(label="Precio del Servicio (CLP) *",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del servicio'}),
                help_text=(""))
    
    descripcion = forms.CharField(label=("Descripción *"),
                widget=forms.Textarea(attrs={'class':class_attr_inputs,'placeholder':'Ingresar la descripción del servicio','rows':'3'}),
                help_text=(""))

    imagen = forms.ImageField(label="Imagen del Servicio *",
                widget=forms.FileInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del servicio'}),
                help_text=(""),required=False)
    
    activo = forms.BooleanField(label='Activo',widget=forms.CheckboxInput(attrs={'class':class_attr_inputs+' form-check-input','checked':''}), required=False)

    class Meta:
        model = Servicio
        fields = '__all__'


class PedidoCarritoForm(ModelForm):

    class_attr_inputs = 'form-control input_for_form mt-2'

    precio_total = forms.IntegerField(label="Precio del Servicio (CLP)",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del pedido',}),
                help_text=(""))

    class Meta:
        model = PedidoCarrito
        fields = '__all__'

class PedidoCarritoFormEditar(PedidoCarritoForm):

    class Meta:
        model = PedidoCarrito
        fields = ['fecha_creacion','fecha_retiro','precio_total','estado']

    class_attr_inputs = 'form-control input_for_form mt-2'

    estados = [
        ('En espera','En espera'),
        ('Pagar','Pagar'),
        ('Pagado','Pagado'),
        ('Retirado','Retirado')
        ]

    estado = forms.CharField(label=("Estado del Pedido"),
                widget=forms.Select(attrs={'class':class_attr_inputs,'placeholder':'Elegir el tipo de producto',},choices=estados),
                help_text=(""),required=True)

    fecha_creacion = forms.DateField(label=("Fecha de creación"),
                widget=forms.DateInput(attrs={'class':class_attr_inputs, 'readonly':True, 'readonly':True}),required=False)
    
    fecha_retiro = forms.DateField(label=("Fecha de retiro"),
                widget=forms.DateInput(attrs={'class':class_attr_inputs}),required=True)
        
    
    precio_total = forms.IntegerField(label="Precio del Carrito (CLP)",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del pedido','readonly':True},),
                help_text=(""),required=False)



class PedidoServicioForm(ModelForm):

    class_attr_inputs = 'form-control input_for_form mt-2'

    precio_total = forms.IntegerField(label="Precio del Servicio (CLP) *",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del pedido'}),
                help_text=(""))

    class Meta:
        model = PedidoServicio
        fields = '__all__'

class PedidoServicioFormEditar(PedidoServicioForm):
    class_attr_inputs = 'form-control input_for_form mt-2'

    estados = [
        ('En espera','En espera'),
        ('Realizar Primer Pago','Realizar Primer Pago'),
        ('Pagado Primer Pago','Pagado Primer Pago'),
        ('Realizar Segundo Pago','Realizar Segundo Pago'),
        ('Pagado Segundo Pago','Pagado Segundo Pago'),
        ('Finalizado','Finalizado')
        ]

    estado = forms.CharField(label=("Estado del Pedido"),
                widget=forms.Select(attrs={'class':class_attr_inputs},choices=estados),
                help_text=(""),required=True)

    nombre = forms.CharField(label=("Servicio"),
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'readonly':True}),required=False)

    terminos_acordados = forms.CharField(label=("Términos acordados"),
                widget=forms.Textarea(attrs={'class':class_attr_inputs,'placeholder':'Ingrese los términos acordados','style':'height:10em'}),required=True,
                help_text=(""))

    fecha_creacion = forms.DateField(label=("Fecha de creación"),
                widget=forms.DateInput(attrs={'class':class_attr_inputs,'readonly':True}),required=False)
    
    fecha_inicio = forms.DateField(label=("Fecha de inicio"),
                widget=forms.DateInput(attrs={'class':class_attr_inputs}),required=True)

    fecha_termino = forms.DateField(label=("Fecha de término"),
                widget=forms.DateInput(attrs={'class':class_attr_inputs}),required=True)

    precio_total = forms.IntegerField(label="Precio del Servicio (CLP)",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del pedido','readonly':True},),
                help_text=(""),required=False)

    class Meta:
        model = PedidoServicio
        fields = ['nombre','fecha_creacion','fecha_inicio','fecha_termino','precio_total','terminos_acordados','estado']