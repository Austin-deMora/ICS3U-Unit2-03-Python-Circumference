#!/usr/bin/env python3
# Created by: Austin de Mora
# Created on: April 2020
# This program calculates circumference

import constants


def main():
    # This function calculates circumference

    # Input
    radius = int(input("Enter the radius of a circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # Output
    print("")
    print("Circumference is {}mm²".format(circumference))


if __name__ == "__main__":
    main()