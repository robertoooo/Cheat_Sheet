# Linux Basic Commands 


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


```
