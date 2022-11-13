
# 💩PoopiLang 💩
De taal Poopilang lijkt op een kindje van C++ en Python, maar dan met een vies tintje.
Je hoeft niet perse variablen te declareren zoals in C++ wel nodig is. Maar het mag wel. 💩
It's somewhat... a shitshow.

## 💩Gebruiken💩
bij het runnen van main, voert het programma een basis uit, geef je als parameter "function" mee, dan voert hij het function bestand uit.
 ```
python main.py [bestand om te runnen]
```

## 💩Testen 💩
De ingebouwde unittests zijn te runnen via VSCode's test sectie of doormiddel van een command prompt.
```
python Tester.py
```
### Unit Testing
Deze zitten verwerkt in de class "TEST_DATATYPES" in de Tester.py
Deze tests zijn belangrijk om te kijken of de datatypes van de Poopilang daadwerkelijk overeenkomen met de datatypes die de gebruiker invoert.
Als je namelijk een float krijgt in plaats van een integer, dan kan je programma bijzondere 'arithmetics' uitvoeren, die je niet verwacht.
Zo heb ik hier getest of datatypes kloppen, of Pi in een float kan & wat de waarde van een string is in Poopilang. Deze lijken allemaal goed te werken.
De test_node functie, loopt ook nog eens alle nodes na en checkt of de types, names en return types ook allemaal kloppen met wat de gebruiker verwacht.
### Integration Testing
de integratie testen zijn terug te vinden in vrijwel alle tests.
doormiddel van de Lexer, Parser en Interpreter te combinberen krijg je 'real time' output van Poopilang.
Als 1 van deze 3 modules niet naar behoren zou werken, dan zouden de outputs niet overeenkomen met de python code die is geschreven.
Ik heb in de reader gekeken voor vorig jaar, waarin een aantal functies staan die zouden moeten werken in je eigen taal.
En die heb ik dan ook in mijn eigen taal gemaakt, en in python.
Door beide functies dezelfde parameter te geven, en te vergelijken of deze gelijk zijn, kan je concluderen dat Poopilang de gewenste output geeft in verschillende test cases.
Om dit een beetje op te spicen, is er een random module gebruikt, die meermaals een random getal in beide functies gooit. Dit blijkt goed te werken.
### Motivatie
Ik heb gebruik gemaakt van verschillende tests zoals hierboven te lezen is en te zien is in de code.
De Parser, Lexer en Interpreter zijn allemaal los getest, en de combinatie van deze 3 is ook getest.
Denk hierbij aan de het parsen van de code, het lexen van de code en het interpreteren van de parser en lexer.
Dus kloppen alle Tokens wel met de code? Klopt de volgorde van de tokens, en krijgt de gebruiker de gewenste output van de code?
Dit zijn belangrijke tests om te doen, want als de taal niet werkt, dan gaat ook niemand dit gebruiken. (of wel?)

De garanties die dus op de code kunnen worden gegeven zijn dat de taal werkt met in ieder geval basis rekenkundigheid, recursieve functies, loopjes, prints  en dat de taal de gewenste output geeft.
De tests geven ook de verwachte uitkomst op een dynamische wijzen, als "tester" kan je zelf de input van de test wijzigen, en dan hoef je de test zelf niet meer aan te passen.
Ook zijn er door deze tests nog enkele fouten gevonden in de code, en die zijn tijdens het testen opgelost.

Deze test laten zien dat de code naar behoren werkt, en dat de output van Poopilang overeenkomt met de output van "normale" python code.
Ik ben zeer tevreden met het resultaat van PoopiLang.

## Benodigdheden van Poopilang voor ATP 💩
### 💩 Turing Complete 💩
Poopilang is turing compleet.
* Het is mogelijk te branchen.
* Het is mogelijk om loop functies te gebruiken (While of Recursief)
* Het is mogelijk een 💩 ton aan variablen te maken, zolang het geheugen van de host het aankan.
### 💩 Functioneel 💩
Het volledige project is functioneel geschreven. 
De Lexer, Parser en Interpreter zijn dan ook individuele componenten zonder eigen kennis van het programma wat het moet draaien.
### 💩 Classes 💩 
Alle Nodes zijn van de class Node maar gebruiken ook elkaar. 
De functies `__repr__()` en `run()` moeten worden geimplementeerd door alle child nodes.
Vervolgens zijn deze te runnen door de interpreter.
### 💩 Decorators💩
Een decorator is geschreven in het bestand "Declarations", voor de debugging van Nodes.
`@DEBUG_DECORATOR` boven de functie plaatsen is voldoende om de decorator op te pakken & de uit te voeren nodes te visualiseren voor de eindgebruiker.
### 💩Hogere Ordefuncties💩
Ik heb gebruiker gemaakt van hogere orderfuncties, deze worden gebruikt in de "Declarations".
 `zip()` en `map()` zijn gebruikt om functies aan te roepen van parameters en/of nodes van functie bodies.

## 💩Functies van Poopilang 💩
### 💩Variabelen💩
Variabelen kunnen gedeclareerd, gedefiniëerd, ge-assigned en gecalled worden. De werking hiervan lijkt op die van C++.
```
💩💩 myOwnPoopiVariable 💩💩💩💩💩💩💩💩💩💩💩 42 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
```
staat gelijk aan:
``` c++
int myOwnPoopiVariable = 42;
```
### 💩Functies💩
Functies kunnen gedeclareerd, gedefiniëerd en gecalled worden. De werking hiervan lijkt op dit van C++.  Functies zonder return voeren hun body uit en returnen `None`.
```
💩💩 doubleme 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩 input 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
    💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 input 💩💩💩💩💩💩💩💩💩 2 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
```
staat gelijk aan:
``` c++
int doubleme(int input) 
{
    return input * 2;
}
```
### 💩Wiskunde💩
Er kunnen verschillende wiskundige operaties worden uitgevoerd op variabelen maar ook op losse getallen.
```
💩💩 x 💩💩💩💩💩💩💩💩💩💩💩 10 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩"
💩💩 y 💩💩💩💩💩💩💩💩💩💩💩 20 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩"
💩💩 myOutput 💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩 y 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩"
```
staat gelijk aan:
``` c++
int x = 10;
int y = 20;
int myOutput = x + y;
```

### 💩Logica💩
Logische operaties kunnen worden uitgevoerd. Een logische operatie geeft `True` of `False` terug.
``` 
AND
💩 trueOrFalse 💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩" 

OR
💩 trueOrFalse 💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩" 
```
staat gelijk aan:
``` c++
bool trueOrFalse = true && false; //False
bool trueOrFalse = true || false; //True
```
### 💩Conditions 💩
Een if statement kan worden gemaakt.
```
💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩💩💩💩💩💩💩💩 0 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
    💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
        💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
    💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
```
staat gelijk aan:
``` c++
if(x > 0)
{
    cout << x << endl;
}
```
### 💩Loopjes💩
Alleen een `while` statement kan gemaakt worden.
```
💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 
💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
    n 💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
```
staat gelijk aan:
``` c++
while(n > 1)
{
    n = n - 1;
}
```
### 💩Printen💩
Dit kunnen variabelen zijn maar ook functiecalls en stukjes logica. 
Een lege regel printen is ook mogelijk, je hoeft er dus niet per se iets op te zetten.
```
💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
```
staat gelijk aan:
``` c++
cout << x << endl;
```
