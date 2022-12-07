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

    precio_total = forms.IntegerField(label="Precio del Servicio (CLP) *",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del pedido'}),
                help_text=(""))

    class Meta:
        model = PedidoCarrito
        fields = '__all__'


class PedidoServicioForm(ModelForm):

    class_attr_inputs = 'form-control input_for_form mt-2'

    precio_total = forms.IntegerField(label="Precio del Servicio (CLP) *",
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresar valor del pedido'}),
                help_text=(""))

    class Meta:
        model = PedidoServicio
        fields = '__all__'
