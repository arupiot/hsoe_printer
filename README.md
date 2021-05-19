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

```
sudo cupsctl --remote-any
sudo /etc/init.d/cups restart
```

## Detect printer address

```
# lpinfo -v
network beh
file cups-brf:/
network ipp
network http
network https
network lpd
network socket
network ipps
direct usb://EPSON/TM-T20II?serial=544338460119060000
network socket://192.168.1.10
```

### Native Epson Driver
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


```
    3  sudo nano /etc/cups/cupsd.conf
    4  sudo nano /etc/cups/cupsd.conf
    5  sudo service cups restart
   10  cp tmt-cups-1.4.1.0.tgz /opt/
   14  mv tmt-cups-1.4.1.0.tgz printer/
   17  tar zxvf tmt-cups-1.4.1.0.tgz
   18  cd tmt-cups
   37  ls /usr/share/cups/model/
   38  ls /usr/share/cups/
   41  cp ppd/tm-t20ii-rastertotmt.ppd /usr/share/cups/model/
   42  ls /usr/share/cups/model/
   43  /etc/init.d/cups restart
   55  cupsenable
   56  cupsenable -h
   57  man cupsenable
   58  cupsenable tmt
   69  sudo apt-get install libcups2-dev libcupsimage2-dev g++ cups cups-client
   73  git clone https://github.com/nemik/epson-tm-t20-cups.git
   74  cd epson-tm-t20-cups/
   77  sudo apt-get install libcups2-dev libcupsimage2-dev g++ cups cups-client
   78  sudo apt-get install libcups2-dev libcupsimage2-dev g++ cups cups-client --fix-missing
   81  sudo apt-get install libcups2-dev libcupsimage2-dev g++ cups cups-client --fix-missing
   85  git clone https://github.com/plinth666/epsonsimplecups.git
   86  cd epsonsimplecups/
  127  cd epsonsimplecups/
  130  service cups restart
  131  service cups status
  132  service cups stop
  133  service cups status
  134  service cups start
  135  service cups status
  138  mv /home/pi/tmx-cups-src-ThermalReceipt-3.0.0.0.tgz ./
  139  tar zxvf tmx-cups-src-ThermalReceipt-3.0.0.0.tgz
  148  ls /usr/share/cups/model/
  152  lpadmin -p tmt2 -i /usr/share/cups/model/tm-t20ii-rastertotmt.ppd -v usb://EPSON/TM-T20III?serial=583741560358950000
  153  cupsenable tmt2
  155  service cups status
  156  cat /var/log/cups/error_log
  157  lpadmin -p tmt2 -i /usr/share/cups/model/epson/EpsonTMT20Simple.ppd.gz -v usb://EPSON/TM-T20III?serial=583741560358950000
  158  lpadmin -p tmt3 -i /usr/share/cups/model/epson/EpsonTMT20Simple.ppd.gz -v usb://EPSON/TM-T20III?serial=583741560358950000
  159  cupsenable tmt3
  166  cd epson-tm-t20-cups/
  180  ls /usr/share/cups/model/
  181  ls /usr/share/cups/model/zjiang/
  182  lpadmin -p tmt4 -i /usr/share/cups/model/zjiang/ZJ-58.ppd -v usb://EPSON/TM-T20III?serial=583741560358950000
  183  cupsenable tmt4
  192  lpadmin -u allow:all -p tmt -i /usr/share/cups/model/epson/EpsonTMT20Simple.ppd.gz -v usb://EPSON/TM-T20III?serial=583741560358950000
  193  cupsenable tmt
  194  cupsaccept tmt
```
