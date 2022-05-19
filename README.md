# Language-identification
Language identification

Program rozpoznávání jazyků

 1. Anotace: 
Program má zjistit, v jakém z 8 jazyků je napsán text.

 2. Přesné zadání:
Pomocí statistiky (frekvencí výskytu písmen v různých jazycích) program analyzuje text a vrací jazyk, kterým je napsán.

 3. Zvolený algoritmus:
Program počítá, kolikrát se vyskytuje každé písmeno v textu, násobí počet písmen jeho průměrnou frekvencí pro daný jazyk (z Wikipedie) a to celé logaritmuje. Tuto operaci provádíme pro každé písmeno a pro každý jazyk, tím dostáváme skóre každého jazyka. Pak počítáme sumu skóre každého jazyka a ten jazyk, který má nejvyšší výsledek je jazyk textu.

 4. Diskuse výběru algoritmu:
Jiný algoritmus odečítal pravděpodobnost výskytu v tabulce od pravděpodobnosti počtu písmen v textu, nachází tedy odchylku, to se provádí pro každý jazyk a každé písmeno. Pak se počítá suma kvadratických odchylek (eliminace záporných hodnot), nejmenší výsledek je jazyk textu.

 5. Program:
Složka obsahuje soubor FrequencyLetters.txt, ve kterém je tabulka frekvencí, soubor „Text U Ktereho Chceme Zjistit Jazyk.txt“, v němž je zadaný text, a samotný program main.py. Program obsahuje funkci JakyJeJazykTextu, která vrací jako výsledek jazyk textu, obsahuje matici z tabulky frekvencí a seznam všech možných písmen. 

 6. Reprezentace vstupních dat a jejich příprava:
Jako vstup program dostává odkaz na soubor, ve kterém se nachází text. Aby program správně zjistil jazyk textu, musí být text napsán správně s diakritikou a měl by jen v minimálním množství obsahovat cizí slova. Text musí být dlouhý aspoň 400 znaků.Text musí být napsán v jednom z 8 jazyku: angličtina, španělština, turečtina, švédština, polština, dánština, islandština, čeština.

 7. Reprezentace výstupních dat a jejich interpretace:
Jako výsledek program vrací jazyk, ve kterém text je napsán.

 8. Testy: <br>
Test1.txt - English <br>
Test2.txt - Polish <br>
Test3.txt - Spanish <br>
Test4.txt - Czech <br>
Test5.txt - Icelandic <br>
