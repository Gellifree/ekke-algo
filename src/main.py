#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import sys

from analyzer.menu import MenuDrawer

def first():
    print('first func called')

def second():
    print('second func called')

def main():
    answer = 0
    while(answer != -1):
        main_menu = ['test element', 'another test element', 'Kilépés']
        func_list = [first, second]
        os.system("cls")
        print("2024 Kovács Norbert - Algoritmusok és adatszerkezetek beadandó\n")
        answer = MenuDrawer.draw(main_menu)

        if(answer == -2 or answer == -3):
            input("Kérlek nyomj entert a folytatáshoz.")
        elif(answer != -1):
            print(" >> " + main_menu[answer] + " <<\n")
            func_list[answer]()
            input(" >> done <<")
        else:
            input("Az alkalmazás most kilép.")
            os.system("cls")

if __name__ == "__main__":
	main()