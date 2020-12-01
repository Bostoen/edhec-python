# GEOPLC
Détection QPV

La réponse se présentera sous la forme suivante 

```json
{
  "Token": "Token",
  "message":"Description de l'action",
  "data":"Données de la réponse"
}
```

Le token d'identification se trouve dans le fichier `.env` sous `API_TOKEN`

**Faire un test**

`POST /check`

**Arguments**

L'objet est de type résidentiel collectif.

- `"Street":string` Adresse du site
- `"CP":string` Code postal du site
- `"Town":string` Ville du site

**Réponse**

- `200` si la requête abouti.

```json
{
  "Status":"Success",
  "Status_id":"200",
  "Address":"l'adresse de l'objet à tester",
  "Lat":"Latitude de l'adresse",
  "Long":"Longitude de l'adresse",
  "Is_QPV":"Résultat du test",
  "Id_QPV":"ID du QPV",
  "Name_QPV":"Nom du QPV"
}
```

**Erreurs**

Le type d'erreur est transmis dans le champ `Name_QPV`

- `400-1` si une erreur est présente dans l'adresse de type syntaxe d'adresse. 

```json
{
  "Status":"Error",
  "Status_id":"400-1",
  "Address":"l'adresse de l'objet à tester",
  "Lat":null,
  "Long":null,
  "Is_QPV":false,
  "Id_QPV":null,
  "Name_QPV":null
}
```

- `400-2` si une erreur est présente dans l'adresse de type syntaxe métadonnée. 

```json
{
  "Status":"Error",
  "Status_id":"400-2",
  "Address":null,
  "Lat":null,
  "Long":null,
  "Is_QPV":false,
  "Id_QPV":null,
  "Name_QPV":null
}
```

Cas assez rare parce que le Geocoder trouve des solutions même pour des données erronées.

- `404` si le Geocoder injoignable. 

```json
{
  "Status":"Error",
  "Status_id":"404",
  "Address":"l'adresse de l'objet à tester",
  "Lat":null,
  "Long":null,
  "Is_QPV":false,
  "Id_QPV":null,
  "Name_QPV":null
}
```

**Exemple**

```json
{
  "Street": "32 rue jean jacques rousseau",
  "CP": "94200",
  "Town": "Ivry sur seine"
}
```
Envoyé à http://localhost:5000/check retourne

```json
{
    "Token": "JAMBON",
	"message": "Success",
	"data": {
		"Status":"Success",
		"Status_id":"200",
        "Address": "32 rue jean jacques rousseau 94200 Ivry sur seine France",
        "Lat": 48.81688700779752,
        "Long": 2.3950689518971724,
        "Is_QPV": true,
        "Id_QPV": "QP094009",
        "Name_QPV": "Ivry Port"
    }
}
```
