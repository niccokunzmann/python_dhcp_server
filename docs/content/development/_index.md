+++
title = "Development"
type = "chapter"
weight = 1
+++

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

## New Releases

When the source code is changed, create a new release.

1. Log the changes: Edit the Changelog Section in

    - `README.md`
    - `python_dhcp_server/flatpak/io.github.niccokunzmann.python_dhcp_server.xml`

    ```sh
    git log # find changes
    git add README.md
    git commit -m"log changes"
    ```

2. Create a new tag

    ```sh
    git tag 1.0.3
    git push origin 1.0.3
    ```

3. Head over to [the Flathub metadata](https://github.com/niccokunzmann/io.github.niccokunzmann.python_dhcp_server/)
   and create a new release.
