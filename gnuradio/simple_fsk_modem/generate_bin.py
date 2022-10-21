#!/usr/bin/env python

import struct, binascii

# Mensagem para enviar no radio!
message = b"Hacker Hackeia\nH2HC2022\nAtaque dos Piriquer\n526 Terabytes de encryption\n"

# Usado para "treinar" o sincronizador de clock do receptor
preamble = b"\x55\xaa" * 12

# Usado para sabermos o inicio da mensagem
# No GNU Radio geralmente eh chamado de "Access Code", mas o termo correto eh "Sync Word"
syncword = binascii.unhexlify("DEADBEEF1337")

# Tamanho codificado, o bloco do gnuradio espera um header com o tamanho do conteudo
# codificado em duas variaveis do tipo short (16 bits) seguidas com o mesmo valor e
# em big-endian (network-endian)
header = struct.pack(">HH", len(message), len(message))

# Agora soh salvar
with open("basebin.bin", "wb") as f:
    f.write(preamble)
    f.write(syncword)
    f.write(header)
    f.write(message)

# Done :D