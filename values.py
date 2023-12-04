# Condition mnemonics
COND = {
    "0000": "EQ",
    "0001": "NE",
    "0010": "HS",
    "0011": "LO",
    "0100": "MI",
    "0101": "PL",
    "0110": "VS",
    "0111": "VC",
    "1000": "HI",
    "1001": "LS",
    "1010": "GE",
    "1011": "LT",
    "1100": "GT",
    "1101": "LE",
    "1110": "AL"
}

# cmd mnemonics
# cmd specifies the data-processing instruction
CMD = {
    "0000": "AND",
    "0001": "EOR",
    "0010": "SUB",
    "0011": "RSB",
    "0100": "ADD",
    "0101": "ADC",
    "0110": "SBC",
    "0111": "RSC",
    "1000": "TST",
    "1001": "TEQ",
    "1010": "CMP",
    "1011": "CMN",
    "1100": "ORR",
    "1101": "MOV", # This one will include other shifts
    "1110": "BIC",
    "1111": "MVN"
}

# sh instruction mnemonics
SH = {
    "00": "LSL",
    "01": "LSR",
    "10": "ASR",
    "11": "ROR"
}

# PW combinations
PW = {
    "00": "Post-index",
    "01": "Not supported",
    "10": "Offset",
    "11": "Pre-index"
}

# LB combinations
LB = {
    "00": "STR",
    "01": "STRB",
    "10": "LDR",
    "11": "LDRB"
}

