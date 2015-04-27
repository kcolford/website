# Main method.

# Copyright (C) 2015 Kieran Colford
#
# This file is part of UWaterloo-AddCourse.
#
# UWaterloo-AddCourse is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# UWaterloo-AddCourse is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with UWaterloo-AddCourse.  If not, see
# <http://www.gnu.org/licenses/>.


"""The main method for this package."""

import argparse
import getpass
try:
    import readline
except ImportError:
    pass
from .course_adder import addcourse
from . import __version__


def main():
    """Main function."""

    parser = argparse.ArgumentParser(
        description='Repeatedly ask QUEST to add you into a particular course.',
    )
    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + __version__)

    args = parser.parse_args()

    course = raw_input('Desired Course: ')
    user = raw_input('QUEST ID: ')
    password = getpass.getpass('Password: ')
    addcourse(user, password, course)
