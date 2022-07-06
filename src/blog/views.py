from rest_framework import viewsets
from .models import post
from .serializers import postSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer


def home(request):
    pass

def signup(request):
    pass

def signin(request):
    pass

def signout(request):
    pass