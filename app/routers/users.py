from typing import Dict, List
from fastapi import APIRouter
from app.db.breaking_bad.breaking_bad import data

router = APIRouter()


@router.get('/api/breakingbad/character/', tags=['characters'])
async def read_users() -> List[Dict]:
    return data


@router.get('/api/breakingbad/character/{user_id}', tags=['characters'])
async def read_user_by_id(user_id: int) -> Dict:
    users = data.get('results')
    for user in users:
        if user.get('id') == user_id:
            return user
    return {'message': f'No such user: {user_id}'}
