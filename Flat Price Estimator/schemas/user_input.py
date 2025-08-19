from pydantic import BaseModel, Field
from typing import Annotated

class InputData(BaseModel):
    sector: Annotated[int, Field(..., description="Location of the flat")]
    bedRoom: Annotated[int, Field(..., description="Number of bedrooms")]
    bathroom: Annotated[int, Field(..., description="Number of bedrooms")]
    balcony: Annotated[int, Field(..., description="Number of balconies")]
    agePossession: Annotated[int, Field(..., description="Age of property (in years)")]
    built_up_area: Annotated[float, Field(..., description="Builtup area the flat")]
    servant_room: Annotated[int, Field(..., description="number of servant rooms")]
    furnishing_type: Annotated[int, Field(..., description="Furnished or Unfurnished flat?")]
    luxury_category: Annotated[int, Field(..., description="Luxury Standard..")]
    floor_category: Annotated[int, Field(..., description="floor preference of the flat..")]