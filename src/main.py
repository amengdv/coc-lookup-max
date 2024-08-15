#!/usr/bin/env python3

import argparse

from csvhandler import get_col_at, get_csv_content

def main():
    
    parser = argparse.ArgumentParser(
        prog="CoC Lookup Max",
        description="Help user lookup max building level per townhall level in Clash Of Clans",
    )

    parser.add_argument("th", type=int, help="Your townhall level: 7-16")
    parser.add_argument(
            "category",
            type=str,
            help="Category [defensive, armybuild, resources, heroes, spells, army, traps]"
    )

    args = parser.parse_args()

    csv_content = get_csv_content(args.category)

    result = get_col_at(args.th, csv_content)
    
    print(result)



main()

