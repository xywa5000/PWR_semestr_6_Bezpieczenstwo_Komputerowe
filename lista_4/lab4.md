# Bezpieczeństwo komputerowe - [lab4](sec-lab4.pdf)

## Zadanie 1

1. Opis

    Algorytm Rivesta-Shamira-Adlemana (RSA) – jeden z pierwszych i obecnie najpopularniejszych asymetrycznych algorytmów kryptograficznych z kluczem publicznym, zaprojektowany w 1977 przez Rona Rivesta, Adiego Shamira oraz Leonarda Adlemana. Pierwszy algorytm, który może być stosowany zarówno do szyfrowania, jak i do podpisów cyfrowych. Bezpieczeństwo szyfrowania opiera się na trudności faktoryzacji dużych liczb złożonych.

2. Jak działa?

    Generowanie kluczy RSA jest procesem, który obejmuje kilka kroków matematycznych i kryptograficznych. Oto, jak ten proces wygląda szczegółowo:

    1. Wybór liczb pierwszych
    Na początek wybiera się dwie duże liczby pierwsze, oznaczane jako $ p $ i $ q $. Te liczby powinny być losowo wybrane i mieć podobną wielkość, aby zapewnić bezpieczeństwo klucza.

    2. Obliczenie $ n $
    Mnoży się wybrane liczby pierwsze $ p $ i $ q $, aby uzyskać wartość $ n $:
    $ n = p \cdot q $
    Liczba $ n $ jest częścią zarówno klucza publicznego, jak i prywatnego. Długość klucza RSA jest zwykle określana przez długość $ n $ w bitach (np. 2048-bitowy klucz RSA).

    3. Obliczenie funkcji Eulera $ \phi(n) $
    Funkcja Eulera, oznaczana jako $ \phi(n) $, jest obliczana na podstawie wybranych liczb pierwszych $ p $ i $ q $:
    $ \phi(n) = (p-1) \cdot (q-1) $

    4. Wybór wykładnika publicznego $ e $
    Następnie wybiera się liczbę całkowitą $ e $, która musi spełniać dwa warunki:
        1. $ 1 < e < \phi(n) $
        2. $ e $ musi być względnie pierwsza z $ \phi(n) $ (to znaczy, że największy wspólny dzielnik $ \gcd(e, \phi(n)) = 1 $)
    
        Często wybieranymi wartościami dla $ e $ są 3, 17 lub 65537, ponieważ ułatwiają one obliczenia i mają dobre właściwości kryptograficzne.

    5. Obliczenie wykładnika prywatnego $ d $
    Wykładnik prywatny $ d $ jest obliczany jako multiplikatywna odwrotność $ e$ modulo $ \phi(n) $. Innymi słowy, $ d $ spełnia równanie:
    $ d \cdot e \equiv 1 \ (\text{mod} \ \phi(n)) $
    Można to obliczyć za pomocą rozszerzonego algorytmu Euklidesa.

    6. Konstrukcja kluczy
    Po wykonaniu powyższych kroków, można zbudować klucze:
    - **Klucz publiczny**: składa się z pary $ (e, n) $
    - **Klucz prywatny**: składa się z pary $ (d, n) $

3. Zadanie

    1. Wybieramy $ p $ i $ q $

    2. Generujemy dwie pary kluczy:
        - publicA   $(n, e_a)$
        - privateA  $(n, d_a)$
        - publicB   $(n, e_b)$
        - privateB  $(n, d_b)$

    3. Znając tylko trzy pierwsze chcemy złamać klucz privateB


## Zadanie 2

1. Założono **profil zaufany**

