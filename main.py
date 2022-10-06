from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Msg(BaseModel):
    msg: str


menuitems = [ {
    "char_id": 1,
    "itemName": "Pork Belly Noodle Bowl",
    "price": "$24.00",
    "img": "https://media-cdn.tripadvisor.com/media/photo-m/1280/18/cd/03/93/pork-belly-noodle-bowl.jpg",
    "ingredients": "Noodles, Pork Belly, Broth",
    "allergens": "gluten, eggs, soy",
},
{
    "char_id": 2,
    "itemName": "Asian-marinated Airline Chicken",
    "price": "$24.00",
    "img": "https://media.wdwnt.com/2019/10/new-kona-cafe-menu-sticky-wings-airplane-chicken-polynesian-resort_17-1200x675.jpg",
    "ingredients": "Sticky Rice, Bok Choy, Asian Glaze",
    "allergens": "dairy, soy",
},
{
    "char_id": 3,
    "itemName": "Turkey Banh Mi",
    "price": "$18.00",
    "img": "https://i1.wp.com/www.wdwopinion.com/wp-content/uploads/2020/01/IMG_8386-scaled.jpg?fit=1024%2C768&ssl=1",
    "ingredients": "Slow-roasted Turkey Breast, Black Pepper Bacon, Pork Pâte, Cilantro, Jalapeño, Onions, and Grilled Poblano Mayonnaise served with French Fries",
    "allergens": "gluten, dairy",
},
]

@app.get('/')

async def read_root():
    return menuitems