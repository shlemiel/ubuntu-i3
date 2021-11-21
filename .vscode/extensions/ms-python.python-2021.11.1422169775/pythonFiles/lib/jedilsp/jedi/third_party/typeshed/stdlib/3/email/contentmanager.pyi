# Stubs for email.contentmanager (Python 3.4)

from typing import Any, Callable
from email.message import Message

class ContentManager:
    def __init__(self) -> None: ...
    def get_content(self, msg: Message, *args: Any, **kw: Any) -> Any: ...
    def set_content(self, msg: Message, obj: Any, *args: Any,
                    **kw: Any) -> Any: ...
    def add_get_handler(self, key: str, handler: Callable[..., Any]) -> None: ...
    def add_set_handler(self, typekey: type,
                        handler: Callable[..., Any]) -> None: ...

raw_data_manager: ContentManager
