from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(packages=["app"])