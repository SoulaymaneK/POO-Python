import googlemaps 

class Gmap:
    def coordgps(adresse):
        gmaps = googlemaps.Client(key='AIzaSyBTeRxf61DWGHagCM2SOVupUhdo2POEkxE') 
        geocode_result = gmaps.geocode(adresse)
        try : 
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
        except IndexError: 
            raise IndexError("Cette adresse n'existe pas!")
        return lat,lng 

class Lieu :
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.__latitude,self.__longitude = Gmap.coordgps(self.adresse)

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,nom):
        if not isinstance(nom,str):
            raise TypeError ("L'adresse doit être de type str!")
        self.__nom = nom
    
    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self,adresse):
        
        if not isinstance(adresse,str):
            raise TypeError ("L'adresse doit être de type str!")
        self.__adresse = adresse

    def detail(self):
        print(f"Nom : {self.nom}\nAdresse : {self.adresse}\nLatitude et Longitude : ({self.__latitude}, {self.__longitude})")
    

l = Lieu("Domicile","75 rue Carnot, 60200 Compiègne, France" )
d = Lieu("BF", "Rue Roger Couttolenc, 60200 Compiègne, France")
utc = Lieu("PG","Rue du Docteur Schweitzer, 60203 Compiègne, France ")





l.nom = "Maison"
l.detail()
print("\n")
d.detail()
print("\n")
utc.detail()






