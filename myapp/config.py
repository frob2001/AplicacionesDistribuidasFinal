import pyrebase

config = {
    "apiKey": "AIzaSyDdIFoXFd0tE14hDK-GmYmV8zrzIchbg6o",
    "authDomain": "apsdistribuidas.firebaseapp.com",
    "databaseURL": "https://apsdistribuidas-default-rtdb.firebaseio.com",
    "projectId": "apsdistribuidas",
    "storageBucket": "apsdistribuidas.appspot.com",
    "messagingSenderId": "680887228389",
    "appId": "1:680887228389:web:541206942cab120e23c10c",
    "measurementId": "G-FW8YR4FD3T"
}

firebase = pyrebase.initialize_app(config)
fdb = firebase.database()

#fdb.child("Productos").push("Marshmellows")

# productos = [
#     {
#         "nombre": "Gomitas",
#         "descripcion": "Gomitas sabores frutales",
#         "precio": 1.99,
#         "imagen": "https://firebasestorage.googleapis.com/v0/b/apsdistribuidas.appspot.com/o/gomitas.jpeg?alt=media&token=2a55bcd7-d3d6-4c08-8b0e-f76fa48dfe1b"
#     },
#     {
#         "nombre": "Marshmallows",
#         "descripcion": "Marshmallows suaves y esponjosos",
#         "precio": 3.49,
#         "imagen": "https://firebasestorage.googleapis.com/v0/b/apsdistribuidas.appspot.com/o/massmellows.jpg?alt=media&token=38ac0660-ce99-4d05-83d6-ffc8c93c1771"
#     },
#     {
#         "nombre": "Chocolate",
#         "descripcion": "Chocolate negro de alta calidad",
#         "precio": 4.99,
#         "imagen": "https://firebasestorage.googleapis.com/v0/b/apsdistribuidas.appspot.com/o/chocolate.jpg?alt=media&token=dba14543-b778-4f55-aa94-f70345fcd3e7"
#     },
#     {
#         "nombre": "Caramelos",
#         "descripcion": "Caramelos variados",
#         "precio": 0.99,
#         "imagen": "https://firebasestorage.googleapis.com/v0/b/apsdistribuidas.appspot.com/o/caramelos.jpg?alt=media&token=e1915da3-eb44-4e56-bc1f-4253800a11a3"
#     },
#     {
#         "nombre": "Chicles",
#         "descripcion": "Chicles de sabores surtidos",
#         "precio": 0.79,
#         "imagen": "https://firebasestorage.googleapis.com/v0/b/apsdistribuidas.appspot.com/o/trident.jpg?alt=media&token=1582d0f4-5469-4ebf-9fbf-468d64b3a759"
#     },
#     # Agrega aquí más ejemplos de dulces según sea necesario
# ]

# # Subir los productos a Firebase
# for producto in productos:
#     fdb.child("productos").push(producto)