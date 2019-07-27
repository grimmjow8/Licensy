import logging
import json


class ConfigHandler:
    CONFIG_PATH = "config.json"

    def __init__(self):
        self.logger = logging.getLogger("discord")
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Loads config and checks fo validity of json file.
        :return: dict loaded json data
        """
        try:
            with open(ConfigHandler.CONFIG_PATH) as cfg:
                data = json.load(cfg)
                return data
        except FileNotFoundError as e:
            self.logger.critical(f"Config json file was not found: {ConfigHandler.CONFIG_PATH} : {e}")
        except ValueError as e:
            self.logger.critical(f"Invalid config json: {e}")
        except KeyError as e:
            self.logger.critical(f"Invalid json config configuration: {e}")
        except Exception as e:
            self.logger.critical(f"Can't load json config: {e}")

    def get_token(self):
        return self.get_key("token")

    def get_default_prefix(self):
        return self.get_key("default_prefix")

    def get_bot_status(self):
        return self.get_key("bot_status")

    def get_developers(self):
        return self.get_key("developers")

    def get_key(self, key):
        try:
            return self.config[key]
        except KeyError as e:
            error_message = f"Key '{key}' not found in json config! {e}"
            self.logger.critical(error_message)
            raise KeyError(error_message)

    def update_status(self, status):
        self.update_key("bot_status", status)

    def update_key(self, key, value):
        try:
            self.config[key] = value
            print(self.config)
            with open(ConfigHandler.CONFIG_PATH, "w") as cfg:
                # key vars are used to prettify outputted json
                json.dump(self.config, cfg, indent=4, sort_keys=True)
        except KeyError as e:
            self.logger.critical(f"Key '{key}' not found in json config! Can't update config! {e}")
        except TypeError as e:
            self.logger.critical(f"Unable to serialize the object {e}")
        except Exception as e:
            self.logger.critical(f"Unable to update json key {key} to value {value}: {e}")