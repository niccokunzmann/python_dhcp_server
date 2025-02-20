---
title: "Konfigurieren"
---

![](/img/windows-files.png)

Wenn Du den Einfachen DHCP Server zum ersten Mal startest, dann erscheinen zwei
Dateien.

- `hosts.csv` ist die Datenbank aller Geräte, die bekannt sind. Die wird
  benutzt, um sich die IP-Adressen zu merken und wieder zu vergeben, auch wenn
  das Programm wieder geöffnet wird. Du kannst diese Datei gern löschen, z.B.
  wenn das Fenster zu groß wird. Du kannst die Datei auch mit anderen Programmen
  auslesen.

- `simple-dhcp-server-qt.yml` ist die Konfigurationsdatei im YAML-Format.

- `simple-dhcp-server-tk.conf` ist eine Python-Datei zur Konfiguration.

Beide Dateien sind stark dokumentiert.

## Konfigurations-Optionen

Es ist ok, die Konfigurationsdatei zu löschen. Wenn das Programm nicht startet,
dann liegt es vielleicht an einem Fehler in der Datei. Lösche sie dann. Hier
werden nun Konfigurationsmöglichkeiten beschrieben.

### Zeit

Der DHCP-Server ist langsamer als die bereits im Netzwerk, so dass er die
anderen nicht ersetzt, sondern erst reagiert, wenn alle anderen die Chance
hatten. So lange wartet er:

```yaml
dhcp_offer_after_seconds: 10
dhcp_acknowledge_after_seconds: 10
```

### Netzwerk

Du kannst die IP-Adresse verändern, wenn du magst:

```yaml
network: '192.168.137.0'
subnet_mask: '255.255.255.0'
```

Wenn du einen Router mit Internet-Zugang hast, setze ihn so:

```yaml
router:
- 192.168.137.1
```

Das selbe für DNS-Server. Normalerweise kannst du auch den Router von oben
verwenden. Hier ist ein Server für die Privatsphäre:

```yaml
domain_name_server:
- 5.9.164.112  # digital courage
```

### Mehr Optionen

Es gibt noch mehr Optionen, die in der Datei dokumentiert sind. Wenn du
`simple-dhcp-server-tk.conf` benutzt, musst du die Schreibweise anpassen.

## Kommandozeile

Es gibt ein ganzes Kapitel, wie man [den Simple DHCP Server aus der
Kommandozeile verwendet][1].

[1]: cmd.md
