# Network utilities for the MPU-package manager, written by Matheus Artur

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from libpath import *
import os, errno, sys

mpu_repository=str("https://gitlab.com/mpu-pkg-manager/mpu-packages/raw/master/")

def unpack():
    os.system(src_path+"./unpack-tarball.sh")
    
def download(packages):
    for pack in packages:
        os.system("wget " + mpu_repository + str(pack[:-4])+".tbz2")

    os.system("mv *.tbz2 "+ pack_path)
    unpack()
