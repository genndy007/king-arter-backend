from fastapi import APIRouter, status

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user():
    pass


@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    pass


@router.put('/{user_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id: int):
    pass


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    pass
