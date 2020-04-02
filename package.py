# -*- coding: utf-8 -*-
name = 'pycharm_ce'

# Vendor packages: <vendor_version>+local.<our_version>
__version__ = '2019.3.4'
version = __version__ + '+local.1.0.0'

description = 'The Python IDE for Professional Developers'

authors = ['JetBrains', 'Joseph Yu']

variants = [['platform-linux', 'arch-x86_64']]

tools = ['pycharm']
# @late()
# def tools():
#     import os
#     bin_path = os.path.join(str(this.root), 'bin')
#     executables = []
#     for item in os.listdir(bin_path):
#         path = os.path.join(bin_path, item)
#         if os.access(path, os.X_OK) and not os.path.isdir(path):
#             executables.append(item)
#     return executables


build_command = r'''
set -euf -o pipefail

# Setup: curl "{CURL_FLAGS}" ...
# Show progress bar if output to terminal, else silence
declare -a CURL_FLAGS
CURL_FLAGS=("-L")
[ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")

URL="https://download.jetbrains.com/python/pycharm-community-{version}.tar.gz"

if [[ $REZ_BUILD_INSTALL -eq 1 ]]
then
    set -x
    curl "{CURL_FLAGS}" "$URL" \
    | tar --strip-components=1 -xz -C "$REZ_BUILD_INSTALL_PATH"

    # Setup our own executables that we can call from PATH
    mkdir -p "$REZ_BUILD_INSTALL_PATH"/local/bin
    ln -srf \
        "$REZ_BUILD_INSTALL_PATH"/bin/pycharm.sh \
        "$REZ_BUILD_INSTALL_PATH"/local/bin/pycharm
fi

'''.format(version=__version__, CURL_FLAGS='${{CURL_FLAGS[@]}}')


def commands():
    """Commands to set up environment for ``rez env vscode``"""
    import os
    env.PATH.append(os.path.join('{root}', 'local', 'bin'))
