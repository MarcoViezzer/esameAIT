Esame Abilità Informatiche e Telematiche - Viezzer Marco
Appello 02/09/2025

Problemi svolti:
Problemi 1, 2, 5, 6 (Bash)
Problema 9 (Python)

-------------------------------------------------------------------------------------------------
Script problem1.sh

Lo script genera un numero arbitrario di file dummy (impostato a 10) nella cartella corrente, modificando poi il nome di ogni file presente all'interno della cartella, compreso lo stesso script.

-------------------------------------------------------------------------------------------------
Script problem2.sh

Lo script richiede la password dell'utente corrente per aprire con privilegi di superutente il file /etc/shadow se questo esiste, mostrandone a schermo il contenuto e veriricandone i permessi di scrittura.

------------------------------------------------------------------------------------------------
Script problem5.sh

Lo script genera il file fileInteri nella cartella corrente per sommare i valori contenuti al suo interno.

-------------------------------------------------------------------------------------------------
Script problem6.sh

Lo script genera il file test_file nella cartella corrente per editarne i contenuti.

-------------------------------------------------------------------------------------------------
Script problem9.py

Lo script legge il file file2_Groups_AGN-wWU_500Mpc_Data.txt e produce in output i grafici richiesti, mostrandoli a schermo ed esportandoli come file .png nella cartella corrente.

Commenti ai grafici:
1) Il grafico "DM mass vs baryonic mass" è generato inizialmente in scala loglog per valorizzare la visualizzazione dei dati. Valori ottenuti dal fit lineare:
  m = 8.67521583612929
  b = -0.08625291537934315
Il fit lineare è stato visualizzato insieme ai dati in un secondo grafico in scala lineare; l'intercetta negativa fa sì che la retta non sia visualizzabile in scala loglog per valori x<0.02.
2) Il grafico "BH mass vs stellar mass" è generato sia in scala lineare che semilogaritmica con il fit sovrapposto. Valori ottenuti dal fit lineare:
   m = 0.2807856720440714
   b = -0.00128457411678284
