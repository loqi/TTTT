############
# scrib41 - A "base 41" numeral format specifying large integers as short strings.
#   This format uses 41 alphanumeric characters as positional digits, which are
#   in turn grouped into three-digit segments. Mathematically speaking, each such
#   character is only a pseudo-digit. The actual digits are the three-character
#   groupings of pseudo-digits, making 65536 the technical radix of this format.
#
#   The standard Latin characters of scrib41 comprise a subset of the alphanumerics
#   optimized for human eyesight and handwriting with its compromised legibility.
#   In sequence:
#       - 0..9      0 1 2 3 4 5 6 7 8 9
#       - 10..19    A C D E F H J K L M
#       - 20..29    N P Q R T U V W X a
#       - 30..40    b d e f h j m r t u y
#
#   Latin characters that might be mistaken for one of these 41 characters are
#   interpreted as synonym characters for a canonical scrib41 pseudo-digit:
#       0 1 2 3 4 5 6 7 8 9 A 8 C D E F 6 H 1 J K L M N 0 P Q R 5 T U
#       V W X 4 2 a b C d e f 9 h 1 j K 1 m h 0 P 9 r 5 t u V W X y 2
#
#   Additionally, the underscore character (_) may be infixed to group sequences of
#   six of these pseudo-digits to aid human scanability. When present, underscores
#   must be positioned between the sixth and seventh pseudo-digit, and then at every
#   multiple of six pseudo-digits. The final three or six pseudo-digits are grouped
#   with an underscore to their left and not to their right.
#
#   All scrib41 numerals describe integers whose memory length is an even number
#   of octets in length (multiples of sixteen bits). The actual digits are three
#   pseudo-digits in length, and each digit trio must fall within the range 000..yrG
#   (zero to 0xFFFF=65535).
#
#   Samples of integers represented as scrib41 numerals and hex equivalets:
#       000000_000000_000   = 0000_0000_0000_0000_0000
#       AXr9H7_5TWmyP       = 467f_3db0_24f2_f973
#       001001              = 0001_0001
#       tyKtyK_tyK          = ffff_ffff_ffff
#       tyL                 = invalid numeral: overflows as 0x1_0000
#       yyy                 = invalid numeral: overflows as 0x1_0d38

def scrib41_from_int64(int64)
    ret = int64
    return ret

def scrib41_from_byteS(byteS)
    ret = byteS
    return ret

def int64_from_scrib41(scrib41)
    ret = scrib41
    return ret

def byteS_from_scrib41(scrib41)
    ret = scrib41
    return ret
