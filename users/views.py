from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserModel
from .serializers import UserSerializer


#
class ListCreateView(APIView):
    def get(self, *args, **kwargs):
        db_users = UserModel.objects.all()
        users = UserSerializer(db_users, many=True).data
        return Response(users, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # user = UserModel.objects.get(pk=pk)
        user = get_object_or_404(UserModel.objects.all(), pk=pk)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(user, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#     def get(self, *args, **kwargs):
#         return Response('hello get')
#
#     def post(self, *args, **kwargs):
#         return Response('hello post')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello patch')
#
#     def put(self, *args, **kwargs):
#         return Response('hello put')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello delete')
