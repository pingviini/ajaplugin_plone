import logging
import tempfile

from aja.deploy.base import DeployBase
from aja.rsync import Rsync
from aja.buildout import AjaBuildout

from .config import DeployParser


class PloneDeploy(DeployBase):
    """Aja Plone deployment support."""

    def __init__(self, config, arguments):
        self.config = config
        self.deploy_config = DeployParser(self.config)
        self.arguments = arguments
        self.path = "{buildouts}/{name}".format(
            buildouts=self.config.buildouts_folder,
            name=self.config.name)
        self.buildout = AjaBuildout(self.config, self.arguments)

    def deploy(self):
        excludes = self.deploy_config.ignores
        rsync = Rsync(
            self.buildout.buildout_config['buildout']['eggs-directory'],
            path=self.path,
            excludes=excludes,
            target=self.config.deployment_target,
            arguments=self.arguments,
            effective_user=self.config.effective_user)
        rsync.push()

    def generate_ignores(self):
        tmp_ignore = tempfile.NamedTemporaryFile()
        for ignore in self.deploy_config.ignores:
            tmp_ignore.write(ignore)
        return tmp_ignore.name

    def deploy_eggs(self):
        excludes = self.deploy_config.ignores
        rsync = Rsync(
            self.buildout.buildout_config['buildout']['eggs-directory'],
            files=self.buildout.eggs,
            excludes=excludes,
            target=self.config.deployment_target,
            arguments=self.arguments,
            effective_user=self.config.effective_user)

        rsync.push()
