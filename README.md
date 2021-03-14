# hsoe_printer
Printer application for the High Street of Exchanges room at the Venice Biennale 2021

## Epson TM-T20II driver

```
sudo apt-get install libcups2-dev libcupsimage2-dev g++ cups cups-client

```

```
https://download.epson-biz.com/modules/pos/index.php?page=single_soft&cid=6408&pcat=3&pid=6146
```

```
https://github.com/plinth666/epsonsimplecups
```

```
https://github.com/nemik/epson-tm-t20-cups
```

## Cups administration

[Command line administration programs](https://www.cups.org/doc/admin.html)


[Command line options](https://www.cups.org/doc/options.html)

### Native Epson Deiver
```
lpadmin -u allow:all -p tmt -i /usr/share/cups/model/epson/EpsonTMT20Simple.ppd.gz -v usb://EPSON/TM-T20III?serial=583741560358950000
```

```
cupsenable tmt
```

```
cupsaccept tmt
```

```
lpadmin -d tmt
```


### Alternative driver
```
lpadmin -p tmt -i /usr/share/cups/model/tm-t20ii-rastertotmt.ppd -v usb://EPSON/TM-T20III?serial=583741560358950000
```


