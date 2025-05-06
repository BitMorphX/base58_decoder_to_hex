#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "1.0.0"

import base58
from colorama import Fore, Style, init
import os
import hashlib

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def verify_checksum(decoded_bytes):
    body = decoded_bytes[:-4]
    expected_checksum = decoded_bytes[-4:]
    actual_checksum = hashlib.sha256(hashlib.sha256(body).digest()).digest()[:4]
    return actual_checksum == expected_checksum

def decode_base58_to_hex(address):
    try:
        decoded = base58.b58decode(address)
        prefix = decoded[:1].hex()
        pubkey_hash = decoded[1:-4].hex()
        checksum = decoded[-4:].hex()
        is_valid_checksum = verify_checksum(decoded)
        return {
            "prefix": prefix,
            "pubkey_hash": pubkey_hash,
            "checksum": checksum,
            "valid": is_valid_checksum
        }
    except Exception as e:
        raise ValueError(f"Error decoding Base58 address: {e}")

def main():
    init(autoreset=True)
    clear_terminal()

    print(Fore.CYAN + "\nBitcoin Base58 Address Decoder: base58_decoder_to_hex\n")
    print(Fore.YELLOW + "-> Enter a Bitcoin address (Base58 format):")

    address = input(Fore.GREEN + "Address: ").strip()

    try:
        decoded_data = decode_base58_to_hex(address)

        print(Fore.CYAN + "\nDecoded Results:")
        print(Fore.MAGENTA + f"Prefix (HEX): {decoded_data['prefix']}")
        print(Fore.CYAN + f"Public Key Hash (HEX): {decoded_data['pubkey_hash']}")
        print(Fore.RED + f"Checksum (HEX): {decoded_data['checksum']}")

        if decoded_data['valid']:
            print(Fore.GREEN + "\nChecksum valid: ✓")
        else:
            print(Fore.RED + "\nChecksum invalid: ✗")

        print()

    except ValueError as e:
        print(Fore.RED + f"\nError: {e}\n")

if __name__ == "__main__":
    main()
