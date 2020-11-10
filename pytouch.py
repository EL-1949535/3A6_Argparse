#!/usr/bin/env python3

"""
Commande 'touch' en python

Par Éthan Leduc
"""

import sys
import argparse
import os
import colorama
from colorama import Fore
colorama.init()


def parse_args() -> argparse.Namespace:
    """Parse les arguments entrés nécéssaire au fonctionnement du script"""
    parser = argparse.ArgumentParser(
        description=f"{Fore.YELLOW}Commande pour créer des fichiers -- ©2020, par Éthan Leduc")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='Ne pas notifier si existe déjà')
    group.add_argument('-v', '--verbeux', action='store_true', help='Notifier les créations')
    parser.add_argument('-t', '--texte', type=str, metavar='TXT', required=False,
                        help='Texte à stocker dans les fichiers crées')
    parser.add_argument('files', metavar='FILE', type=str, nargs='+', help='Fichiers à créer')
    return parser.parse_args()


def main() -> None:
    """Fonction principale"""
    args = parse_args()
    try:
        for file in args.files:
            if os.path.isfile(file) and not args.quiet:
                print(f"{Fore.YELLOW}Le fichier existe déjà: {Fore.CYAN}{file}")
            else:
                f = open(file, "w+")
                if args.texte is not None:
                    f.write(args.texte)
                f.close()
                if args.verbeux:
                    print(f"{Fore.WHITE}Fichier créé: {Fore.CYAN}{file}")
    except OSError as error:
        print(f"{Fore.RED}{error.__class__.__name__}{Fore.YELLOW}: {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
