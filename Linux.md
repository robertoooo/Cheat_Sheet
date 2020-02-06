# Linux Kommandon
Här kommer jag uppdatera alla kommandon under kursens gång.
Jag har också andra cheat cheets för andra språk om ni vill titta på de.


### Grundläggande kommandon
```bash
ls -l #Flagga som visar detaljerad information om filer och kataloger i en lista, flaggor
ls /etc #Argument som listar kataloger och filer i katalogen /etc istället för din aktuella katalog

cd #Ändrar din nuvarande katalog till hemkatalog (utan argument → hemkatalog ~)
cd / #Ändrar din nuvarande katalog till root med argumentet ”/”
cd .. #Backa en mapp (förälderkatalogen = parent directory)

pwd #Visar din nuvarande katalog (Present Working Directory) 
clear #Rensar terminalen
exit #Stänger av terminalen

echo hej hej hej #Skriver ut ”hej hej hej” som stdout i bashen
cat fil.txt #Skriver ut innehållet av filen fil.txt i stdout

man ls #Visar vad ls gör och vad ls har för flaggor och argument

sudo <kommando> #Kör kommando som root
sudo shutdown #Använd dig av root/superuser för att stänga av systemet

which cat #Skriver ut vart programmet cat är någonstans

```

### Skapa och ta bort kataloger
```bash
mkdir <katalognamn> #Skapar en katalog
rmdir <katalognamn> #Tar bort en katalog
touch <filnamn> #Skapar en fil

rm -rf katalognamn #Tar rekursivt bort katalogen och allt den innehåller

```

### Installera en applikation med packethanteraren RPM (Redhat Package Manager)
```bash
sudo yum check-update #Kolla efter uppdateringar med RPM
yum search <applikation> #Sök efter en applikation i packetförråden
yum info <applikation> #Information om en applikation
yum install <applikation> #Installera en applikation 
```


### Miljövariabler
```bash
echo $PWD
echo $HOME
echo $PATH

printenv #Skriv ut alla miljövariabler

```


### Byta konto och lösenord
```bash
passwed <USER> #Byter lösenord på specificerad användare, utan argument byter på nuvarande användare
su - #Byta användare till root
su - robert #Byta användare till robert

```



### Omdirigering
```bash
echo hej >> testfil #Lägger till en ny rad i testfil
echo hej > testfil #Skriver över testfil
```


### Behörigheter
```bash
chmod u+w testfil #Ger användare skrivbehörighet till filen
chmod u-w testfil #Tar bort användarens skrivbehörighet
chmod g+w testfil #Ger gruppen skrivbehörighet till filen
chmod g+wx testfil #Ger gruppen skriv och körbehörighet till filen
chmod u-rwx, g-x testfil #Användare: ta bort läs+skriv+kör Grupp: Ta bort kör

chmod 777 testfil #-rwxrwxrwx
chmod 755 testfil #-rwxr-xr-x
chmod 700 testfil #-rwx------
```

### Jobba med grupper
```bash
chgrp gruppnamn fil/katalognamn #chgrp kommandot byter grupp på den fil eller katalog du specificerar

sudo groupadd it_stockholm #Lägger till gruppen it_stockholm
sudo groupdel it_stockholm #Tar bort gruppen it_stockholm

usermod -a -G it_stochkolm adminuser #Lägger till gruppen it_stockholm för användaren adminuser
  # -a: Lägg till (append) som sekundär grupp
  # -G: Lägg till som följande grupp (Måste användas med -a)

usermod -g it_stockholm adminuser #Ändrar den primära gruppen till it_stockholm för användaren adminuser
  # Ändrar gruppen på alla filer adminuser har som tillhör den gamla gruppen
```


### Skapa och ta bort användare
```bash
useradd filip #Lägger till användaren filip
userdel filip #Tar bort användaren filip
passwd filip #Lägger till ett lösenord för filip

```

### Visa innehåll på filer
```bash
cat file #Visar innehållet av filen i terminalen
more file #Bläddra igenom en textfil
less file #Bläddra igenom textfil med mer funktioner än more
  # Både less och more är baserade på VI editorn.
  
  
  
head file #Skriver ut början (toppen) av filen
tail file #Skriver ut slutet (botten) av filen
  # tail och less visar 10 rader som standard
  # tail/head -n file #Visar ”n” rader
  # tail -15 file.txt #Visar de 15 sista raderna på file.txt


tail -f file #Följer slutet på en fil som ändras
  # Visar data som skrivs till filen
  # Används för att titta på filer som ändras ofta, ex. Log filer
```

### Information om grupper och användare
```bash
getent group groupname		#Hämtar information från /etc/group
getent passwd username 	#Hämtar information från /etc/passwd


```

### Hitta filer och katalger
```bash
find #Hittar rekursivt filer i sökvägen
 # Om inga argument ges till find, hittar den alla filer i sökvägen (pwd)
 # find kommandot har många olika alternativ/flaggor som kan användas för att reducera djupet på sökningen 

locate #Använder sig av en databas för att hitta filer vilket gör locate mycket snabbare
 # databasen uppdateras en gång om dagen, vilket gör att denna sökning inte alltid är färsk
 # För att uppdatera databasen manuellt: sudo updatedb 


find . -name ”bin”	#Söker efter filen/katalogen bin i din nuvarande sökväg
find . -iname ”Bin”	#Ej skiftlägeskänsligt (case sensetive)  
find . -ls #Kör find med ls -l, listar en detaljerad lista av filer och kataloger som find hittar

find . -type d -exec chmod 775 {} + #Ändrar behörigheter på alla kataloger i sökvägen



```


### Kopiera och flytta filer
```bash
cp source_file destination_file
cp source_file destination_directory
cp -r source_directory destination_directory


mv source destination #Flytta en katalog från source path till destination path
mv /home/it /home/groups/it

```


