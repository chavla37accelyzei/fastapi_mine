from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()
class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class person(BaseModel):
    name:str
    age:int
    address:Address

#we define address ,person models 
#where person includes an Address object on its attribute

#send request
data = {
    'name' :'John',
    'age':30,
    'address':{
        'street' : 'main street',
         'city'  : 'Rajam',
         'zip_code':532127

    }

}

response = requests.post("http://localhost:120.0.0.800/process/",json=data)
print(response.save)


#Declare with an example
class Item(BaseModel):
    name = str = Field(example = ['100'])
    describe:str=Field(default = None,examples = ['a very nice item'])
