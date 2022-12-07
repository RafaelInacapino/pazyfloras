from django.shortcuts import render, redirect
from tienda.models import Producto, Servicio, PedidoCarrito, PedidoServicio
from gestiontienda.forms import ProductoForm, ServicioForm, PedidoCarritoForm, PedidoServicioForm
from gestiontienda.decorators import superuser_required 



@superuser_required
def productos(request):

    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "productos"

    # page head
    context["title"]="Productos - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectionlistarproductos.html"

    # Script
    productos = Producto.objects.all()
    context["productos"] = productos
    for pro in context["productos"]:
        pro.precioSTR = "{:,}".format(pro.precio).replace(".","P").replace(",",".").replace("P",",")

    return render(request,'gestiontienda/1_listar_productos.html',context)

@superuser_required
def crearproducto(request):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "crearproducto"

    # page head
    context["title"]="Crear Producto - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioncrearproducto.html"

    # Script
    context["form"] = ProductoForm()
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            if not request.FILES:
                context["mensaje"] = 'La imagen es obligatoria.'
                context["clasesmensaje"] = 'alert alert-danger bg-gradient text-center'
                context['form'] = ProductoForm(data=request.POST,files=request.FILES)
                return render(request, 'gestiontienda/2_crear_productos.html', context)  
            try:
                formulario.save()
                request.session["mensaje"] = 'Producto creado con éxito'
                request.session["clasesmensaje"] = 'alert alert-success bg-gradient text-center'
                return redirect(to='/gestiontienda/productos') 
            except:
                context["mensaje"] = 'Datos incorrectos.'
                context["clasesmensaje"] = 'alert alert-danger bg-gradient text-center'
                context['form'] = ProductoForm(data=request.POST,files=request.FILES)
                return render(request, 'gestiontienda/2_crear_productos.html', context)  
        else:
            context["mensaje"] = 'Formulario inválido.'
            context["clasesmensaje"] = 'alert alert-danger bg-gradient text-center'
            context['form'] = ProductoForm(data=request.POST,files=request.FILES)
            return render(request, 'gestiontienda/2_crear_productos.html', context)  
    return render(request,'gestiontienda/2_crear_productos.html',context)

@superuser_required
def cambiarestadoproductos(request, id):
    # context dict
    context = {}
    producto = Producto.objects.get(id=id)
    print(producto)
    if producto.activo:
        producto.activo = False
        producto.save()
    else:
        producto.activo = True
        producto.save()
    return redirect("/gestiontienda/productos")

