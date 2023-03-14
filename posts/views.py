from rest_framework.decorators import action
from .models import Post, Like
from rest_framework import viewsets, mixins, permissions, status
from .serializers import PostSerializer, LikeSerializer, LikeByDaySerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .filters import LikeFilter
from django.db.models import Count, Sum


class PostViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeFilter
    lookup_field = 'post_id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user_id == request.user:
            self.perform_destroy(instance)
        else:
            return Response({"message": "You did not like this post yet"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], url_path='analytics', detail=False)
    def analytics(self, request):
        qs = Like.objects.extra(select={'day': "date(created_at)"}).values('day').annotate(likes=Count('pk'))
        qs = self.filter_queryset(qs)
        serializer_data = LikeByDaySerializer(qs, many=True).data
        return Response(serializer_data)

