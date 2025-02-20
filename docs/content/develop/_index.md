---
title: "Development Setup"
---

## Installing Python

Generally, we need Python 3.
This guides through the setup.

### Windows

On Windows, you can download and install Python 3 from [Python.org](https://www.python.org/).

### Linux

You can use the system installation of Python.
Also, create a virtual environment.

Check that you have Python3 installed:

```sh
python3 --version
```

#### Debian/Ubuntu

Install these packages:

```sh
sudo apt install python3 python3-pip python3-tk
```

### MacOS

Under MacOS, use [brew].

```sh
brew install python python-tk create-dmg
```

[brew]: https://brew.sh/

## Setup

To setup this software for development, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/niccokunzmann/simple_dhcp_server.git
    cd simple_dhcp_server
    ```

2. Install [tox]:

    ```sh
    pip install tox
    ```

## Running Tests

The `tox.ini` file has several environments that can be used to run the tests.

```sh
tox
```

## Documentation

For the docuentation, we use [Hugo].
Install hugo and run it.

```sh
# in the repository
cd docs
hugo serve
```

And head over to the website.

## New Releases

When the source code is changed, create a new release.

1. Log the changes:

    - `docs/changes/_index.md`
    - `flatpak/io.github.niccokunzmann.python_dhcp_server.xml`

    ```sh
    git log # find changes
    git add docs/changes/_index.md flatpak/io.github.niccokunzmann.python_dhcp_server.xml
    git commit -m"log changes"
    ```

2. Create a new tag

    ```sh
    git tag 1.0.3
    git push origin 1.0.3
    ```

3. Head over to [the Flathub metadata](https://github.com/niccokunzmann/io.github.niccokunzmann.python_dhcp_server/)
   and create a new release.


[Hugo]: https://gohugo.io/
