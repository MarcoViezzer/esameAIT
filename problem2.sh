# Esame Abilità Informatiche e Telematiche - Marco Viezzer
# Problem 2
# Verifica l'esistenza del file /etc/shadow e in caso affermativo ne mostra i contenuti; verifica se si detiene il permesso di editarlo.

#!/bin/bash

filePath="/etc/shadow"

if [[ -f "$filePath" ]]; then
    echo "Shadow passwords are enabled"
    # Se esiste, apri file /etc/shadow come super utente
    sudo cat $filePath
else
    echo "File doesn't exist"
    exit 1
fi

# Verifica permesso di scrittura
if [[ -w  "$filePath" ]]; then
    echo "You have permission to edit ${filePath}"
else
    echo "You do NOT have permissions to edit ${filePath}"
    exit 2
fi
