from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.models import Consumer


class ConsumerSerializer(GeoFeatureModelSerializer):
    id = serializers.CharField(source="consumer_id")
    
    class Meta:
        model = Consumer
        geo_field = "geometry"
        id_field = False
        fields = ("id","amount_due", "previous_jobs_count", "status", "street")
