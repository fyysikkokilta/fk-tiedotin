#!/bin/bash

week=$(date +%U)
year=$(date +%Y)
#((week++))
week=$(LC_NUMERIC="en_US.UTF-8" printf "%.2d" $((week)))
echo "The week number is $week."

scp mails/kilta-tiedottaa-viikko-${week}.html fk@otax.fi:~/www/wp-content/uploads/viikkotiedote/${year} &&
scp data/week${week}.json fk@otax.fi:~/www/wp-content/uploads/viikkotiedote-data/${year} &&
scp data/week${week}-en.json fk@otax.fi:~/www/wp-content/uploads/viikkotiedote-data/${year}

echo "Success!"
