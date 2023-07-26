from rest_framework import serializers


try:

    from apps.marcar_asistencia.models import Asistencia

except:
    pass 

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Asistencia
        except:
            pass    
        fields = '__all__'

