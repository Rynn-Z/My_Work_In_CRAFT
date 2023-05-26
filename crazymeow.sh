#!/bin/bash

 set -e

 DEST=/root/test

 mkdir -p $DEST

 for meow in $(ls . | grep -E "^[0-9]{3}"); do
     echo "Deleting $meow/run"
     rm -rf $meow/run
     mkdir $meow/run
 done
