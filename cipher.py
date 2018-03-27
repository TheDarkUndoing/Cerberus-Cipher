import sys, math, argparse, optparse


def banner():
    print("_________             ___.                               ")
    print("\_   ___ \  __________\_ |__   ___________ __ __  ______ ")
    print("/    \  \/_/ __ \_  __ \ __ \_/ __ \_  __ \  |  \/  ___/ ")
    print("\     \___\  ___/|  | \/ \_\ \  ___/|  | \/  |  /\___ \  ")
    print(" \______  /\___  >__|  |___  /\___  >__|  |____//____  > ")
    print("        \/     \/          \/     \/                 \/  ")
    print("_________ .__       .__                                  ")
    print("\_   ___ \|__|_____ |  |__   ___________  ______         ")
    print("/    \  \/|  \____ \|  |  \_/ __ \_  __ \/  ___/         ")
    print("\     \___|  |  |_> >   Y  \  ___/|  | \/\___ \          ")
    print(" \______  /__|   __/|___|  /\___  >__|  /____  >         ")
    print("        \/   |__|        \/     \/           \/          ")
    print("                                                         ")

    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")


def cipher():
	EncryptDecrypt = input("Would you like to encrypt or decrypt a string?\n")

	if(EncryptDecrypt == "-e"):
		print("encrypting.....")

	elif(EncryptDecrypt == 'd'):
		print("decrypting.....")

	else:
		print("You did not enter a valid input")


def main():
	banner()
	cipher()

main()
