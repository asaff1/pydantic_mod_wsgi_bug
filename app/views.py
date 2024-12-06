from typing import Annotated

from ninja import NinjaAPI, Form
from pydantic import ConfigDict, BaseModel, StringConstraints

router = NinjaAPI()


class PayloadString(BaseModel):
    # This works with apache
    string: str


class PayloadStringStrip(BaseModel):
    # This will fail with apache
    string: str

    model_config = ConfigDict(str_strip_whitespace=True)


class PayLoadStringConstraints(BaseModel):
    number: Annotated[str, StringConstraints(pattern=r"^0\d\d$", strip_whitespace=True)]



@router.post("/payload_string")
def payload_string(request, payload: Form[PayloadString]):
    # Works with no issues
    return {"status": "OK", "payload": payload.model_dump()}


@router.post("/payload_string_strip")
def payload_string_strip(request, payload: Form[PayloadStringStrip]):
    # Won't work in apache
    return {"status": "OK", "payload": payload.model_dump()}



@router.post("/payload_string_constraints")
def payload_string_constraints(request, payload: Form[PayLoadStringConstraints]):
    # This works only if you input a non-valid number, e.g '11'. For a valid input like '123', apache will freeze
    return {"status": "OK", "payload": payload.model_dump()}
