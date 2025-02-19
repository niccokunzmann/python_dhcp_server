+++
title = "Development"
type = "chapter"
weight = 1
+++

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
