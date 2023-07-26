from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

def index(request):
    return render(request, 'co-design1/index.html')

@api_view(['POST'])
def submit_order(request):
    phone_number = request.data.get('phoneNumber')
    menu = request.data.get('menu')
    total = request.data.get('total')

    # 데이터베이스에 저장하는 코드
    order = Order.objects.create(phone_number=phone_number, menu=menu, total=total)
    serializer = OrderSerializer(order)
    return Response(serializer.data)