### Fildiskriptorer (STDIN, STDOUT, STDERR)
```bash
echo hej 1> /dev/pts/x #Skickar hej till terminal x stdout
echo hej 2> /dev/dev/null #Skickar stderr till /dev/null

```

### Söka efter text i en fil (grep)
```bash
grep hej nyfil #Söker efter hej i filen nyfil
◦ -i Ignorerar stor/liten bokstav
◦ -c Räknar förekomsten av dit sök mönster i en fil
◦ -n Skriver ut rad nummer
◦ -v Inverterar sökningen, skriver ut de rader som ej matchar
◦ -w Matchar exakt ditt sökord
```

### Miljövariabler
En miljövariable är en key/value pair
```bash
printenv #Skriver ut alla miljövariabler 
echo $HOME = printenv HOME #Skiruver ut en miljövariable

export TZ = ”Europe/Stockholm” #Exporterar en miljövariabel (bara i din terminal)
unset TZ #Tar bort miljövarabel 
``` 
bashrc är ett shellscript som initieras när du öppnar en ny terminal.
För att lägga till en miljövariable i alla terminaler lägger du till den i ~/.bashrc.
Tänk på att bashrc är personlig och varje användare har en egen bashrc.
```shell
vi ~/.basrc #För att redigera initieringsscriptet för den inloggade användaren
```


### Processer och Jobb kontroll 
```bash
ps -e #Visar alla aktiva processer i ett Linuxsystem med ett generiskt Linuxformat
ps -eH #Visar alla aktiva processer i ett processträd
ps -f #Listar terminalens processer i fullt format
ps -ef #Listar alla aktiva process i fullt format

ps -ef | grep pts #Visar alla processer som innehåller pts, dvs alla aktiva terminaler 


ps -u användarnamn #Visar en användares processer


kill PID #Dödar en process där PID är processID (-9 #Force kill)

```

### Bakgrund och Förgrund processer 
```bash
jobs #Se vilka jobb som befinner sig i bakgrunden
kill %1 #Dödar jobbnummer 1
fg %1 #Lägger jobbnummer 1 i förgrunden
fg #Lägger det senaste jobbet i förgrunden

```


### Insatllera Paket
RPM baserade distros
```bash
yum search inkspace #Söker efter paketet inkspace
yum info inkspace #Visare information om inkspace
yum install inkspace #Installerar inkspace
yum remove inkspace #Avinstallerar inkspace
yum update #För att uppdatera alla dina paket 
rpm -q inkspace #För att kontrollera ifall något är installerat


```
dpkg baserade distros
```bash
apt-get search inkspace #Söker efter paketet inkspace
apt show inkspace or apt-cache inkspace (old) #Visar information om inkspace
apt-get install inkspace #Installerar inkspace
apt-get remove inkspace #Avinstallerar inkspace
apt-get update #För att uppdatera alla dina paket
dpkg -l inkspace #För att kontrollera ifall något är installerat 
```

## Nätverkssäkerhet

### Netcat
```bash
nc -l 1234 #lyssna på port 1234 med nc
nc 127.0.0.1 1234 #koppla upp oss till den porten 
```

### IPtables
```bash
iptables -L #Listar alla filter rules
iptables -A INPUT -p tcp --dport 80 -j ACCEPT #Lägger till på INPUT kedjan, accepterar alla tcp paket på port 80 (HTTP)
iptables -L #Se den nyligen tillagda regeln
iptables -nL #Se port 80 istället för http på den utskrivna regeln
iptables -A INPUT -p tcp --dport 80 -s 10.0.0.0/24 -j ACCEPT #Lägger till INPUT kedjans alla tcp paket som kommer från ip adressen 10.0.0.0/24 på port 80 (HTTP)
iptables -A INPUT -j DROP #Droppar alla paket i slutet av kedjan
iptables -nL --line-numbers #Visa reglerna med nummer
iptables -D INPUT 2 #Tar bort regel nummer 2 på kedjan INPUT
netfilter-persistent save #Spara din konfiguration inför omstart
```

### systemctl
```bash
systemctl reload sshd #Vi startar om ssh daemon
systemctl #Visar aktiva tjänster
systemctl stop SERVICE #Stoppar SERVICE, funkar igen efter omstart
systemctl disable SERVICE #Stänger av SERVICE, startar inte vid omstart
```


### netstat
```bash
netstat -ntp #(Kör som root)
# n: Visar i numeriskt format
# u: Inkluderar udp protokoll
# t: Inkludera tcp protokoll
# l: Visa bara sockets som lyssnar
# p: Visa pid (process ID) och namnet på processen som lyssnar
# 0.0.0.0:68 lyssnar på alla ip adresser

```

### nmap
```bash
nmap x.x.x.x
# Scanna IP adressen för info.
nmap -nL 10.0.0.1/24 #List scan av alla adresser på nätverket
nmap -sn 10.0.0.1/24 #Ping scan av alla adresser på nätverket
nmap -Pn 10.0.0.1/24 #Behandla alla värdar som online, tar lång tid!
# Alla ovanstående kommandon kan också köras på en specifik adress eller mindre antal adresser.

nmap -v -T5 -p 0-65535 -A 10.0.2.4
#A: OS
#T1-5 T1:Långsam T5: Snabb
```

### TCP Wrappers
```bash
/etc/hosts.allow #Allow filen körs först vid försök att ansluta till en TCP
/etc/hosts.deny #Deny filen körs efter Allow och om den matchas nekas åtkomst
```

### netdiscover
```bash
netdiscover -r 192.168.0.0/24
#r: Range
#Söker igenom subnätet 192.168.0.x
```

