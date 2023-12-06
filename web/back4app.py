import requests

# Definir las credenciales de la API
headers = {
    "X-Parse-Application-Id": "Oa2WHGwGmV6FNYvw3ynCp9uvLMte7g8EZo1bxkSM",
    "X-Parse-REST-API-Key": "MsKJi967w8B5NqekwYefa1TFvdRwDZ5LlHAupy9Y",
    "accept": "application/json"
}


# Función para login por la API
def login_api(usuario: str, codigo: str):
    # Definir URL de la API donde se enviarán los datos
    URL: str = "https://parseapi.back4app.com/login?username={}&password={}".format(usuario, codigo)
    # Enviar los datos a la API
    response = requests.get(URL, headers=headers)
    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        print(response.json().get("sessionToken"))
        print("Datos enviados correctamente:")
        print("-------------------------------------")
        user: str = response.json().get("username")
        print("Usuario: ", user)
        print("-------------------------------------")
        return user

    else:
        print("Error al enviar los datos:", response.status_code)
        print("-------------------------------------")
        user: str = response.status_code
        return user


def obtener_datos_api(user: str):
    # URL: str = "https://parseapi.back4app.com/classes/parametros?where=usuario=='{}'".format(user)
    URL1: str = "https://parseapi.back4app.com/classes/almacen?where=%7B%22usuario%22%3A%20%22{}%22%7D".format(user)
    # Enviar los datos a la API
    response = requests.get(URL1, headers=headers)
    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        print("Datos obtenidos correctamente:")
        print("-------------------------------------")
        dato: str = response.json()["results"][0].get("nombre")
        datos = response.json()
        print("enviado: ", URL1)
        print("Dato: ", datos)
        print("-------------------------------------")
        return datos

    else:
        print("Error al enviar los datos:", response.status_code)
        print("-------------------------------------")
        dato: str = response.status_code
        return dato
