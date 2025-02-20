---
title: "Configure"
---

![](/img/windows-files.png)

When you first start the Simple DHCP Server, you can see two files appearing.

- `hosts.csv` is the database of all devices that were known. This is used to
  re-assign the same IP address and remember assignments between starts of the
  program. You can safely delete this if your window becomes too full. You can
  also read this in with a program.

- `simple-dhcp-server-qt.yml` is a configuration file in the YAML format.

- `simple-dhcp-server-tk.conf` is a Python program as confguration file.

Both files are extensively documented.

## Configuration Options

It is safe to delete the configuration file. If the program does not start, it
might be because of mistake in the file. Delete it then. Here are some of the
configuration options.

### Timings

The DHCP server is slower than those already on the network, so it does not
replace them but responds when everybody else had the chance. These are the
timings:

```yaml
dhcp_offer_after_seconds: 10
dhcp_acknowledge_after_seconds: 10
```

### Network

You can change the IP address if you like:

```yaml
network: '192.168.137.0'
subnet_mask: '255.255.255.0'
```

If you have a router for Internet access, configure it like this:

```yaml
router:
- 192.168.137.1
```

Same for the DNS servers. Usually, this is the same as your router from above.
If you like to use a privacy friendly server:

```yaml
domain_name_server:
- 5.9.164.112  # digital courage
```

### More Options

More options are documented in the files respectively. If you use the
`simple-dhcp-server-tk.conf` file, you need to change syntax.

## Command Line

There is a whole chapter on how to [use the Simple DHCP Server from the command
line][1].

[1]: cmd.md
