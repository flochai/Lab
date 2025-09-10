#! /bin/bash

while true
do
        echo "1. Add"
        echo "2. Substract"
        echo "3. Multiply"
        echo "4. Divide"
        echo "5. Quit"

        read -p "Enter the number of the operation you wish to do: " choice

        if [ $choice -eq 1 ]
        then
          read -p "Enter number 1: " number1
          read -p "Enter number 2: " number2
          echo Answer=$(( number1 + number2 ))
        elif [ $choice -eq 2 ]
        then
          read -p "Enter number 1: " number1
          read -p "Enter number 2: " number2
          echo Answer=$(( number1 - number2 ))
        elif [ $choice -eq 3 ]
        then
          read -p "Enter number 1: " number1
          read -p "Enter number 2: " number2
          echo Answer=$(( number1 * number2 ))
        elif [ $choice -eq 4 ]
        then
          read -p "Enter number 1: " number1
          read -p "Enter number 2: " number2
          echo Answer=$(( number1 / number2 ))
        elif [ $choice -eq 5 ]
        then
          echo See you soon!
          break
        fi
done
