# Esame Abilità Informatiche e Telematiche - Marco Viezzer
# Problem 6
# Crea un file a due colonne e ne modifica l'entrata richiesta

#!/bin/bash

touch test_file

# Scrittura file riga per riga
printf "# control of memory requirements\n" > test_file
printf "BoundaryLayerFactor 3.0\n" >> test_file
printf "MaxMem 512\n" >> test_file
printf "MaxMemPerParticle 240\n" >> test_file
printf "PredPeakFactor 0.8\n" >> test_file

# Modifica l'entrata corrispondente a MaxMem
gawk -i inplace '{if ($1=="MaxMem") $2=1024}1' test_file
