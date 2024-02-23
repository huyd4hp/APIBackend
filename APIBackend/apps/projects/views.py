from rest_framework import viewsets
from .models import Project,Task
from .serializers import ProjectSerializer,TaskSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import IsManagerOrAdminUser
# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'created':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsManagerOrAdminUser]
        return [permission() for permission in permission_classes]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]