from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class CMBot:
    """
    Creates the TgBot object from environment variables.
    """

    token: str
    admin_ids: list[int]
  
    @staticmethod
    def from_env(env: Env):
        """
        Creates the CMBot object from environment variables.
        """
        token = env.str("BOT_TOKEN")
        admin_ids = list(map(int, env.list("ADMINS")))
        return CMBot(token=token, admin_ids=admin_ids)


@dataclass
class Config:
    """
    The main configuration class that integrates all the other configuration classes.

    This class holds the other configuration classes, providing a centralized point of access for all settings.

    Attributes
    ----------
    cm_bot : CMBot
        Holds the settings related to the Telegram Bot.
    """

    cm_bot: CMBot


def load_config(path: str = None) -> Config:
    """
    This function takes an optional file path as input and returns a Config object.
    :param path: The path of env file from where to load the configuration variables.
    It reads environment variables from a .env file if provided, else from the process environment.
    :return: Config object with attributes set as per environment variables.
    """

    # Create an Env object.
    # The Env object will be used to read environment variables.
    env = Env()
    env.read_env(path)

    return Config(
        cm_bot=CMBot.from_env(env),
    )