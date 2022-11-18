from typing import TypedDict


class OutputCommonParametersDto(TypedDict):
    page: int
    size: int


async def common_parameters(page: int = 1, size: int = 10) -> OutputCommonParametersDto:
    return {"page": page, "size": size}
