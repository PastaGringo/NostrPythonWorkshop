# NostrPythonWorkshop
## Convert Nostr keys
### Install requirements (nostr_protocol)
```
pip install -r requirements.txt
or
pip install nostr_protocol
```
```
python3 ConvertKeys.py

npub_str: npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy
npub_hex: aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4
nsec_str: nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99
nsec_hex: 9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028

nsec_hex_str -> nsec_bech32
nsec_hex_str: 9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028
Found nsec_bech32: nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99 <- should be: nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99

nsec_bech32_str -> nsec_hex
nsec_bech32_str: nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99
Found nsec_hex: 9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028 <- should be: 9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028

npub_hex_str -> npub_bech32
npub_hex_str: aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4
Found npub_bech32: npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy <- should be: npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy

npub_bech32_str -> npub_hex
npub_bech32_str: npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy
Found npub_hex: aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4 <- should be: aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4
```

## Misc
### Generate python requirements.txt
```
pipreqs .
```
### Generate python requirements.txt (overwrite)
```
pipreqs . --force
```
### Clear console function
```
def clear_console():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
```
