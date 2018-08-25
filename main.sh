#!/bin/bash

Name=("Doctor Who" "The Vietnam War" "Game of Thrones" "American Gods" "Vikings" "Star Trek: Discovery" "Blue Planet II" "The Expanse" "Legion" "Black Mirror" "The Punisher" "Fortitude" "Emerald City" "Nova" "The Young Pope" "Will" "A Series of Unfortunate Events" "Sun Records" "The Get Down" "American Crime" "Fargo" "Top of the Lake" "Stranger Things" "Taboo" "The Magicians" "The 100" "13 Reasons Why" "Vice" "The Late Show with Stephen Colbert" "Underground" "Incorporated" "The Handmaid's Tale" "Sherlock" "Pure Genius" "Z: The Beginning of Everything" "This Is Us" "Feud" "Crashing" "Into the Badlands" "Iron Fist" "The Leftovers" "The White Princess" "Brockmire" "Dear White People" "The Last Kingdom" "I Love Dick" "The Keepers" "House of Cards" "Designated Survivor" "The Good Fight" "Better Call Saul" "Silicon Valley" "Jamestown" "Genius" "Riviera" "GLOW" "Preacher" "Cleverman" "Gypsy" "I'm Dying Up Here" "Broken" "The Defiant Ones" "Ozark" "Still Star-Crossed" "Ray Donovan" "Atypical" "Midnight Texas" "The Deuce" "Narcos" "Skyward" "Electric Dreams" "StartUp" "American Horror Story" "Alias Grace" "One Mississippi" "Fear the Walking Dead" "South Park" "Big Little Lies" "Bad Blood" "Curb Your Enthusiasm" "Channel Zero" "Mr. Mercedes" "Mindhunter" "Gunpowder" "Bob's Burgers" "Shameless" "Kingdom" "The Marvelous Mrs. Maisel" "Godless" "Damnation" "Happy!" "The Flash" "Dexter");


for i in "${Name[@]}"
do
   echo "\""$i"\""
   python3 infoExtractorThreaded.py "\""$i"\"" && notify-send "\""$i"\""&

   # do whatever on $i
done
