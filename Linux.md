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


mv source destination

```


```



