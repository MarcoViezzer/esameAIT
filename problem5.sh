# Esame Abilità Informatiche e Telematiche - Marco Viezzer
# Problem 5
# Crea un file con colonna di interi e ne calcola la somma

#!/bin/bash

touch fileInteri

# Scrivi colonna di primi 10 interi su fileInteri
for ((i=1; i<=10; i++)); do echo -e "$i"; done > fileInteri

# Somma riga per riga la prima colonna di fileInteri
gawk 'BEGIN {sum=0} {sum+=$1} END {print sum}' fileInteri

