from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import *
from .serializers import *


class IndexView(APIView):

    def get(self, request):
        context = {'mensaje': 'servidor activo'}
        return Response(context)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserDetail(APIView):
    def get(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username)
        user.delete()
        return Response(status=204)


class UsuariosList(APIView):
    def get(self, request):
        dataUsuarios = Usuarios.objects.all()
        serUsuarios = UsuariosSerializer(dataUsuarios, many=True)
        return Response(serUsuarios.data)

    def post(self, request):
        serUsuarios = UsuariosSerializer(data=request.data)
        serUsuarios.is_valid(raise_exception=True)
        serUsuarios.save()
        return Response(UsuariosSerializer.data)


class UsuariosDetail(APIView):
    def get(self, request, id_usuarios):
        dataUsuarios = Usuarios.objects.get(pk=id_usuarios)
        serUsuarios = UsuariosSerializer(dataUsuarios)
        return Response(serUsuarios.data)

    def put(self, request, id_usuarios):
        dataUsuarios = Usuarios.objects.get(pk=id_usuarios)
        serUsuarios = UsuariosSerializer(dataUsuarios, data=request.data)
        serUsuarios.is_valid(raise_exception=True)
        serUsuarios.save()
        return Response(serUsuarios.data)

    def delete(self, request, id_usuarios):
        dataUsuarios = Usuarios.objects.get(pk=id_usuarios)
        serUsuarios = UsuariosSerializer(dataUsuarios)
        dataUsuarios.delete()
        return Response(serUsuarios.data)


class RolesList(APIView):
    def get(self, request):
        dataRoles = Roles.objects.all()
        serRoles = RolesSerializer(dataRoles, many=True)
        return Response(serRoles.data)

    def post(self, request):
        serRoles = RolesSerializer(data=request.data)
        serRoles.is_valid(raise_exception=True)
        serRoles.save()
        return Response(RolesSerializer.data)


class RolesDetail(APIView):
    def get(self, request, id_rol):
        dataRoles = Roles.objects.get(pk=id_rol)
        serRoles = RolesSerializer(dataRoles)
        return Response(serRoles.data)

    def put(self, request, id_rol):
        dataRoles = Roles.objects.get(pk=id_rol)
        serRoles = RolesSerializer(dataRoles, data=request.data)
        serRoles.is_valid(raise_exception=True)
        serRoles.save()
        return Response(serRoles.data)

    def delete(self, request, id_rol):
        dataRoles = Roles.objects.get(pk=id_rol)
        serRoles = RolesSerializer(dataRoles)
        dataRoles.delete()
        return Response(serRoles.data)


class ProductosList(APIView):
    def get(self, request):
        dataProductos = Productos.objects.all()
        serProductos = ProductosSerializer(dataProductos, many=True)
        return Response(serProductos.data)

    def post(self, request):
        serProductos = ProductosSerializer(data=request.data)
        serProductos.is_valid(raise_exception=True)
        serProductos.save()
        return Response(ProductosSerializer.data)


class ProductosDetail(APIView):
    def get(self, request, id_producto):
        dataProductos = Productos.objects.get(pk=id_producto)
        serProductos = ProductosSerializer(dataProductos)
        return Response(serProductos.data)

    def put(self, request, id_producto):
        dataProductos = Productos.objects.get(pk=id_producto)
        serProductos = ProductosSerializer(dataProductos, data=request.data)
        serProductos.is_valid(raise_exception=True)
        serProductos.save()
        return Response(serProductos.data)

    def delete(self, request, id_producto):
        dataProductos = Productos.objects.get(pk=id_producto)
        serProductos = ProductosSerializer(dataProductos)
        dataProductos.delete()
        return Response(serProductos.data)


class RegistroClienteTiendaList(APIView):
    def get(self, request):
        dataRegistro = RegistroClienteTienda.objects.all()
        serRegistro = RegistroClienteTiendaSerializer(dataRegistro, many=True)
        return Response(serRegistro.data)

    def post(self, request):
        serRegistro = RegistroClienteTiendaSerializer(data=request.data)
        serRegistro.is_valid(raise_exception=True)
        serRegistro.save()
        return Response(RegistroClienteTiendaSerializer.data)


class RegistroClienteTiendaDetail(APIView):
    def get(self, request, id_cli):
        dataRegistro = RegistroClienteTienda.objects.get(pk=id_cli)
        serRegistro = RegistroClienteTiendaSerializer(dataRegistro)
        return Response(serRegistro.data)

    def put(self, request, id_cli):
        dataRegistro = RegistroClienteTienda.objects.get(pk=id_cli)
        serRegistro = RegistroClienteTiendaSerializer(dataRegistro, data=request.data)
        serRegistro.is_valid(raise_exception=True)
        serRegistro.save()
        return Response(serRegistro.data)

    def delete(self, request, id_cli):
        dataRegistro = RegistroClienteTienda.objects.get(pk=id_cli)
        serRegistro = RegistroClienteTiendaSerializer(dataRegistro)
        dataRegistro.delete()
        return Response(serRegistro.data)


class TiendasList(APIView):
    def get(self, request):
        dataTiendas = Tiendas.objects.all()
        serTiendas = TiendasSerializer(dataTiendas, many=True)
        return Response(serTiendas.data)

    def post(self, request):
        serTiendas = TiendasSerializer(data=request.data)
        serTiendas.is_valid(raise_exception=True)
        serTiendas.save()
        return Response(TiendasSerializer.data)


class TiendasDetail(APIView):
    def get(self, request, id_tienda):
        dataTiendas = Tiendas.objects.get(pk=id_tienda)
        serTiendas = TiendasSerializer(dataTiendas)
        return Response(serTiendas.data)

    def put(self, request, id_tienda):
        dataTiendas = Tiendas.objects.get(pk=id_tienda)
        serTiendas = TiendasSerializer(dataTiendas, data=request.data)
        serTiendas.is_valid(raise_exception=True)
        serTiendas.save()
        return Response(serTiendas.data)

    def delete(self, request, id_tienda):
        dataTiendas = Tiendas.objects.get(pk=id_tienda)
        serTiendas = TiendasSerializer(dataTiendas)
        dataTiendas.delete()
        return Response(serTiendas.data)


class VentasList(APIView):
    def get(self, request):
        dataVentas = Ventas.objects.all()
        serVentas = VentasSerializer(dataVentas, many=True)
        return Response(serVentas.data)

    def post(self, request):
        serVentas = VentasSerializer(data=request.data)
        serVentas.is_valid(raise_exception=True)
        serVentas.save()
        return Response(VentasSerializer.data)


class VentasDetail(APIView):
    def get(self, request, id_ventas):
        dataVentas = Ventas.objects.get(pk=id_ventas)
        serVentas = VentasSerializer(dataVentas)
        return Response(serVentas.data)

    def put(self, request, id_ventas):
        dataVentas = Ventas.objects.get(pk=id_ventas)
        serVentas = VentasSerializer(dataVentas, data=request.data)
        serVentas.is_valid(raise_exception=True)
        serVentas.save()
        return Response(serVentas.data)

    def delete(self, request, id_ventas):
        dataVentas = Ventas.objects.get(pk=id_ventas)
        serVentas = VentasSerializer(dataVentas)
        dataVentas.delete()
        return Response(serVentas.data)




