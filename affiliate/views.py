import http
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import statistics
from affiliate.models import Product


# Handle Products
def createproduct(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        affiliate_promo = request.POST['affiliate_promo']
        product = Product(name=name, description=description, image=image, price=price, affiliate_promo=affiliate_promo)
        product.save()

        return Response({'message': 'Product created'}, status=statistics.HTTP_201_CREATED)
    else:
        return Response({'message': 'Invalid request'}, status=statistics.HTTP_400_BAD_REQUEST)

def getproduct(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        return Response({'message': 'Product fetched', 'product': product}, status=statistics.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid request'}, status=statistics.HTTP_400_BAD_REQUEST)

def updateproduct(request, pk):
    if request.method == 'PUT':
        product = Product.objects.get(pk=pk)
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.image = request.FILES['image']
        product.price = request.POST['price']
        product.affiliate_promo = request.POST['affiliate_promo']
        product.save()

        return Response({'message': 'Product updated'}, status=statistics.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid request'}, status=statistics.HTTP_400_BAD_REQUEST)

def deleteproduct(request, pk):
    if request.method == 'DELETE':
        product = Product.objects.get(pk=pk)
        product.delete()

        return Response({'message': 'Product deleted'}, status=statistics.HTTP_204_NO_CONTENT)
    else:
        return Response({'message': 'Invalid request'}, status=statistics.HTTP_400_BAD_REQUEST)