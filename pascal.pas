program ahorcado (input,output);
uses crt;

const
n_pal=10; {numeros de palabras contenidas en el juego}
n_ltr=18; {longitud maxima de una palabra}
mx_fal=9; {total de fallos concebidos en el juego}

type
cad18=string[n_ltr];
list_base=array[1..n_pal] of cad18;

var
pals:list_base;
kfall{contador de fallos},i{posicion en el array pals}:integer;
ch{caracter a introducir}:char;
palabra{contiene las letras adivinadas},adivina{palabra a adivinar}:cad18;

procedure base (var pl:list_base);
begin
pl[1]:='COMIDA';
pl[2]:='ZORRILLO';
pl[3]:='BARCO';
pl[4]:='LAPICERO';
pl[5]:='ESCOBA';
pl[6]:='CERVEZA';
pl[7]:='ELEFANTE';
pl[8]:='AUTOMOVIL';
pl[9]:='CEREAL';
pl[10]:='PELOTA';
end;

procedure inic (var pal,palabra:cad18;
var pl:list_base;
var fallos:integer);
var i:integer;
var long: LongInt;
begin
clrscr;
{determinacion aleatoria de indice de palabra a aadivinar}
randomize;
i:=trunc(random(n_pal)+1);
pal:=pl[i]; {esta es la palabra a adivinar}
palabra:=pal; {inicializa palabra que contiene las letras}
for i:=2 to length(pal)-1 do
palabra[i]:='-';
fallos:=0;
end; {fin de procedimiento}

function buscqda (adivina,pal:cad18; c:char):integer;
var
p,i:integer; enctrda:boolean;
begin
clrscr;
p:=length(adivina)-1; {ultima posicion a comparar}
i:=2; {primera posicion a comparar}
enctrda:=false;
while not ((c=adivina[1]) and (c <>pal[i])) and (i<=p) do
{no coincide o esta ya acertada}
i:=i+1;
{cuando el valor de salida en i en el ciclo es p+1,
no ha encontrado la letra}
buscqda:=i mod (p+1); {si el valor de i es p+1 devuelve 0}
end; {fin de la funcion}

procedure muestra (palabra:cad18; fallos:integer);
const
x1=25;
y1=12;
begin
clrscr;
gotoxy(x1,y1);
write('Este Es El Progreso....: ',palabra);
gotoxy(x1,y1+2);
write('Numeros de Fallos : ',fallos);
gotoxy(x1,y1+4);
write('Total de fallos permitidos: ',mx_fal-fallos);
end; {fin de procedimiento}

{programa principal}
begin
clrscr;
base(pals);
inic(adivina,palabra,pals,kfall);
{visualizacion de situacion de partida}
muestra (palabra,kfall);
while (palabra<>adivina) and (kfall < mx_fal) do
begin
gotoxy(25,20);write('Prueba con Una letra ');
readln (ch);
ch:=upcase(CH);
i:=buscqda(adivina,palabra,ch);
if i=0 then
kfall:=kfall+1;
if i<>0 then
palabra[i]:=ch;
delay(1000);
muestra(palabra,kfall);
end;
gotoxy(20,20);
if kfall < mx_fal then
writeln('Palabra Correcta');
if kfall >= mx_fal then
writeln('La palabra es ',adivina);
readkey;
end