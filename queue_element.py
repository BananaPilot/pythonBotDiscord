from typing import Any, TypedDict

class QueueElementType(TypedDict):
    id: str
    fulltitle: str
    url: str
    duration: int
    webpage_url: str


class QueueElement:
    @staticmethod
    def create(track_info: dict[str, Any]) -> QueueElementType:
        return {
            "id": track_info["id"],
            "fulltitle": track_info["fulltitle"],
            "url": track_info["url"],
            "duration": track_info["duration"],
            "webpage_url": track_info["webpage_url"],
        }