@superuser_required
def editarproducto(request, id):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "editarproducto"

    # page head
    context["title"]="Editar Producto - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioneditarproducto.html"
        
    # Script    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            pro = Producto.objects.get(id=id)
            pro.tipo = formulario.data["tipo"]
            pro.nombre = formulario.data["nombre"]
            # try:
            #     pro.precio = int(formulario.data["precio"])
            # except:
            #     context['form'] = ProductoForm(data=request.POST,files=request.FILES)
            #     context["mensaje"] = "Ingrese números enteros sin puntos."
            #     context["clasesmensaje"] = "alert alert-danger bg-gradient text-center"
            #     return render(request, 'gestiontienda/3_editar_productos.html', context) 
            pro.precio = formulario.data["precio"]
            pro.descripcion = formulario.data["descripcion"]
            try:
                if formulario.files["imagen"]:
                    pro.imagen = formulario.files["imagen"]
            except:
                pass
            try:
                if formulario.data["activo"]=='on':
                    pro.activo = True
            except:
                pro.activo = False
            request.session['mensaje'] = 'Producto actualizado con éxito.'
            request.session["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"
            pro.save()
            return redirect(to='/gestiontienda/productos') 
        else:
            print('Form is "NOT VALID"')
            context['form'] = ProductoForm(data=request.POST,files=request.FILES)
            context["mensaje"] = "Error al actualizar el producto."
            context["clasesmensaje"] = "alert alert-danger bg-light bg-gradient text-center"
            return render(request, 'gestiontienda/3_editar_productos.html', context)            
    else:
        context["id"] = id
        pro = Producto.objects.all().get(id=id)
        context["form"] = ProductoForm(instance=pro)
    return render(request,'gestiontienda/3_editar_productos.html',context)

@superuser_required
def servicios(request):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "servicios"

    # page head
    context["title"]="Servicios - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectionlistarservicios.html"
    
    servicios = Servicio.objects.all()
    context["servicios"] = servicios
    for ser in context["servicios"]:
        ser.precioSTR = "{:,}".format(ser.precio).replace(".","P").replace(",",".").replace("P",",")

    return render(request,'gestiontienda/4_listar_servicios.html',context)

@superuser_required
def crearservicio(request):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "crearservicio"

    # page head
    context["title"]="Crear Servicio - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioncrearservicio.html"

    # Script
    context["form"] = ServicioForm()
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            if not request.FILES:
                context["mensaje"] = 'La imagen es obligatoria.'
                context["clasesmensaje"] = 'alert alert-danger bg-gradient text-center'
                context['form'] = ServicioForm(data=request.POST,files=request.FILES)
                return render(request, 'gestiontienda/5_crear_servicios.html', context)  
            try:
                formulario.save()
                request.session["mensaje"] = 'Servicio creado con éxito'
                request.session["clasesmensaje"] = 'alert alert-success bg-gradient text-center'
                return redirect(to='/gestiontienda/servicios') 
            except:
                context["mensaje"] = 'Datos incorrectos.'
                context["clasesmensaje"] = 'alert alert-danger bg-gradient text-center'
                context['form'] = ServicioForm(data=request.POST,files=request.FILES)
                return render(request, 'gestiontienda/4_listar_servicios.html', context)  
        else:
            context["mensaje"] = 'Formulario inválido.'
            context["clasesmensaje"] = 'alert alert-danger bg-gradient text-center'
            context['form'] = ServicioForm(data=request.POST,files=request.FILES)
            return render(request, 'gestiontienda/5_crear_servicios.html', context)  
    return render(request,'gestiontienda/5_crear_servicios.html',context)

@superuser_required
def cambiarestadoservicios(request, id):
    # context dict
    context = {}
    servicio = Servicio.objects.get(id=id)
    print(servicio)
    if servicio.activo:
        servicio.activo = False
        servicio.save()
    else:
        servicio.activo = True
        servicio.save()
    return redirect("/gestiontienda/servicios")

@superuser_required
def editarservicio(request, id):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "editarservicio"

    # page head
    context["title"]="Editar Servicio - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioneditarservicio.html"
    
    # Script    
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            ser = Servicio.objects.get(id=id)
            ser.nombre = formulario.data["nombre"]
            try:
                ser.precio = int(formulario.data["precio"])
            except:
                context['form'] = ServicioForm(data=request.POST,files=request.FILES)
                context["mensaje"] = "Ingrese números enteros sin puntos."
                context["clasesmensaje"] = "alert alert-danger bg-gradient text-center"
                return render(request, 'gestiontienda/6_editar_servicios.html', context) 
            ser.precio = formulario.data["precio"]
            ser.descripcion = formulario.data["descripcion"]
            try:
                if formulario.files["imagen"]:
                    ser.imagen = formulario.files["imagen"]
            except:
                pass
            try:
                if formulario.data["activo"]=='on':
                    ser.activo = True
            except:
                ser.activo = False
            request.session['mensaje'] = 'Servicio actualizado con éxito.'
            request.session["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"
            ser.save()
            return redirect(to='/gestiontienda/servicios') 
        else:
            print('Form is "NOT VALID"')
            context['form'] = ServicioForm(data=request.POST,files=request.FILES)
            context["mensaje"] = "Error al actualizar el servicio."
            context["clasesmensaje"] = "alert alert-danger bg-light bg-gradient text-center"
            return render(request, 'gestiontienda/6_editar_servicios.html', context)            
    else:
        context["id"] = id
        ser = Servicio.objects.all().get(id=id)
        context["form"] = ServicioForm(instance=ser)
    return render(request,'gestiontienda/6_editar_servicios.html',context)

@superuser_required
def datostienda(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "datostienda"

    # page head
    context["title"]="Datos Tienda - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectiondatostienda.html"
    
    return render(request,'gestiontienda/7_listar_datostienda.html',context)

@superuser_required
def editardatostienda(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "editardatostienda"

    # page head
    context["title"]="Editar Datos Tienda - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioneditardatostienda.html"
    
    return render(request,'gestiontienda/8_editar_datostienda.html',context)



@superuser_required
def pedidoscarrito(request):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "pedidoscarrito"

    # page head
    context["title"]="Datos Tienda - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectionlistarpedidoscarrito.html"

    # script
    ped = PedidoCarrito.objects.all()
    context["pedidoscarritos"] = ped
    for pro in context["pedidoscarritos"]:
        pro.precio_total_STR = "{:,}".format(pro.precio_total).replace(".","P").replace(",",".").replace("P",",")
    
    return render(request,'gestiontienda/7_listar_pedidoscarrito.html',context)

@superuser_required
def editarpedidocarrito(request, id):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "editarpedidocarrito"

    # page head
    context["title"]="Datos Tienda - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioneditarpedidocarrito.html"
    
    # Script    
    if request.method == 'POST':
        formulario = PedidoCarritoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            ser = PedidoCarrito.objects.get(id=id)
            print(request.POST["estado"])
            ser.estado = request.POST["estado"]
            ser.save()
            request.session['mensaje'] = 'Pedido de Carrito actualizado con éxito.'
            request.session["clasesmensaje"] = "alert alert-success bg-light bg-gradient text-center"
            return redirect(to='/gestiontienda/pedidoscarrito') 
        else:
            context['form'] = PedidoCarritoForm(data=request.POST,files=request.FILES)
            context["mensaje"] = "Error al actualizar el pedido de carrito."
            context["clasesmensaje"] = "alert alert-danger bg-gradient text-center"
            return render(request, 'gestiontienda/8_editar_pedidocarrito.html', context)            
    else:
        context["id"] = id
        ped = PedidoCarrito.objects.all().get(id=id)
        context["form"] = PedidoCarritoForm(instance=ped)
    return render(request,'gestiontienda/8_editar_pedidocarrito.html',context)

@superuser_required
def pedidosservicio(request):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "pedidosservicio"

    # page head
    context["title"]="Datos Tienda - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectionlistarpedidosservicio.html"# script
    
    # script
    ped = PedidoServicio.objects.all()
    context["pedidosservicios"] = ped
    for pro in context["pedidosservicios"]:
        pro.precio_total_STR = "{:,}".format(pro.precio_total).replace(".","P").replace(",",".").replace("P",",")
    
    return render(request,'gestiontienda/9_listar_pedidosservicio.html',context)


@superuser_required
def editarpedidoservicio(request, id):
    # context dict
    context = {}

    #for redirects
    try:
        context["mensaje"] = request.session["mensaje"] 
        request.session["mensaje"] = ""       
        context["clasesmensaje"] = request.session["clasesmensaje"]
        request.session["clasesmensaje"] = ""
    except:
        pass

    # view url name
    context["view"] = "editarpedidoservicio"

    # page head
    context["title"]="Datos Tienda - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/content.html"
    context["sectionnav"]="gestiontienda/components/sectionnav.html"
    context["sectionview"]="gestiontienda/components/sectioneditarpedidoservicio.html"

    # Script    
    if request.method == 'POST':
        formulario = PedidoServicioForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            ser = PedidoServicio.objects.get(id=id)
            print(request.POST["estado"])
            ser.estado = request.POST["estado"]
            ser.save()
            request.session['mensaje'] = 'Pedido de Servicio actualizado con éxito.'
            request.session["clasesmensaje"] = "alert alert-success bg-gradient text-center"
            ser.save()
            return redirect(to='/gestiontienda/pedidosservicio') 
        else:
            context['form'] = PedidoServicioForm(data=request.POST,files=request.FILES)
            context["mensaje"] = "Error al actualizar el pedido de servicio."
            context["clasesmensaje"] = "alert alert-danger bg-gradient text-center"
            return render(request, 'gestiontienda/10_editarpedidoservicio.html', context)            
    else:
        context["id"] = id
        ser = PedidoServicio.objects.all().get(id=id)
        context["form"] = PedidoServicioForm(instance=ser)
    return render(request,'gestiontienda/10_editarpedidoservicio.html',context)



def accesodenegado(request):
    # context dict
    context = {}

    # view url name
    context["view"] = "accesodenegado"

    # page head
    context["title"]="Acceso Denegado - Paz y Floras"
    context["icon"]="tienda/images/imagen5.png"
    context["head"]="gestiontienda/components/head.html"

    # page general body info 
    context["header"]="gestiontienda/components/header.html"
    context["footer"]="gestiontienda/components/footer.html"

    # page body blocks
    context["content"]="gestiontienda/components/accesodenegado.html"
    return render(request, 'gestiontienda/20_accesodenegado.html', context)

