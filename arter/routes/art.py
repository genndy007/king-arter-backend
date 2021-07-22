from fastapi import APIRouter, status

router = APIRouter(
    prefix='/art',
    tags=['Arts']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_art():
    pass


@router.get('/{art_id}', status_code=status.HTTP_200_OK)
async def get_art(art_id: int):
    pass


@router.put('/{art_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_art(art_id: int):
    pass


@router.delete('/{art_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_art(art_id: int):
    pass
