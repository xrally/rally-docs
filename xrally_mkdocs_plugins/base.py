# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import importlib
import os
import sys

from rally.common.plugin import plugin

from mkdocs.plugins import BasePlugin


def configure(name):
    """Initialize a plugin.

    NOTE: platform name is hardcoded to '_mkdocs' and 'hidden' attribute is
        always True, so such plugins will not be displayed in Rally plugins
        reference.
    """
    return plugin.configure(name, platform="_mkdocs", hidden=True)


class RallyMKDocsPluginBase(plugin.Plugin):
    """A base class for Rally MKDocs plugins"""
    @classmethod
    def modify_markdown(cls, markdown, page, config, site_navigation):
        """Modifies page content.

        Should be called when "!<plugin_name>" is detected (where
        "<plugin_name>" is a name of a plugin, i.e. result of .get_name() call)
        """
        return markdown


class RallyMKDocs(BasePlugin):
    """An entry-point for all custom rally plugins for MKDocs.

    The "plugin" feature in MKDocs requires specifying each plugin separately
    in setup.cfg/setup.py file + enabling it via ``mkdocs.yml`` configuration
    file.
    The great achievement of Rally framework is absence of such hardcoded
    things. This class adopts pluggable feature from Rally to MKDocs purpose.

    The usage:
    """

    def __init__(self):
        self._loaded = False

    def load(self):
        """Ensure that plugins are loaded."""
        if not self._loaded:
            # NOTE(andreykurilin): The following code is a modifyied version of
            #   ``rally.common.plugin.discover.import_modules_from_package``.
            #   The only difference is that is imports modules outside rally
            #   framework dir.
            home = os.path.dirname(os.path.abspath(__file__))
            for root, dirs, files in os.walk(os.path.dirname(__file__)):
                for filename in files:
                    if filename.startswith("__") or not filename.endswith(
                            ".py"):
                        continue
                    root = root.replace(home, "xrally_mkdocs_plugins")
                    root = root.replace("/", ".")
                    module_name = "%s.%s" % (root, filename[:-3])
                    if module_name not in sys.modules:
                        sys.modules[module_name] = importlib.import_module(
                            module_name)

            self._loaded = True

    def on_page_markdown(self, markdown, page, config, site_navigation):
        self.load()
        for p in RallyMKDocsPluginBase.get_all(allow_hidden=True):
            if "!%s" % p.get_name() in markdown:
                markdown = p.modify_markdown(markdown, page, config,
                                             site_navigation)
        return markdown
