import json
import os
from django.conf import settings
from facility.models import School, SocialWork, YouthCareer, Daycare


def run():
    with open(os.path.join(settings.BASE_DIR, 'dataset/Schulen.geojson')) as f:
        data_list = json.load(f)

    category_name = data_list["name"]
    features = data_list["features"]
    School.objects.all().delete()
    for feature in features:
        geometry = feature["geometry"]["coordinates"]
        object_id = feature["properties"]["OBJECTID"]
        typ = feature["properties"]["TYP"]
        art = feature["properties"]["ART"]
        standorttyp = feature["properties"]["STANDORTTYP"]
        bezeichnung = feature["properties"]["BEZEICHNUNG"]
        bezeichnungzusatz = feature["properties"]["BEZEICHNUNGZUSATZ"]
        kurzbezeichnung = feature["properties"]["KURZBEZEICHNUNG"]
        strasse = feature["properties"]["STRASSE"]
        plz = feature["properties"]["PLZ"]
        ort = feature["properties"]["ORT"]
        telefon = feature["properties"]["TELEFON"]
        fax = feature["properties"]["FAX"]
        email = feature["properties"]["EMAIL"]
        profile = feature["properties"]["PROFILE"]
        sprachen = feature["properties"]["SPRACHEN"]
        www = feature["properties"]["WWW"]
        traeger = feature["properties"]["TRAEGER"]
        traegertyp = feature["properties"]["TRAEGERTYP"]
        bezugnr = feature["properties"]["BEZUGNR"]
        gebietsartnummer = feature["properties"]["GEBIETSARTNUMMER"]
        snummer = feature["properties"]["SNUMMER"]
        nummer = feature["properties"]["NUMMER"]
        global_id = feature["properties"]["GlobalID"]
        lat = geometry[1]
        long = geometry[0]
        school_obj = School(object_id=object_id, typ=typ, art=art, category=category_name, standorttyp=standorttyp,
                            bezeichnung=bezeichnung, bezeichnungzusatz=bezeichnungzusatz, kurzbezeichnung=kurzbezeichnung,
                            strasse=strasse, plz=plz, ort=ort, telefon=telefon, fax=fax, email=email, profile=profile,
                            sprachen=sprachen, www=www, traeger=traeger, traegertyp=traegertyp, bezugnr=bezugnr,
                            gebietsartnummer=gebietsartnummer, snummer=snummer, nummer=nummer, global_id=global_id,
                            lat=lat, long=long)
        school_obj.save()

    print("Schulen data successfully inserted")

    with open(os.path.join(settings.BASE_DIR, 'dataset/Schulsozialarbeit.geojson')) as f:
        data_list = json.load(f)

    category_name = data_list["name"]
    features = data_list["features"]
    SocialWork.objects.all().delete()
    for feature in features:
        geometry = feature["geometry"]["coordinates"]
        object_id = feature["properties"]["OBJECTID"]
        leistungen = feature["properties"]["LEISTUNGEN"]
        bezeichnung = feature["properties"]["BEZEICHNUNG"]
        kurzbezeichnung = feature["properties"]["KURZBEZEICHNUNG"]
        strasse = feature["properties"]["STRASSE"]
        plz = feature["properties"]["PLZ"]
        ort = feature["properties"]["ORT"]
        telefon = feature["properties"]["TELEFON"]
        fax = feature["properties"]["FAX"]
        email = feature["properties"]["EMAIL"]
        lat = geometry[1]
        long = geometry[0]
        social_work_obj = SocialWork(object_id=object_id, category=category_name, leistungen=leistungen, bezeichnung=bezeichnung,
                                     kurzbezeichnung=kurzbezeichnung, strasse=strasse, plz=plz, ort=ort,
                                     telefon=telefon, fax=fax, email=email, lat=lat, long=long)
        social_work_obj.save()

    print("Schulsozialarbeit data successfully inserted")


    with open(os.path.join(settings.BASE_DIR, 'dataset/Jugendberufshilfen.geojson')) as f:
        data_list = json.load(f)

    category_name = data_list["name"]
    features = data_list["features"]
    YouthCareer.objects.all().delete()
    for feature in features:
        geometry = feature["geometry"]["coordinates"]
        object_id = feature["properties"]["OBJECTID"]
        leistungen = feature["properties"]["LEISTUNGEN"]
        bezeichnung = feature["properties"]["BEZEICHNUNG"]
        kurzbezeichnung = feature["properties"]["KURZBEZEICHNUNG"]
        strasse = feature["properties"]["STRASSE"]
        plz = feature["properties"]["PLZ"]
        ort = feature["properties"]["ORT"]
        telefon = feature["properties"]["TELEFON"]
        fax = feature["properties"]["FAX"]
        email = feature["properties"]["EMAIL"]
        lat = geometry[1]
        long = geometry[0]
        youth_career_obj = YouthCareer(object_id=object_id, category=category_name, leistungen=leistungen, bezeichnung=bezeichnung,
                                     kurzbezeichnung=kurzbezeichnung, strasse=strasse, plz=plz, ort=ort,
                                     telefon=telefon, fax=fax, email=email, lat=lat, long=long)
        youth_career_obj.save()

    print("Jugendberufshilfen data successfully inserted")


    with open(os.path.join(settings.BASE_DIR, 'dataset/Kindertageseinrichtungen.geojson')) as f:
        data_list = json.load(f)

    category_name = data_list["name"]
    features = data_list["features"]
    Daycare.objects.all().delete()
    for feature in features:
        geometry = feature["geometry"]["coordinates"]
        object_id = feature["properties"]["OBJECTID"]
        bezeichnung = feature["properties"]["BEZEICHNUNG"]
        kurzbezeichnung = feature["properties"]["KURZBEZEICHNUNG"]
        strasse = feature["properties"]["STRASSE"]
        strschl = feature["properties"]["STRSCHL"]
        hausbez = feature["properties"]["HAUSBEZ"]
        plz = feature["properties"]["PLZ"]
        ort = feature["properties"]["ORT"]
        hort = feature["properties"]["HORT"]
        kita = feature["properties"]["KITA"]
        url = feature["properties"]["URL"]
        telefon = feature["properties"]["TELEFON"]
        fax = feature["properties"]["FAX"]
        email = feature["properties"]["EMAIL"]
        barrierefrei = feature["properties"]["BARRIEREFREI"]
        integrativ = feature["properties"]["INTEGRATIV"]
        lat = geometry[1]
        long = geometry[0]
        daycare_obj = Daycare(object_id=object_id, category=category_name, bezeichnung=bezeichnung,
                              kurzbezeichnung=kurzbezeichnung, strasse=strasse, strschl=strschl, hausbez=hausbez,
                              plz=plz, ort=ort, hort=hort, kita=kita, url=url, telefon=telefon, fax=fax, email=email,
                              barrierefrei=barrierefrei, integrativ=integrativ, lat=lat, long=long)
        daycare_obj.save()

    print("Kindertageseinrichtungen data successfully inserted")