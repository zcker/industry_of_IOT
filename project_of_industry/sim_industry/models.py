from django.db import models


# Create your models here.
class DeviceInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    online = models.CharField(max_length=255)
    encrypt = models.CharField(max_length=255)
    onlinetime = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'device_info'


class Door(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'door'


class Fire(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fire'


class Gas(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'gas'


class Temperature(models.Model):
    value = models.CharField(max_length=255)
    time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temperature'


class Water(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'water'


class Weight(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'weight'
