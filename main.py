import os

import click
import uvicorn
from core.config.settings import settings


# @click.command()
# @click.option(
#     "--env",
#     type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
#     default="local",
# )
# @click.option(
#     "--debug",
#     type=click.BOOL,
#     is_flag=True,
#     default=False,
# )

def main():
    uvicorn.run(
        app="app.server:app",
        host=settings.app.app_host,
        port=settings.app.app_port,
        reload=True if settings.app.env != "production" else False,
        workers=1,
    )

if __name__ == "__main__":
    main()
