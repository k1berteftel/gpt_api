from typing import Literal

from pydantic import BaseModel


class GenerationResponse(BaseModel):
    prompt: str
    image_url: str | None = None
    model_name: Literal[
        'kling', 'seedance_lite', 'seedance_pro'
    ]
    duration: int = 5
    aspect_ratio: Literal['16:9', '9:16'] = '16:9'
