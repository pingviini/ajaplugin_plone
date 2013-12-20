from ConfigParser import ConfigParser


class DeployConfigParser(ConfigParser):

    def getlist(self, section, option):
        value = self.get(section, option)
        return list(filter(None, (x.strip() for x in value.splitlines())))

    def gettuple(self, section, option):
        value = self.get(section, option)
        return tuple(filter(None, (x.strip() for x in value.splitlines())))

    def getlistint(self, section, option):
        return [int(x) for x in self.getlist(section, option)]


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
        return self.parser.gettuple('deploy:plone', 'ignores')