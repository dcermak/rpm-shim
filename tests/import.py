# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import logging

# enable debug logging
logging.basicConfig(level=logging.DEBUG)


def test():
    import rpm

    # sanity check
    print("RPM conf dir:", rpm.expandMacro("%getconfdir"))

    from pathlib import Path
    import sys

    assert len(rpm.__path__) == 1
    rpm_path = rpm.__path__[0]
    python_path = sys.path

    for site_dir in python_path:
        if Path(rpm_path).is_relative_to(Path(site_dir)):
            break
    else:
        raise RuntimeError(f"{rpm_path} is not relative to any python path: {python_path}")


if __name__ == "__main__":
    test()
