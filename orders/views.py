from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
import os

class ReactAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.BASE_DIR, 'orders/co-design/build', 'index.html')) as file:
                return HttpResponse(file.read())
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! ensure your React project has been built and index.html is available
                """,
                status=501,
            )
def index(request):
    return render(request, 'orders/co-design/build/index.html')

@api_view(['POST'])
def submit_order(request):
    phone_number = request.data.get('phoneNumber')
    menu = request.data.get('menu')
    total = request.data.get('total')

    # 데이터베이스에 저장하는 코드
    order = Order.objects.create(phone_number=phone_number, menu=menu, total=total)
    serializer = OrderSerializer(order)
    return Response(serializer.data)