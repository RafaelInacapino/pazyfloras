from django.shortcuts import render, redirect
from tienda.models import Producto, Servicio, PedidoCarrito, PedidoServicio
from django.contrib.auth.models import User
from tienda.decorators import login_required
import datetime

def index(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "index"

    # page head
    context["title"]="Paz y Floras"
    context["icon"]="tienda/images/icono_pazyfloras.png"
    context["head"]="tienda/components/head.html"
    
    # page general body info
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["carousel"]="tienda/components/carousel.html"
    context["testimonials"]="tienda/components/testimonials.html"

    return render(request, 'tienda/1_index.html', context)

def productos(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "productos"

    # page head
    context["title"]="Productos - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectionproductos"]="tienda/components/sectionproductos.html"

    # page data instructions
    context["productos"]= Producto.objects.all().filter(activo=True)
    for pro in context["productos"]:
        pro.precioSTR = "{:,}".format(pro.precio).replace(".","P").replace(",",".").replace("P",",")
        pro.idmodal = pro.nombre.replace(" ","")+str(pro.id)
        pro.nombremodal = "#"+pro.idmodal 
    return render(request, 'tienda/2_productos.html', context)

def maceteros(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "maceteros"

    # page head
    context["title"]="Maceteros - Paz y Floras"
    context["icon"]="tienda/images/imagen3.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectionproductos"]="tienda/components/sectionproductos.html"

    # page data instructions
    context["tipo"] = "macetero"
    context["productos"]= Producto.objects.all().filter(activo=True)
    for ser in context["productos"]:
        ser.precioSTR = "{:,}".format(ser.precio).replace(".","P").replace(",",".").replace("P",",")
        ser.idmodal = ser.nombre.replace(" ","")+str(ser.id)
        ser.nombremodal = "#"+ser.idmodal 
    return render(request, 'tienda/3_maceteros.html', context)

def vasijas(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "vasijas"

    # page head
    context["title"]="Vasijas - Paz y Floras"
    context["icon"]="tienda/images/imagen4.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectionproductos"]="tienda/components/sectionproductos.html"

    # page data instructions
    context["tipo"] = "vasija"
    context["productos"]= Producto.objects.all().filter(activo=True)
    for ser in context["productos"]:
        ser.precioSTR = "{:,}".format(ser.precio).replace(".","P").replace(",",".").replace("P",",")
        ser.idmodal = ser.nombre.replace(" ","")+str(ser.id)
        ser.nombremodal = "#"+ser.idmodal 
    return render(request, 'tienda/4_vasijas.html', context)

def plantas(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "plantas"

    # page head
    context["title"]="Plantas - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectionproductos"]="tienda/components/sectionproductos.html"

    # page data instructions
    context["tipo"] = "planta"
    context["productos"]= Producto.objects.all().filter(activo=True)
    for ser in context["productos"]:
        ser.precioSTR = "{:,}".format(ser.precio).replace(".","P").replace(",",".").replace("P",",")
        ser.idmodal = ser.nombre.replace(" ","")+str(ser.id)
        ser.nombremodal = "#"+ser.idmodal 
    return render(request, 'tienda/5_plantas.html', context)
    
def servicios(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "servicios"

    # page head
    context["title"]="Servicios - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectionservicios"]="tienda/components/sectionservicios.html"

    # page data instructions
    context["tipo"] = "servicio"
    context["servicios"]= Servicio.objects.all().filter(activo=True)

    for ser in context["servicios"]:
        ser.precioSTR = "{:,}".format(ser.precio).replace(".","P").replace(",",".").replace("P",",")
        ser.idmodal = ser.nombre.replace(" ","")+str(ser.id)
        ser.nombremodal = "#"+ser.idmodal 
    return render(request, 'tienda/6_servicios.html', context)

@login_required
def carrito(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "carrito"

    # page head
    context["title"]="Carrito - Paz y Floras"
    context["icon"]="tienda/images/imagen4.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["carrito"]="tienda/components/sectionservicios.html"

    # page data instructions
    context["tipo"] = "carrito"
    
    #reset carrito
    # request.session["carrito"] = []
    

    try:
        if len(request.session["carrito"])==0:
            print("Carrito existe, pero está vacío.")
        else:
            print("Carrito tiene productos: "+str(request.session["carrito"]))
    except:
        print("Error!")
        request.session["carrito"] = []
        print("Carrito creado!")
    productos = []
    context["carritopreciototal"] = 0
    for pro in request.session["carrito"]:
        producto = Producto.objects.get(id=pro[0])
        producto.cantidad = pro[1]
        context["carritopreciototal"] += int(producto.cantidad) * int(producto.precio)
        producto.precioSTR = "{:,}".format(producto.precio).replace(".","P").replace(",",".").replace("P",",")
        
        productos.append(producto)
    context["carritopreciototalSTR"] = "{:,}".format(context["carritopreciototal"]).replace(".","P").replace(",",".").replace("P",",")
    request.session["carritopreciototal"] = context["carritopreciototal"]
    request.session["carritopreciototalSTR"] = context["carritopreciototalSTR"]
    context["productos"] = productos
    return render(request, 'tienda/7_carrito.html', context)

def pedirCarrito(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "carrito"

    # page head
    context["title"]="Carrito - Paz y Floras"
    context["icon"]="tienda/images/imagen4.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["carrito"]="tienda/components/sectionservicios.html"

    # page data instructions
    context["tipo"] = "carrito"
    
    #reset carrito
    # request.session["carrito"] = []
    
    if request.method == "POST":
        pedidoCarrito = PedidoCarrito(user=User.objects.get(id=request.user.id),fecha_creacion=datetime.date.today(),precio_total=request.session["carritopreciototal"], json="")
        pedidoCarrito.save()
        request.session["mensaje"] = "Pedido solicitado"
        request.session["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"
        request.session["carrito"] = []
        return redirect("/tienda/cuenta/mispedidos")

@login_required
def agregarProducto(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "carrito"

    # page head
    context["title"]="Carrito - Paz y Floras"
    context["icon"]="tienda/images/imagen4.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["carrito"]="tienda/components/sectionservicios.html"

    # page data instructions
    context["tipo"] = "carrito"


    #script
    try:
        if len(request.session["carrito"])==0:
            print("Carrito existe!")
        else:
            print("Carrito tiene productos: "+ str(request.session["carrito"]))
        
    except:
        request.session["carrito"] = []
        print("Carrito creado!")
        
    if request.method == "POST":
        pro = Producto.objects.get(id=id)
        cantidad = request.POST["cantidad"]
        pro_existe = False
        for procar in request.session["carrito"]:
            if int(procar[0]) == int(pro.id):
                request.session["carrito"].remove([procar[0],procar[1]])
                request.session["carrito"].append([pro.id,cantidad])
                request.session["carrito"] = request.session["carrito"]
                print("Igualdad")
                pro_existe = True
                break 
        if not pro_existe:
            request.session["carrito"].append([pro.id,cantidad])
            request.session["mensaje"] = "Producto Agregado al Carrito."
            return redirect('/tienda/cuenta/carrito')
        else:
            return redirect('/tienda/cuenta/carrito')
    
    return  redirect('/tienda/cuenta/carrito')

@login_required
def eliminarProducto(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "carrito"

    # page head
    context["title"]="Carrito - Paz y Floras"
    context["icon"]="tienda/images/imagen4.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["carrito"]="tienda/components/sectionservicios.html"

    # page data instructions
    context["tipo"] = "carrito"

    #script
    for procar in request.session["carrito"]:
        if int(procar[0]) == int(id):
            request.session["carrito"].remove([procar[0],procar[1]])
            request.session["carrito"] = request.session["carrito"]
            print("Igualdad")
            pro_existe = True
            break
    return redirect('/tienda/cuenta/carrito')    

def pedirServicio(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "carrito"

    # page head
    context["title"]="Carrito - Paz y Floras"
    context["icon"]="tienda/images/imagen4.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["carrito"]="tienda/components/sectionservicios.html"

    # page data instructions
    context["tipo"] = "carrito"
    
    #reset carrito
    # request.session["carrito"] = []
    

    if request.method == "POST":
        servicio = Servicio.objects.get(id=id)
        pedidoServicio = PedidoServicio(user=User.objects.get(id=request.user.id),fecha_inicio=datetime.date.today(),precio_total=servicio.precio)
        pedidoServicio.save()
        request.session["mensaje"] = "Pedido de Servicio solicitado"
        request.session["clasesmensaje"] = "alert alert-success bg-gradient text-center"
        return redirect("/tienda/cuenta/misservicios")


def quienessomos(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "quienessomos"

    # page head
    context["title"]="Quienes Somos - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectionquienessomos"]="tienda/components/sectionquienessomos.html"

    # page data instructions
    context["tipo"] = "quienessomos"
    return render(request, 'tienda/8_quienessomos.html', context)

def contacto(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "contacto"

    # page head
    context["title"]="Contacto - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectioncontacto"]="tienda/components/sectioncontacto.html"

    # page data instructions
    context["tipo"] = "contacto"
    return render(request, 'tienda/9_contacto.html', context)

from .forms import RegisterUserForm

def registro(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "registro"

    # page head
    context["title"]="Registro - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["sectioncontacto"]="tienda/components/sectioncontacto.html"

    # page data instructions
    context["tipo"] = "contacto"

    #Script
    if request.method == 'POST':
        print('Method is "POST"')
        form = RegisterUserForm(request.POST)
        # RegisterUserForm is created from User model, all model field restrictions are checked to considerate it a valid form
        if form.is_valid():
            print('Form is "VALID"')
            # Save user to database but with is_active = False
            user = form.save(commit=False)
            user.is_active = True
            user.is_superuser = False
            user.is_staff = False
            user.save()
            context["mensaje"] = "Registrado con Éxito."
            return redirect('/tienda/cuenta/login')
        else:
            print('Form is "NOT VALID"')
            context['form'] = RegisterUserForm(request.POST)
            context["mensaje"] = "Error al Registrar."
            return render(request, 'registration/register.html', context)
    else:
        print('Method is "NOT POST"')
        form = RegisterUserForm()
        context['form'] = form
        return render(request, 'registration/register.html', context)



@login_required
def perfil(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfil"

    # page head
    context["title"]="Perfil - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentaperfil.html"

    # page data instructions
    context["tipo"] = "perfil"


    return render(request, 'tienda/10_perfilcuenta.html', context)


@login_required
def perfilpedidos(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfilpedidos"

    # page head
    context["title"]="Pedidos - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentapedidos.html"

    # page data instructions
    context["tipo"] = "perfil"

    #Scripts
    listadoPedidos = PedidoCarrito.objects.all().filter(user=User.objects.get(id=request.user.id))
    context["listadoPedidos"]=listadoPedidos

    return render(request, 'tienda/11_perfilpedidos.html', context)


@login_required
def perfilservicios(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfilservicios"

    # page head
    context["title"]="Servicios - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentaservicios.html"

    # page data instructions
    context["tipo"] = "perfil"

    #scripts
    listadoServicio = PedidoServicio.objects.all().filter(user=User.objects.get(id=request.user.id))
    context["listadoServicio"]=listadoServicio

    return render(request, 'tienda/12_perfilservicios.html', context)
   
@login_required
def perfilpagarcarritopagar(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfilpagar"

    # page head
    context["title"]="Pagar - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentapagar.html"

    # page data instructions
    context["tipo"] = "perfil"

    #scripts
    context["mensaje"] = "Enviando a Webpay ..."
    context["id"] = id
    context["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"

    return render(request, 'tienda/20_perfilpagarpedidoproductos.html', context)

@login_required
def perfilpagarcarritowebpay(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfilpedidopagado"

    # page head
    context["title"]="Pedidos - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentapagar.html"

    # page data instructions
    context["tipo"] = "perfil"
    context["id"] = id
    #scripts
    return render(request,"tienda/21_testingpagarpedidoproductos.html", context)

@login_required
def perfilpagarcarritopagado(request, id):

    # context dict
    context = {}
    pedido = PedidoCarrito.objects.get(id=id)
    pedido.estado = "Pagado"
    pedido.save()
    request.session["mensaje"] = "Pedido Pagado"
    request.session["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"
    return redirect("/tienda/cuenta/mispedidos")

@login_required
def perfilpagarserviciopagar(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfilpagar"

    # page head
    context["title"]="Pagar - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentapagar.html"

    # page data instructions
    context["tipo"] = "perfil"

    #scripts
    context["mensaje"] = "Enviando a Webpay ..."
    context["id"] = id
    context["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"

    return render(request, 'tienda/20_perfilpagarpedidoservicio.html', context)

@login_required
def perfilpagarserviciowebpay(request, id):
    # context dict
    context = {}

    # view url name
    context["view"] = "perfilpedidopagado"

    # page head
    context["title"]="Pedidos - Paz y Floras"
    context["icon"]="tienda/images/imagen2.png"
    context["head"]="tienda/components/head.html"

    # page general body info 
    context["header"]="tienda/components/header.html"
    context["footer"]="tienda/components/footer.html"

    # page body blocks
    context["contentperfil"] = "tienda/components/contentperfil.html"
    context["sectioncuentanav"]="tienda/components/sectioncuentanav.html"
    context["sectioncuentaview"]="tienda/components/sectioncuentapagar.html"

    # page data instructions
    context["tipo"] = "perfil"
    context["id"] = id
    #scripts
    return render(request,"tienda/21_testingpagarpedidoservicio.html", context)

@login_required
def perfilpagarserviciopagado(request, id):

    # context dict
    context = {}
    pedido = PedidoServicio.objects.get(id=id)
    pedido.estado = "Pagado"
    pedido.save()
    request.session["mensaje"] = "Pedido Pagado"
    request.session["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"
    return redirect("/tienda/cuenta/misservicios")