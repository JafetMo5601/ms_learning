from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer, UserSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response('Data provided invalid.', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Product.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response('Data provided invalid.', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = ProductSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(instance=user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
