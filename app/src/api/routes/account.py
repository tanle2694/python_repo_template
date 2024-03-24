import fastapi
import pydantic


router = fastapi.APIRouter(prefix="/accounts", tags=["accounts"])

@router.get(
    path="",
    name="accounts:read-accounts",
    response_model="",
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_accounts():
    return ""

@router.get(
    path="/{id}",
    name="accounts:read-account-by-id",
    response_model="",
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_account(
    id: int,
):
    return ""


@router.patch(
    path="/{id}",
    name="accounts:update-account-by-id",
    response_model="",
    status_code=fastapi.status.HTTP_200_OK,
)
async def update_account(
):
    return ""


@router.delete(
    path="",
    name="accounts:delete-account-by-id",
    status_code=fastapi.status.HTTP_200_OK,
)
async def delete_account():
    return ""