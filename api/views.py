from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.filter import ConsumerFilter
from api.page import ApiPageNumberPagination
from api.models import Consumer
from api.serializers import ConsumerSerializer


class ConsumerView(GenericViewSet, ListModelMixin):
    throttle_scope = 'consumer_listing'
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    pagination_class = ApiPageNumberPagination
    filter_backends = [ConsumerFilter, OrderingFilter]
    ordering_filters = ['consumer_id']
