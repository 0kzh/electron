#!/usr/bin/env python

import platform
import sys

NODE_VERSION = 'v0.11.13'
BASE_URL = 'https://gh-contractor-zcbenz.s3.amazonaws.com/libchromiumcontent'
LIBCHROMIUMCONTENT_COMMIT = '9006e277b20109de165d4a17827c9b2029bf3831'

ARCH = {
    'cygwin': '32bit',
    'darwin': '64bit',
    'linux2': platform.architecture()[0],
    'win32': '32bit',
}[sys.platform]
DIST_ARCH = {
    '32bit': 'ia32',
    '64bit': 'x64',
}[ARCH]

TARGET_PLATFORM = {
  'cygwin': 'win32',
  'darwin': 'darwin',
  'linux2': 'linux',
  'win32': 'win32',
}[sys.platform]
