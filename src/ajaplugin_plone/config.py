from ConfigParser import (
    ConfigParser,
    NoSectionError
    )


class DeployConfigParser(ConfigParser):

    def get_list(self, section, option):
        value = self.get(section, option)
        return list(filter(None, (x.strip() for x in value.splitlines())))

    def get_tuple(self, section, option):
        try:
            value = self.get(section, option)
        except NoSectionError:
            return None

        return tuple(filter(None, (x.strip() for x in value.splitlines())))

    def get_list_int(self, section, option):
        return [int(x) for x in self.get_list(section, option)]


class DeployParser(object):
    """Parse deployment related configuration."""

    def __init__(self, config):
        self.config = config
        self.parser = DeployConfigParser()
        self.config_path = "{site_config_folder}/{name}.cfg".format(
            site_config_folder=self.config.buildouts_config_folder,
            name=self.config.name)
        self.parser.read(self.config_path)

    @property
    def ignores(self):
        return self.parser.get_tuple('deploy:plone', 'ignores')