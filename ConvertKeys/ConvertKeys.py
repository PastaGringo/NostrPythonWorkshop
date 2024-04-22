#!/usr/bin/env python3

from nostr_protocol import Keys, SecretKey, PublicKey

def main():
    print()
    npub_bech32_str = "npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy"
    npub_hex_str = "aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4"
    nsec_bech32_str = "nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99"
    nsec_hex_str = "9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028"
    print("npub_str:",npub_bech32_str)
    print("npub_hex:",npub_hex_str)
    print("nsec_str:",nsec_bech32_str)
    print("nsec_hex:",nsec_hex_str)
    print()
    #######################################################################
    print("nsec_hex_str -> nsec_bech32")
    secret_key = SecretKey.from_hex(nsec_hex_str)
    nsec_bech32 = secret_key.to_bech32()
    print("nsec_hex_str:", nsec_hex_str)
    print(f"Found nsec_bech32: {nsec_bech32} <- should be: {nsec_bech32_str}")
    #######################################################################
    print()
    #######################################################################
    print("nsec_bech32_str -> nsec_hex")
    secret_key = SecretKey.from_bech32(nsec_bech32_str)
    nsec_hex = secret_key.to_hex()
    print("nsec_bech32_str:", nsec_bech32_str)
    print(f"Found nsec_hex: {nsec_hex} <- should be: {nsec_hex_str}")
    #######################################################################
    print()
    #######################################################################
    print("npub_hex_str -> npub_bech32")
    secret_key = PublicKey.from_hex(npub_hex_str)
    npub_bech32 = secret_key.to_bech32()
    print("npub_hex_str:", npub_hex_str)
    print(f"Found npub_bech32: {npub_bech32} <- should be: {npub_bech32_str}")
    #######################################################################
    print()
    #######################################################################
    print("npub_bech32_str -> npub_hex")
    secret_key = PublicKey.from_bech32(npub_bech32_str)
    npub_hex = secret_key.to_hex()
    print("npub_bech32_str:", npub_bech32_str)
    print(f"Found npub_hex: {npub_hex} <- should be: {npub_hex_str}")
    #######################################################################
    
if __name__ == "__main__":
    main()
