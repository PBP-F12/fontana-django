from typing import Mapping, NotRequired, Optional, TypeVar, Generic, TypedDict, Literal, Any
from rest_framework.response import Response as RESTResponse
from rest_framework import status as rest_status

HttpStatus = Literal[
    100,
    101,
    102,
    103,
    200,
    201,
    202,
    203,
    204,
    205,
    206,
    207,
    208,
    226,
    300,
    301,
    302,
    303,
    304,
    305,
    307,
    308,
    400,
    401,
    402,
    403,
    404,
    405,
    406,
    407,
    408,
    409,
    410,
    411,
    412,
    413,
    414,
    415,
    416,
    417,
    418,
    421,
    422,
    423,
    424,
    425,
    426,
    427,
    428,
    429,
    431,
    451,
    500,
    501,
    502,
    503,
    504,
    505,
    506,
    507,
    508,
    510,
    511,
]

T = TypeVar("T")
MessageResponseType = str
DataResponseType = Optional[T]
StatusResponseType = HttpStatus
TemplateNameResponseType = Optional[str]
HeadersResponseType = Optional[Mapping[str, str]]
ExceptionResponse = bool
ContentTypeResponse = Optional[str]


class ResponseDict(TypedDict):
    code: HttpStatus
    success: bool
    data: NotRequired[Any]
    message: str


class Response(RESTResponse, Generic[T]):
    def __init__(
        self,
        message: MessageResponseType,
        data: DataResponseType[T] = None,
        status: StatusResponseType = rest_status.HTTP_200_OK,
        template_name: TemplateNameResponseType = None,
        headers: HeadersResponseType = None,
        exception: ExceptionResponse = False,
        content_type: ContentTypeResponse = None,
    ) -> None:
        response_data: ResponseDict = {
            "code": status,
            "success": rest_status.is_success(status),
            "message": message,
        }

        if data:
            response_data["data"] = data

        super().__init__(
            response_data, status, template_name, headers, exception, content_type
        )
