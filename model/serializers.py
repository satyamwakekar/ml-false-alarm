from rest_framework import serializers


class saveohlcserializer(serializers.Serializer):
    """ Serializer serializes a name field for testing api view  """
    instrument_id = serializers.FloatField()
    trade_time_in_min = serializers.DateTimeField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    indicator = serializers.CharField()
    sample_rate = serializers.IntegerField()


