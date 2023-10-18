from rest_framework.serializers import *
from apps.post.models import *


#post
class PostSerializers(ModelSerializer):


    class Meta:
        model = ModelsPost
        fields = '__all__'

