from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

# Custom exception for when an entity is not found in the database
class EntityNotFound(HTTPException):
    def __init__(self, entity: str, entity_id: int):
        super().__init__(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"{entity} with ID {entity_id} not found"
        )

# Custom exception for bad requests (e.g., invalid data)
class BadRequestError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=HTTP_400_BAD_REQUEST,
            detail=detail
        )
