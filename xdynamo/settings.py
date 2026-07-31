from typing import Protocol

from xcon import xcon_settings


class ShouldAutoCreateTableCallable(Protocol):
    def __call__(self, table_name: str) -> bool:
        raise NotImplementedError


_auto_create_table_only_in_environments = {'unittest', 'local'}


def default_should_auto_create_table(table_name: str) -> bool:
    return xcon_settings.environment in _auto_create_table_only_in_environments


should_auto_create_callable: ShouldAutoCreateTableCallable = default_should_auto_create_table
