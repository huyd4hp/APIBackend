from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .permissions import IsOwnerOrAdminUser
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def get_permissions(self):
        # Chỉ được xem nếu được xác thực
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        # Cho phép bất kỳ ai tạo
        elif self.action == 'create':
            permission_classes = [AllowAny]
        # Chỉ Admin có quyền sửa hoặc User đó tự sửa thông tin bản thân
        else:
            permission_classes = [IsOwnerOrAdminUser]
        return [permission() for permission in permission_classes]

    
class UserProfileViewSet(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
        
