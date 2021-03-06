# Copyright 2015-2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import yaml

from argparse import ArgumentParser

class DockerfileArgParser(ArgumentParser):
    """Argument parser class Dockerfile auto generation"""

    def set(self):
        """Setup parser for Dockerfile auto generation"""

        # create the top-level parser
        subparsers = self.add_subparsers(help='help for subcommand', dest='subparser_name')

        # create the parser for the "explicit" command
        parser_explicit = subparsers.add_parser(
            'explicit',
            help='explicit --help')
        parser_explicit.add_argument(
            '-p', '--platform',
            required=True,
            help="Path to platform config")
        parser_explicit.add_argument(
            '-i', '--images',
            required=True,
            help="Path to images config")
        parser_explicit.add_argument(
            '-o', '--output',
            required=True,
            help="Path to write generate Dockerfiles")

        # create the parser for the "dir" command
        parser_dir = subparsers.add_parser(
            'dir',
            help='dir --help')
        parser_dir.add_argument(
            '-d', '--directory',
            required=True,
            help="Path to read config and write output")

    def parse(self, argv):
        args = self.parse_args(argv)

        # If given directory path
        if args.subparser_name == 'dir':
            platform_path = 'platform.yaml'
            images_path = 'images.yaml.em'
            args.platform =  os.path.join(args.directory, platform_path)
            args.images = os.path.join(args.directory, images_path)
            args.output = args.directory

        return args


class DockerfolderArgParser(ArgumentParser):
    """Argument parser class Dockerfolder auto generation"""

    def set(self):
        """Setup parser for Dockerfolder auto generation"""

        # create the top-level parser
        subparsers = self.add_subparsers(help='help for subcommand', dest='subparser_name')

        # create the parser for the "explicit" command
        parser_explicit = subparsers.add_parser(
            'explicit',
            help='explicit --help')
        parser_explicit.add_argument(
            '-m', '--manifest',
            required=True,
            help="Path to manifest config")
        parser_explicit.add_argument(
            '-o', '--output',
            required=True,
            help="Path to write generate Dockerfiles")
        parser_explicit.add_argument(
            '-a', '--auto',
            action='store_true',
            help="Auto generate Dockerfiles files in docker folders")

        # create the parser for the "dir" command
        parser_dir = subparsers.add_parser(
            'dir',
            help='dir --help')
        parser_dir.add_argument(
            '-d', '--directory',
            required=True,
            help="Path to read config and write output")
        parser_dir.add_argument(
            '-a', '--auto',
            action='store_true',
            help="Auto generate Dockerfiles files in docker folders")

    def parse(self, argv):
        args = self.parse_args(argv)

        # If given directory path
        if args.subparser_name == 'dir':
            manifest_path = 'manifest.yaml'
            args.manifest =  os.path.join(args.directory, manifest_path)
            args.output = args.directory

        return args


class DockerlibraryArgParser(ArgumentParser):
    """Argument parser class Dockerlibrary auto generation"""

    def set(self):
        """Setup parser for Dockerlibrary auto generation"""

        self.add_argument(
            '-m', '--manifest',
            required=True,
            help="Path to manifest config")
        self.add_argument(
            '-o', '--output',
            required=True,
            help="Path to write generate Dockerlibrary")

    def parse(self, argv):
        args = self.parse_args(argv)
        return args
