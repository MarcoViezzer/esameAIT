Esame Abilità Informatiche e Telematiche - Viezzer Marco
Appello 02/09/2025

Problemi svolti:
Problemi 1, 2, 5, 6 (Bash)
Problema 9 (Python)

-------------------------------------------------------------------------------------------------
Script problem1.sh

Lo script genera un numero arbitrario di file dummy (impostato a 10) nella cartella corrente; stampa poi a schermo il numero di file presenti nella cartella corrente elencandoli; infine modifica il nome di ogni file, compreso lo stesso script.

-------------------------------------------------------------------------------------------------
Script problem2.sh

Lo script verifica l'esistenza del file /etc/shadow stampando a schermo l'esito della ricerca; in caso positivo, richiede la password dell'utente corrente per aprire con privilegi di superutente il file, mostrandone a schermo il contenuto e veriricandone i permessi di scrittura.

------------------------------------------------------------------------------------------------
Script problem5.sh

Lo script genera il file fileInteri nella cartella corrente per calcolare la somma dei valori contenuti al suo interno e stamparla a schermo.

-------------------------------------------------------------------------------------------------
Script problem6.sh

Lo script genera il file test_file nella cartella corrente per editarne i contenuti.

-------------------------------------------------------------------------------------------------
Script problem9.py

Lo script è stato compilato con NumPy < 2 . L’utilizzo di versioni differenti potrebbe generare errori.  
Lo script legge il file file2_Groups_AGN-wWU_500Mpc_Data.txt e produce in output i grafici richiesti, mostrandoli a schermo ed esportandoli come file .png nella cartella corrente.

Commenti ai grafici:
1) Il grafico "DM mass vs baryonic mass" è generato inizialmente in scala loglog per valorizzare la visualizzazione dei dati. Stime dei parametri ottenute dal fit lineare y=mx+b:  
m = 8.67521583612929  
b = -0.08625291537934315.  
Il fit lineare è stato visualizzato insieme ai dati in un secondo grafico in scala lineare, in quanto l'intercetta negativa fa sì che la retta non sia visualizzabile in scala loglog per valori x<0.02.
2) Il grafico "BH mass vs stellar mass" è generato sia in scala lineare che semilogaritmica con il fit sovrapposto. Stime dei parametri ottenute dal fit lineare y=mx+b:  
m = 0.2807856720440714    
b = -0.00128457411678284.
