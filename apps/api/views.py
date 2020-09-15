from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.api.models import Game, Bid
from apps.api.serializers import GameSerializer, BidSerializer

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    # the user must be logged in to the system to create a category
    permission_classes = (IsAuthenticated,)
    # we can convert the data back and forth
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        print(request, '\n', args, '\n', kwargs)
        game = Game.objects.get(pk=self.kwargs["pk"])

        super().destroy(request, *args, **kwargs)
        return Response({
            "event": game,
            "status": status.HTTP_200_OK
        })


# class & method to get a single game by event_id, used to update scores when status of event is FINAL
class SingleGame(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GameSerializer

    def get_queryset(self):
        # localhost:8000/games/pk/
        if self.kwargs.get("pk"):
            game = Game.objects.get(pk=self.kwargs["pk"])
            return game


class BidViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BidSerializer

    def get_queryset(self):
        queryset = Bid.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can place a bid"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
