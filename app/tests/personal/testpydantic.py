import datetime

import pydantic

import typing
import datetime

def format_datetime_into_isoformat(date_time: datetime.datetime) -> str:
    return date_time.replace(tzinfo=datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
def format_dict_key_to_camel_case(dict_key: str) -> str:
    return "".join(word if idx ==0 else word.capitalize() for idx, word in enumerate(dict_key.split('_')))



class BaseSchemaModel(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        from_attributes: bool = True
        validate_assignment: bool = True
        populate_by_name: bool = True
        json_encoders: dict = {datetime.datetime: format_datetime_into_isoformat}
        alias_generator: typing.Any = format_dict_key_to_camel_case


class AccountWithToken(BaseSchemaModel):
    token: str
    username: str
    email: pydantic.EmailStr
    is_verified: bool
    is_active: bool
    is_logged_in: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class AccountInResponse(BaseSchemaModel):
    id: int
    authorized_account: AccountWithToken

a = AccountWithToken(token="xx", username="yy", email="zz@gmail.com", isVerified=True, is_active=True, is_logged_in=True, created_at=datetime.datetime.now(), updated_at=None)
