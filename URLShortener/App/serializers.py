from rest_framework.serializers import ModelSerializer
from .models import Link

# To serialize the view  of APIs into datatypes
class LinkSerializer(ModelSerializer):
    class Meta:
        model=Link
        fields='__all__'