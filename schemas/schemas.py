from pydantic import BaseModel

class trending_list_in(BaseModel):
    nameoftrend1: str
    nameoftrend2: str
    nameoftrend3: str
    nameoftrend4: str
    nameoftrend5: str
    dateofcreation : str
    timeofcreation : str
    ip : str

class Trending_list(trending_list_in):
    id :str

