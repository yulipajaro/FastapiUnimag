from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

function_routes=APIRouter()

data=[
    {
    "id":1,
    "name":"Iphone 13",
    "quantity":12,
    "description":"Nuevo celular de Apple",
    "precio":4500000,
    "category":2
    },
    {
    "id":2,
    "name":"MSI GF13 thin",
    "quantity":10,
    "description":"Laptop para gamer",
    "precio":5000000,
    "category":1
    }
    ]


class Productos(BaseModel):
    id:int
    name:str
    quantity:int
    description:str
    precio:int
    category:int


@function_routes.get("/products")
def list_of_products():
    return JSONResponse(content={"message": "List of products","data":data},status_code=200) 

@function_routes.get('/products/{id}')
def serch_for_id(id):
    if len(data) == 0:
        return JSONResponse(content={"message": "No hay productos"},status_code=404)
    else:
        for product in data:
            if product["id"] == int(id):
                 return JSONResponse(content={"data":product},status_code=200)
        return JSONResponse(content={"message": "Product not found"},status_code=404)

@function_routes.get('/products/category/{category_id}')
def serch_for_category_id(category_id):
    
    if len(data) == 0:
        return JSONResponse(content={"message": "No hay productos"},status_code=404)
    else:
        contador_de_categorias=0
        product_for_categorias=[]
        for product in data:
            if product["category"] == int(category_id):
                product_for_categorias.append(product)
                contador_de_categorias=contador_de_categorias+1
        if contador_de_categorias==0:
            return JSONResponse(content={"message": "Categoria not found"},status_code=404)
        else:
            return JSONResponse(content={"data":product_for_categorias},status_code=200)
                 
        
        



@function_routes.post("/products")
def crear_productos(product:Productos):
    if product != None:
        data.append(product.dict())
        return JSONResponse(content={"message": "Product created","data":product.dict()},status_code=200)  
    else:
        return JSONResponse(content={"message": "Product not created"},status_code=404)  
        
    
