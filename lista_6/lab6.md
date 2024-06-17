# Bezpieczeństwo komputerowe - [lab6](sec-lab6.pdf)

## Zadanie 1.

1. Pobieranie certyfikatu

    Zadanie wykonane na przykładzie: https://pwr.edu.pl/. Wybrana opcja exportu do pliku, to pełna ścieżka (certyfikaty pośrednie oraz główny).

    Alternatywnie certyfikaty można pobrać poleceniem:
    ```
    openssl s_client -connect pwr.edu.pl:443 -showcerts
    ```

    Nazwa pliku dla dalszych poleceń: _.pwr.edu.crt

2. openssl x509

    Jaka organizacja (issuer) wydała i podpisała certyfikat:

    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -issuer
    issuer=C = NL, O = GEANT Vereniging, CN = GEANT OV RSA CA 4
    ```

    Algorytm użyty do podpisania certyfikatu, co wpływa na jego bezpieczeństwo:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -text | grep "Signature Algo
    rithm"
        Signature Algorithm: sha384WithRSAEncryption
        Signature Algorithm: sha384WithRSAEncryption
    ```

    Okres ważności certyfikatu, czyli daty, od kiedy do kiedy certyfikat jest ważny:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -dates
    notBefore=Feb 18 00:00:00 2024 GMT
    notAfter=Feb 17 23:59:59 2025 GMT
    ```

    Podmiot (subject), dla którego został wydany certyfikat, czyli np. nazwę domeny:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -subject
    subject=C = PL, ST = Dolno\C5\9Bl\C4\85skie, O = Politechnika Wroc\C5\82awska, CN = *.pwr.edu.pl
    ```

    Dodatkowe nazwy domen (SANs), które są również objęte certyfikatem:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -text | grep -A 1 "Subject Alternative Name"
        X509v3 Subject Alternative Name:
        DNS:*.pwr.edu.pl, DNS:pwr.edu.pl
    ```

    Różne rozszerzenia X509 obecne w certyfikacie, które zawierają dodatkowe informacje o certyfikacie:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -text | grep -A 10 "X509v3 extensions"
            X509v3 extensions:
                X509v3 Authority Key Identifier:
                    6F:1D:35:49:10:6C:32:FA:59:A0:9E:BC:8A:E8:1F:95:BE:71:7A:0C
                X509v3 Subject Key Identifier:
                    40:39:A6:1D:52:C6:67:81:14:06:84:5A:5D:83:48:C5:FF:4E:C4:60
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
                X509v3 Basic Constraints: critical
                    CA:FALSE
                X509v3 Extended Key Usage:
                    TLS Web Server Authentication, TLS Web Client Authentication
    ```

    URI do listy unieważnionych certyfikatów (CRL), gdzie można sprawdzić, czy certyfikat został unieważniony:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -text | grep -A 4 "CRL Distribution Points"
                X509v3 CRL Distribution Points:
                    Full Name:
                    URI:http://GEANT.crl.sectigo.com/GEANTOVRSACA4.crl
                Authority Information Access:
                    CA Issuers - URI:http://GEANT.crt.sectigo.com/GEANTOVRSACA4.crt
    ```

    URI do serwisu OCSP, który umożliwia sprawdzenie statusu certyfikatu w czasie rzeczywistym:
    ```
    $ openssl x509 -in _.pwr.edu.crt -noout -text | grep -A 4 "Authority Information Access"
                Authority Information Access:
                    CA Issuers - URI:http://GEANT.crt.sectigo.com/GEANTOVRSACA4.crt
                    OCSP - URI:http://GEANT.ocsp.sectigo.com
                X509v3 Subject Alternative Name:
                    DNS:*.pwr.edu.pl, DNS:pwr.edu.pl
    ```

3. openssl verify

    Pobrano certyfikaty pojedynczo (bez pełnej ściezki certyfikacji):
    ```
    USERTrust_RSA_Certification_Authority.crt
    +---GEANT_OV_RSA_CA_4.crt
        +---pwr.edu.pl.crt
    ```

    Weryfikacja czy istnieje zaufana ścieżka:
    ```
    $ openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt -untrusted GEANT_OV_RSA_CA_4.crt -untrusted pwr.edu.pl.crt USERTrust_RSA_Certification_Authority.crt
    USERTrust_RSA_Certification_Authority.crt: OK
    ```

4. openssl ocsp

    ```
    $ openssl ocsp -issuer GEANT_OV_RSA_CA_4.crt -cert pwr.edu.pl.crt -url http://GEANT.ocsp.sectigo.com
    WARNING: no nonce in response
    Response verify OK
    pwr.edu.pl.crt: good
        This Update: Jun 14 21:01:26 2024 GMT
        Next Update: Jun 21 21:01:25 2024 GMT
    ```

    ```
    $ openssl ocsp -issuer USERTrust_RSA_Certification_Authority.crt -cert GEANT_OV_RSA_CA_4.crt -url http://GEANT.ocsp.sectigo.com
    WARNING: no nonce in response
    Response verify OK
    GEANT_OV_RSA_CA_4.crt: good
        This Update: Jun 16 16:37:30 2024 GMT
        Next Update: Jun 23 16:37:29 2024 GMT
    ```

    "WARNING: no nonce in response" to ostrzeżenie dotyczy braku wartości nonce w odpowiedzi OCSP. Nonce jest opcjonalnym polem w żądaniu OCSP, które służy do zapewnienia unikalności odpowiedzi OCSP. Brak nonce nie jest zazwyczaj problemem, ale niektóre aplikacje lub zasady mogą wymagać jego obecności dla celów bezpieczeństwa.

5. verify vs ocsp

    Główna różnica między **openssl verify** a **openssl ocsp** polega na tym, że pierwsze narzędzie sprawdza poprawność certyfikatu w oparciu o lokalne dane i łańcuchy certyfikacji, podczas gdy drugie komunikuje się z serwerem OCSP, aby uzyskać aktualny status certyfikatu zgodnie z protokołem OCSP.

## Zadanie 2.

Na raize pominiętę ze względów technicznych.

## Zadanie 3.


