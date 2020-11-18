# PyConfig

### Automatic Python Environment Variable Configuration Package

## Description

**PyConfig** is a DevOps tool that helps Python developers to efficiently import various configuration files into their environment. It also automates config file exports to VCS such as Git while hiding sensitive information.

## Installation

Install **PyConfig** with Pip:
```bash
pip install pyconfig-env
```
Upgrade using the `-U` flag:
```bash
pip install -U pyconfig-env
```

## Usage

### Importing into the environment

After installing, import **PyConfig** into your main Python file:
```python3
import pyconfig
```
Then you can import configurations as Python files, JSON objects, JSON files, or .env files:
```python3
# Python file
pyconfig.parse_py('config.py')

# JSON object
json_dict = {'DEBUG': True}
pyconfig.parse_json_obj(json_dict)

# JSON file
pyconfig.parse_json('config.json')

# .env file
pyconfig.parse_env('config.env')
```
The variables can be accessed anywhere in the Python program via `os.environ`:
```python3
print(os.environ['DEBUG'])  # Prints True
```

### Exporting a file for VCS

**PyConfig** currently only supports exporting Python config files for VCS. In order to make use of this feature, first ensure that the original config file is hidden from the VCS. For example, with Git, add the filename to a `.gitignore` file.
```
# config.py - This file was added to .gitignore

DEBUG = True  # Ending a line with an asterisk (*) denotes a variable that is safe to upload in the VCS system*
SECRET = 'database password'  # All other variables will be cleared for the template configuration file (config.py.sample)
```
Then simply generate the template configuration file:
```python3
pyconfig.py_template('config.py')  # Creates config.py.sample
```
```
# config.py.sample

DEBUG = True  # Ending a line with an asterisk (*) denotes a variable that is safe to upload in the VCS system
SECRET = ''  # All other variables will be cleared for the template configuration file (config.py.sample)
```
As shown above, the entire file remained exactly the same, except that the variables which were not marked as safe had their values cleared. The asterisks at the end of the lines were also removed, as they are unnecessary for the VCS system itself.

## Developers

Ashish D'Souza - [@computer-geek64](https://github.com/computer-geek64)

## Releases

The current stable release for **PyConfig** is [v1.0.0](https://github.com/computer-geek64/timelock/releases/latest)

It is also released as a Python package on [PyPI](https://pypi.org/project/pyconfig-env/) (the Python Package Index).

## Versioning

This project is uses the [Git](https://git-scm.com/) Version Control System (VCS).

## License

This project is licensed under the [MIT License](LICENSE).
