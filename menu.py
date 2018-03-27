import argparse
from banner import banner

def menu():
	#parser = argparse.ArgumentParser(prog='CerberusCipher', description=banner())
	parser = argparse.ArgumentParser(description=banner())
	parser.add_argument('-e', '--encrypt', help='encrypt phrase',
						action='store_true')

	parser.add_argument('-d', '--decrypt', help='decrypt phrase',
						action='store_true')


	args = parser.parse_args()
	#print(args.accumulate(args.Help))

menu()