2. Czym jest **podpis zaufany**

    Polski podpis zaufany oparty na profilu zaufanym jest specjalnym rodzajem podpisu elektronicznego, który został stworzony w ramach polskiego systemu identyfikacji elektronicznej. Jest to część tzw. infrastruktury klucza publicznego (PKI), która umożliwia bezpieczne podpisywanie dokumentów cyfrowych oraz autoryzację użytkowników w środowisku internetowym.

    ### Kluczowe cechy polskiego podpisu zaufanego opartego na profilu zaufanym:
    1. **Profil zaufany (ePUAP)**: Podpis ten opiera się na tzw. profilu zaufanym, który jest częścią Elektronicznej Platformy Usług Administracji Publicznej (ePUAP). Profil zaufany to elektroniczna tożsamość użytkownika, która umożliwia korzystanie z wielu usług publicznych online.
    2. **Zgodność z prawem**: Polski podpis zaufany oparty na profilu zaufanym spełnia wymogi prawa polskiego, co oznacza, że ma taką samą ważność prawna jak podpis własnoręczny w wielu sytuacjach.
    3. **Bezpieczeństwo**: Zapewnia wysoki poziom bezpieczeństwa dzięki wykorzystaniu zaawansowanych technologii kryptograficznych oraz uwierzytelnianiu dwuetapowemu.
    4. **Uniwersalność**: Dzięki integracji z ePUAP, polski podpis zaufany umożliwia korzystanie z różnorodnych usług publicznych online, takich jak składanie wniosków, podawanie deklaracji czy kontaktowanie się z urzędami.

    ### Zastosowania polskiego podpisu zaufanego opartego na profilu zaufanym:
    - **Komunikacja z administracją publiczną**: Użytkownicy mogą korzystać z polskiego podpisu zaufanego do załatwiania spraw urzędowych online, np. składając wnioski o dokumenty czy zgłaszając zmiany.
    - **E-commerce**: Podpis ten może być wykorzystywany do zawierania bezpiecznych transakcji online, np. podpisywania umów czy autoryzacji płatności.
    - **Dostęp do usług online**: Umożliwia dostęp do wielu usług online, które wymagają potwierdzenia tożsamości, takich jak bankowość internetowa czy korzystanie z platform edukacyjnych.

    Więcej: https://epodrecznik.mc.gov.pl/mediawiki/index.php?title=Podpis_zaufany

3. Podpisanie wybranego dokumetu

    Wybrane dokumenty to:

    - test_1.txt
    - test_2.pdf

    Możliwe formaty podpisów to:
    
    - XAdES (XML Advanced Electronic Signatures) - standard podpisów elektronicznych oparty na języku XML, dane przechowywane w formacie XML
    - PAdES (PDF Advanced Electronic Signatures) - standard podpisów elektronicznych stworzony specjalnie dla dokumentów w formacie PDF, pozwala on na osadzenie danych dotyczących podpisu w pliku PDF

