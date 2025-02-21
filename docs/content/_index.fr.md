---
type: "home"
---

Serveur DHCP entièrement en Python ne nécessitant aucune bibliothèque ou
installation supplémentaire autre que Python 3.

![](/img/windows-tk.png)

- [Installation][2]
- [Contribuer][1]
- [Voir la source][3]

## Compatibilité

It was testet under Ubuntu 14 and later with Python and Windows 7 and later. It
does not use any operating system specific Python functions, so it should work
when Python 3 works.

## Fonctionnalités

This DHCP server program will assign IP addresses ten seconds later than
requested. So, it can be used in networks that already have a DHCP server
running.

Ce serveur DHCP simple

- affiche les clients dans le réseau
- liste l'adresse IP, l'adresse MAC et le nom d'hôte
- highlights recently refreshed/added clients
- assigns IP addresses 10 seconds later than usual DHCP servers
- se rappelle des adresses dans le fichier `hosts.csv`
- peut être configuré pour servir toutes les options DHCP en utilisant
  Python/Yaml

[Les contributions sont les bienvenues !][1]

## Projets connexes

Ce programme a été créé pour rechercher des Raspberry Pis dans le réseau.

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder)
- [Angry IP](https://angryip.org/)

[1]: contribute
[2]: install
[3]: https://github.com/niccokunzmann/simple_dhcp_server/
