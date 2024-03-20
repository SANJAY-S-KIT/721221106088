from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User,Product
from .serializers import UserSerializer,ProductSerializer

# Create your views here.
@api_view(["GET"])
def getData(request):
    items = User.objects.all()
    serializer = UserSerializer(items,many=True)
    return Response(serializer.data)
def getDataProduct(request):
    items = Product.objects.all()
    serializer = ProductSerializer(items,many=True)
    return Response(serializer.data)

@api_view([ "POST" ])
def saveData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def saveDataProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    
    
        
