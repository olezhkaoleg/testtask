#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      olezhkaoleg
#
# Created:     16.03.2022
# Copyright:   (c) olezhkaoleg 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    field = serializers.Metaclass()
