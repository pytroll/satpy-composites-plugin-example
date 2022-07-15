# Example Satpy Plugin Package - Composites

[![CI](https://github.com/pytroll/satpy-composites-plugin-example/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/pytroll/satpy-composites-plugin-example/actions/workflows/ci.yaml)

This is a toy package to show how to make an independent package that adds
or changes functionality to Satpy. This package specifically adds new
composites, but Satpy also supports adding readers, writers, and enhancements.

See the
[Satpy Plugin Documentation](https://satpy.readthedocs.io/en/latest/dev_guide/plugins.html)
for more information.

## Install

This package is *NOT* available from PyPI or conda. It is purely an example and
proof of concept. It is only possible to install this package from source. If
you are hoping to use this package as a starting point then you likely want to
install it in "editable" mode. This can be done by running:

```bash
pip install -e .
```

This will make any changes to the Python or YAML content in your package
available to your scripts automatically. However, if you change the entry point
definitions in the ``pyproject.toml`` (or ``setup.py``) you will likely need
to reinstall the package by running the above command again.

## Repository contents

This project contains five types of files and directories in addition to this README:

1. ``pyproject.toml``: The package and entry point definitions. You could also
   implement this in a ``setup.py`` 
2. ``satpy_cpe``: The plugin Python package.
3. ``satpy_cpe/etc``: The plugin component configuration directory where custom
   YAML files are stored.
4. ``.github``: Automated tests run automatically on GitHub. These exist
   primarily to verify that this example still works with the upstream Satpy
   package. It is not technically required to make a Satpy plugin package.
5. ``.gitignore``: This file tells ``git`` which files not to include when
   working with ``git`` to update this GitHub project repository. This is also
   not technically needed for the plugin package to work, but is highly 
   recommended in your own projects to avoid committing unwanted files to git.

See the Satpy Plugin Documentation linked above.
