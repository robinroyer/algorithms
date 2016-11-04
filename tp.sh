#!/bin/bash

# Utilisation
#
# tp.sh -a [vorace|progdyn|tabou] -e [path_vers_exemplaire] [-t] [-p]
#
# Arguments optionnels :
#
# -p Imprime les blocs triés.
# -t Imprime le temps d’exécution.

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a|--algo)
    ALGO="$2"
    shift
    ;;
    -e|--ex_path)
    EX_PATH="$2"
    shift
    ;;
    -p|--print|-t|--time)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        echo "Usage du script:"
        echo "tp.sh -a [vorace|progdyn|tabou] -e [path_vers_exemplaire] [-t] [-p]"
        exit
    ;;
esac
shift
done

python3 ./src/data_analysis/$ALGO.py $EX_PATH $OPTIONS
