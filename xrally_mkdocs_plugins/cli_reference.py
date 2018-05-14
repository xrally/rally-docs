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
import re
import sys

import pkg_resources
import pkgutil
#from rally.common import version
#from rally.common.plugin import discover
#from rally.common.plugin import plugin as base_plugin
#from rally import plugins as r_plugins

#from xrally_mkdocs_plugins import r2m


####

import copy
import inspect

from rally.cli import cliutils
from rally.cli import main

from xrally_mkdocs_plugins import base
from xrally_mkdocs_plugins import mdutils


class Parser(object):
    """A simplified interface of argparse.ArgumentParser"""
    def __init__(self):
        self.parsers = {}
        self.subparser = None
        self.defaults = {}
        self.arguments = []

    def add_parser(self, name, help=None, description=None,
                   formatter_class=None):
        parser = Parser()
        self.parsers[name] = {"description": description,
                              "help": help,
                              "fclass": formatter_class,
                              "parser": parser}
        return parser

    def set_defaults(self, command_object=None, action_fn=None,
                     action_kwargs=None):
        if command_object:
            self.defaults["command_object"] = command_object
        if action_fn:
            self.defaults["action_fn"] = action_fn
        if action_kwargs:
            self.defaults["action_kwargs"] = action_kwargs

    def add_subparsers(self, dest):
        # NOTE(andreykurilin): there is only one expected call
        if self.subparser:
            raise ValueError("Can't add one more subparser.")
        self.subparser = Parser()
        return self.subparser

    def add_argument(self, *args, **kwargs):
        if "action_args" in args:
            return
        self.arguments.append((args, kwargs))


def get_defaults(func):
    """Return a map of argument:default_value for specified function."""
    spec = inspect.getargspec(func)
    if spec.defaults:
        return dict(zip(spec.args[-len(spec.defaults):], spec.defaults))
    return {}


@base.configure("cli_reference")
class CLIReference(base.RallyMKDocsPluginBase):

    @classmethod
    def _make_arguments_section(cls, category_name, command, arguments,
                                defaults):
        defin = mdutils.DefinitionsList(
            "Command arguments", prefix="%s_%s_" % (category_name, command))

        for args, kwargs in arguments:
            # for future changes...
            # :param args: a single command argument which can represented by
            #       several names(for example, --uuid and --task-id) in cli.
            # :type args: tuple
            # :param kwargs: description of argument. Have next format:
            #       {"dest": "action_kwarg_<name of keyword argument in code>",
            #        "help": "just a description of argument"
            #        "metavar": "[optional] metavar of argument."
            #                   "Example: argument '--file'; metavar 'path' ",
            #        "type": "[optional] class object of argument's type",
            #        "required": "[optional] boolean value"}
            # :type kwargs: dict
            dest = kwargs.get("dest").replace("action_kwarg_", "")
            description = []
            description.append(kwargs.get("help", ""))

            action = kwargs.get("action")
            if not action:
                arg_type = kwargs.get("type")
                if arg_type:
                    description.append("*Type*: %s" % arg_type.__name__)

                skip_default = dest in ("deployment",
                                        "task_id",
                                        "verification")
                if not skip_default and dest in defaults:
                    description.append("*Default*: %s" % defaults[dest])
            metavar = kwargs.get("metavar")

            if metavar:
                args = ["%s %s" % (arg, metavar) for arg in args]
            try:
                defin.add_term(", ".join(args), description)
            except TypeError:
                import pdb;pdb.set_trace()
        return defin.to_md()

    @classmethod
    def modify_markdown(cls, markdown, page, config, site_navigation):
        """Alter the Markdown source text with CLI reference.

        :param markdown: Markdown source text of page as string
        :param page: `mkdocs.nav.Page` instance
        :param config: global configuration object
        :param site_navigation: global navigation object

        :returns: Markdown source text of page as string
        """
        parser = Parser()

        categories = copy.copy(main.categories)
        cliutils._add_command_parsers(categories, parser)

        content = []
        for cg in sorted(categories.keys()):
            if cg == "deployment":
                # oops. let's skip it
                continue
            cparser = parser.parsers[cg]["parser"]
            content.append("## Category: %s" % cg)
            # NOTE(andreykurilin): we are re-using `_add_command_parsers`
            #   method from `rally.cli.cliutils`, but, since it was designed
            #   to print help message, generated description for categories
            #   contains specification for all sub-commands. We don't need
            #   information about sub-commands at this point, so let's skip
            #   "generated description" and take it directly from category
            #   class.
            description = cparser.defaults["command_object"].__doc__
            content.append(description)

            for command in sorted(cparser.subparser.parsers.keys()):
                subparser = cparser.subparser.parsers[command]

                content.append("### rally %s %s" % (cg, command))
                content.append(subparser["description"])

                if subparser["parser"].arguments:
                    defaults = get_defaults(
                        subparser["parser"].defaults["action_fn"])
                    content.append(cls._make_arguments_section(
                        cg, command, subparser["parser"].arguments,
                        defaults))

        return markdown.replace("!%s" % cls.get_name(), "\n\n".join(content))
