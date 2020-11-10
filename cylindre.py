#!/usr/bin/env python3

"""
Programme calculant le volume d'un cylindre

Par Éthan Leduc
"""

import argparse
import math


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculateur de volume pour cylindre -- ©2020, par Éthan Leduc")
    parser.add_argument('-r', '--rayon', type=float, metavar='R', required=True, help='Rayon du cylindre')
    parser.add_argument('-H', '--hauteur', type=float, metavar='H', required=True, help='Heuteur du cylindre')
    parser.add_argument('-p', '--précision', type=int, metavar='P', required=False, help='Précision du calcul')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='Afficher seulement le volume')
    group.add_argument('-v', '--verbeux', action='store_true', help='Afficher le maximum d\'info')
    return parser.parse_args()


def volume_cylindre(rayon: float, hauteur: float) -> float:
    return math.pi * (rayon ** 2) * hauteur


def main() -> None:
    """Fonction principale"""
    args = parse_args()
    volume = volume_cylindre(args.rayon, args.hauteur)
    if args.précision is not None:
        format_string = "{:." + str(args.précision) + "f}"
        volume = format_string.format(volume)
    if args.quiet:
        print(volume)
    elif args.verbeux:
        print(f"Volume du cylindre de hauteur {args.hauteur} et de rayon {args.rayon} selon EL: {volume}")
    else:
        print(f"Volume du cylindre selon EL: {volume}")
    return


if __name__ == '__main__':
    main()
