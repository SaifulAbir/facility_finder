from django.db import models
from django.utils import timezone


class School(models.Model):
    object_id = models.IntegerField()
    typ = models.IntegerField(default=0)
    art = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    standorttyp = models.CharField(max_length=50, null=True, blank=True)
    bezeichnung = models.CharField(max_length=250, null=True, blank=True)
    bezeichnungzusatz = models.TextField(null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=200, null=True, blank=True)
    strasse = models.CharField(max_length=250, null=True, blank=True)
    plz = models.CharField(max_length=150, null=True, blank=True)
    ort = models.CharField(max_length=150, null=True, blank=True)
    telefon = models.CharField(max_length=150, null=True, blank=True)
    fax = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    profile = models.TextField(null=True, blank=True)
    sprachen = models.TextField(null=True, blank=True)
    www = models.URLField(max_length=250, null=True, blank=True)
    traeger = models.CharField(max_length=150, null=True, blank=True)
    traegertyp = models.IntegerField(default=0)
    bezugnr = models.CharField(max_length=150, null=True, blank=True)
    gebietsartnummer = models.IntegerField()
    snummer = models.IntegerField(default=0)
    nummer = models.IntegerField(default=0)
    global_id = models.CharField(max_length=150, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'schools'

    def __str__(self):
        return self.object_id


class SocialWork(models.Model):
    object_id = models.IntegerField()
    category = models.CharField(max_length=80)
    traeger = models.TextField(null=True, blank=True)
    leistungen = models.CharField(max_length=255, null=True, blank=True)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    strasse = models.CharField(max_length=250, null=True, blank=True)
    plz = models.CharField(max_length=150, null=True, blank=True)
    ort = models.CharField(max_length=150, null=True, blank=True)
    telefon = models.CharField(max_length=150, null=True, blank=True)
    fax = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'social_works'

    def __str__(self):
        return self.object_id


class YouthCareer(models.Model):
    object_id = models.IntegerField()
    category = models.CharField(max_length=80)
    traeger = models.TextField(null=True, blank=True)
    leistungen = models.CharField(max_length=255, null=True, blank=True)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    strasse = models.CharField(max_length=250, null=True, blank=True)
    plz = models.CharField(max_length=150, null=True, blank=True)
    ort = models.CharField(max_length=150, null=True, blank=True)
    telefon = models.CharField(max_length=150, null=True, blank=True)
    fax = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'youth_careers'

    def __str__(self):
        return self.object_id


class Daycare(models.Model):
    object_id = models.IntegerField()
    category = models.CharField(max_length=80)
    traeger = models.TextField(null=True, blank=True)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    strasse = models.CharField(max_length=250, null=True, blank=True)
    strschl = models.CharField(max_length=200, null=True, blank=True)
    hausbez = models.CharField(max_length=100, null=True, blank=True)
    plz = models.CharField(max_length=150, null=True, blank=True)
    ort = models.CharField(max_length=150, null=True, blank=True)
    hort = models.IntegerField(default=0)
    kita = models.IntegerField(default=0)
    url = models.URLField(max_length=255, null=True, blank=True)
    telefon = models.CharField(max_length=150, null=True, blank=True)
    fax = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    barrierefrei = models.IntegerField(default=0)
    integrativ = models.IntegerField(default=0)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'daycares'

    def __str__(self):
        return self.object_id