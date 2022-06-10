from enum import Enum
from pydantic import BaseModel

class SEARCH_TYPE(Enum):
    TRACK = 'track'
    ARTISTS = 'artists'
    ALBUMS = 'albums'

class SearchSchema(BaseModel):
    search_type: SEARCH_TYPE = SEARCH_TYPE.TRACK
    query: str
