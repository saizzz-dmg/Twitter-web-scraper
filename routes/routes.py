from fastapi import APIRouter,Request 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.models import trending_list_in  , Trending_list
from config.database import collection_name
from schemas import individual_serial
from bson import ObjectId
from scrapers.scraper import scraper_func , refresh_scraper_func
import httpx

router = APIRouter()
templates = Jinja2Templates(directory="templates")

latest_id = 0

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "My Dynamic Title"})

@router.get('/finalendpoint')
async def get_trendings():
    trendings = individual_serial(collection_name.find_one({"_id" : ObjectId(str(latest_id))}))
    tredning1 = collection_name.find_one({"_id" : ObjectId(str(latest_id))})
    # print(type(tredning1))
    # print(trendings)
    return trendings

@router.get('/getTrendings')
async def put_trendings(request : Request):
    global latest_id
    inputvalues = scraper_func()
    print(inputvalues , 'from method')
    result = collection_name.insert_one(dict(inputvalues))
    latest_id =  result.inserted_id
    print(latest_id)
    async with httpx.AsyncClient() as client:
        try :
            response2 = await client.get("http://127.0.0.1:8000/finalendpoint")
            response = response2.json()
            # response = Trending_list(**response1)
            # print(type(response))
            # print(response)

            return templates.TemplateResponse("results.html", {"request": request, 
                                                           "date": response["dateOfCreation"],
                                                           "time" : response["timeOfCreation"],
                                                           "nameoftrend1" : response["nameoftrend1"],
                                                           "nameoftrend2" : response["nameoftrend2"],
                                                           "nameoftrend3" : response["nameoftrend3"],
                                                           "nameoftrend4" : response["nameoftrend4"],
                                                           "nameoftrend5" : response["nameoftrend5"],
                                                           "ip" : response["ip"],
                                                           "JSON" : response})
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except httpx.RequestError as req_err:
            print(f"Request error occurred: {req_err}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")

@router.get('/refreshfeed')
async def put_trendings(request : Request):
    global latest_id
    inputvalues = refresh_scraper_func()
    print(inputvalues , 'from method')
    result = collection_name.insert_one(dict(inputvalues))
    latest_id =  result.inserted_id
    print(latest_id)
    async with httpx.AsyncClient() as client:
        try :
            response2 = await client.get("http://127.0.0.1:8000/finalendpoint")
            response = response2.json()
            # response = Trending_list(**response1)
            # print(type(response))
            # print(response)

            return templates.TemplateResponse("results.html", {"request": request, 
                                                           "date": response["dateOfCreation"],
                                                           "time" : response["timeOfCreation"],
                                                           "nameoftrend1" : response["nameoftrend1"],
                                                           "nameoftrend2" : response["nameoftrend2"],
                                                           "nameoftrend3" : response["nameoftrend3"],
                                                           "nameoftrend4" : response["nameoftrend4"],
                                                           "nameoftrend5" : response["nameoftrend5"],
                                                           "ip" : response["ip"],
                                                           "JSON" : response})
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except httpx.RequestError as req_err:
            print(f"Request error occurred: {req_err}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")



    

        












    