4. Weryfikacja podpisu

    Do weryfikacji użyto System Automatycznej Weryfikacji Podpisu Elektronicznego (SAWPE) firmy Madkom SA2 (https://weryfikacjapodpisu.pl)

    Po dodaniu pliku de weryfikacji otrzymujemy następujące dane:

    |        Kategoria       |                               Dane                               |
    |:----------------------:|:-----------------------------------------------------------------:|
    |      Integralność      | Zachowana - podpisane dane nie zostały zmodyfikowane od czasu ich elektronicznego uwierzytelnienia |
    |       Podpisujący      |                           *IMIĘ i NAZWISKO*                      |
    | Rodzaj uwierzytelnienia| Podpis zaufany (Minister do spraw informatyzacji - pieczęć podpisu zaufanego) |
    |Deklarowany czas złożenia podpisu | 2024-05-21T02:19:33.071+02:00                                         |

    Poniżej znajdziemy:
    
    - Dane personalne osoby, która użyła swojego profilu zaufanego, aby złożyć podpis: (id konta, imię, nazwisko, pesel)

    - Certyfikat podpisującego oraz informację, że Certyfikat nie znajduje się na liście CRL

    |          Kategoria         |                                     Dane                                     |
    |:--------------------------:|:----------------------------------------------------------------------------:|
    |      Nazwa powszechna      |                      Minister do spraw informatyzacji - pieczęć podpisu zaufanego                      |
    |         Organizacja        |                              Ministerstwo Cyfryzacji                             |
    |             Kraj           |                                       PL                                       |
    | Numer seryjny certyfikatu |                           20892124217292921814138920212746575688618877                           |
    |       Wystawiony przez     |                               Centrum Kwalifikowane EuroCert                               |

    - Cała ścieżka certyfikacji wygląda następująco:
    
        Nazwa powszechna: **Narodowe Centrum Certyfikacji**
        Organizacja: Narodowy Bank Polski
        Kraj: PL
        Numer seryjny certyfikatu: 370927558070677912140887258838452155756220254790
        Wystawiony przez: Narodowe Centrum Certyfikacji

        Nazwa powszechna: **Centrum Kwalifikowane EuroCert**
        Organizacja: EuroCert Sp. z o.o.
        Kraj: PL
        Numer seryjny certyfikatu: 150378514884649544203033409041720775548471354512
        Wystawiony przez: Narodowe Centrum Certyfikacji

        Nazwa powszechna: **Minister do spraw informatyzacji - pieczęć podpisu zaufanego**
        Organizacja: Ministerstwo Cyfryzacji
        Kraj: PL
        Numer seryjny certyfikatu: 20892124217292921814138920212746575688618877
        Wystawiony przez: Centrum Kwalifikowane EuroCert

    - Lista unieważnionych certyfikatów (lista CRL, ang. Certificate Revocation List) – lista certyfikatów unieważnionych przez organ certyfikujący z różnych powodów. Publikowana jest przez wystawcę certyfikatów (CA). Zawiera numery seryjne certyfikatów, które zostały unieważnione np. na skutek ujawnienia klucza prywatnego.  
    ~wikipedia

5. Zmiana dokumentu po podpisaniu

    Zmieniono losowo jeden znak w podpisanym pliku i poddano ponownej weryfikacji.

    |        Kategoria       |                          Dane                               |
    |:----------------------:|:-----------------------------------------------------------------:|
    |      Integralność      | Niezachowana - podpisane dane prawdopodobnie zostały zmodyfikowane po ich uwierzytelnieniu elektronicznym |
    |       Podpisujący      |                           *IMIĘ i NAZWISKO*                      |
    | Rodzaj uwierzytelnienia| Podpis zaufany (Minister do spraw informatyzacji - pieczęć podpisu zaufanego) |
    |Deklarowany czas złożenia podpisu | 2024-05-21T02:19:33.071+02:00                                         |

    Wnioski: zgodnie z oczekiwaniami podpis zaufany chroni przed niepowołoną zmianą treści dokumentu.

6. Certyfikat niezaufany

    Informacje ogólne otrzymane po zweryfikowaniu dokumentu, otrzymanego od prowadzącej zajęcia, są takie same jak w przypadku dokumentów testowych z punktów 2.-5. Jednak wystawca certyfikatu niezaufany (certyfikat nie znajduje się na liście TSL). Dodatkowo ścieżka certyfikacji jest też inna: pl.ID Root CA > pl.ID Authorization CA MSWiA > *IMIĘ i NAZWISKO*.

7. Podpis zaufany, a osobisty i kwalifikowany

    W przypadku e-dowodu i e-PUAP, podpis zaufany jest najczęściej wykorzystywanym rodzajem podpisu elektronicznego, podczas gdy podpis osobisty i kwalifikowany dostępne są dla użytkowników, którzy chcą skorzystać z bardziej zaawansowanych usług wymagających wysokiego poziomu uwierzytelnienia.

    Więcej: https://www.ur.edu.pl/files/ur/import/private/87/Akty-prawne/Mini-poradnik-Podpis-osobisty-zaufany-i-kwalifikowany-podpis-elektroniczny.pdf
