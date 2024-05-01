from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Sum

from .filters import ProductFilter
from .models import Product, Review
from .serializers import ProductSerializer



# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('-id'))
    respage = 2
    paginator = PageNumberPagination()
    paginator.page_size = respage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response({"products": serializer.data})

@api_view(['GET'])
def get_by_id_products(request,pk):
    products = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(products, many=False)
    print(products)
    return Response({"products": serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data = data)

    if serializer.is_valid():
        product = Product.objects.create(**data,user=request.user)
        res = ProductSerializer(product, many=False)
        return Response({"products": res.data})
    else:
        return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request,pk):
    user = request.user
    product = get_object_or_404(Product,id=pk)
    data = request.data
    reviews = Product.reviews.filter(user=user)

    if data['rating']<= 0 or data['rating'] > 5:
        return Response({"error":'please select between 1 to 5 only'}
                        , status=status.HTTP_400_BAD_REQUEST)
    elif reviews.exists():
        new_review = {'rating': data['rating'],'comment':data['comment']}
        reviews.update(**new_review)

        rating = product.reviews.aggregate(Avg_ratings = Avg('rating'))
        product.ratings = rating['avg_ratings']
        product.save()

        return Response({'details':'Product raeview updated'})
    else:
        Review.objects.create(
            user=user,
            product=product,
            rating=data['rating'],
            comment=data['comment']
        )
        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
        product.ratings = rating['avg_ratings']
        product.save()
        return Response({'details':'Product review created'})