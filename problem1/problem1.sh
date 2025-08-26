# Esame Abilità Informatiche e Telematiche - Marco Viezzer
# Problem 1
# Lista file nella working directory e ne modifica il nome anteponendo la data odierna

#!/bin/bash

# Crea n dummy files

n=10
for ((i=1; i<=n; i++)); do
    touch dummy${i}
done

# Lista file regolari che si trovano nella working directory, salvandoli in fileArray e stampandoli

fileArray=()
for f in *; do
    [[ -f "$f" ]] && fileArray+=("$f")
done

if [[ ${#fileArray[@]} != 0 ]]
then
    echo -e "Numero file presenti nella working directory attuale: ${#fileArray[@]}"
    echo -e  "Elenco file:\n${fileArray[@]}"
else
    echo Nessun file trovato nella cartella corrente.
fi

# Rinomina file inserendo all'inizio la data odierna in formato YYYY-MM-DD

 for f in *; do
     [[ -f "$f" ]] && mv "$f" "$(date +%Y-%m-%d)-$f"
 done
