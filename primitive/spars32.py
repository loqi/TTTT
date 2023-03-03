############
# spars32 - A binary integer format using a 32-bit signed integer to represent
# a 64-bit signed floating-magnitude integer. This format provides eight decimal
# digits of precision, and a magnitude range spanning a signed 64-bit integer.
#
# It is intended to compress a 64-bit integer into a 32-bit integer by sacrificing
# precision for range. It is designed to exceed human-scale range and precision
# needs. All possible 32-bit integers unambigueusly and efficiently map to one signed
# 64-bit two's-compliment integer value. Arithmetic may not be performed directly on
# a spars32 integer, and must instead be done on its 64-bit expansion. Signed integer
# compare functions performed directly between spars32 values always produce correct
# results.
#
# Spars32 values in the -1G to +1G range represent their exact integer value, i.e.
# for values in this range, we have nine significant decimal digits. Values in the
# 1,000,000,000..1,360,000,000 (positive or negative) provide 8.25 significant digits
# in the 64-bit expansion -- that is, a spars32 integer can represent 64-bit integers
# 1234567800, 1234567825, 1234567850, 1234567875, and so on. Values in the range
# 1360M..1450M (positive or negative) provide 8 significant digits and an resolution
# increment of 1000, representing this set of expanded values: { 10,000,000,000
# 10,000,001,000  10,000,002,000  ... 99,999,998,000  99,999,999,000 }. This pattern
# holds with each successive set of 90,000,000 consecutive 32-bit values mapping to
# a set of 64-bit values with ten times the magnitude, eight significant digits and
# zeros as the low-order digits. So, the 32-bit range 1450M..1540M maps to 32-bit
# values { 100,000,000,000  100,000,010,000  ...  999,999,980,000  999,999,990,000 }.
# This pattern is interrupted when the final 32-bit positive or negative value is
# reached, setting an outer limit to the mappable 64-bit value. A spars32 value of
# -2147488648 maps to -7,748,364,800,000.000,000 and +2147488647 maps to the 64-bit
# integer value +7,748,364,700,000.000,000. Any 64-bit value outside this range has
# no spars32 equivalent.

# Samples of integers represented as spars32 bit fields and decimal equivalets:
#
#    32-bit value  |                 64-bit value   | if v32 < 1000M  (increment 1)
#              -1  |                   -0.000,001
#               0  |                    0.000,000   |    v64 = v32
#               1  |                    0.000,001   |
#     999,999,999  |                  999.999,999   |
#   1,000,000,000  |                1,000.000,000   | if v32 < 1360M  (increment 25)
#   1,000,000,001  |                1,000.000,025   |    v64 = (v32 - 1G) * 25 + 1G
#   1,000,000,002  |                1,000.000,050   |
#   1,359,999,998  |                9,999.999,950   |
#   1,359,999,999  |                9,999.999,975   |
#   1,360,000,000  |               10,000.000,000   | if v32 < 1450M  (increment 1K)
#   1,090,000,001  |               10,000.001,000   |    v64 = (v32 - 1360M) * 1000 + 10G
#   1,449,999,999  |               99,999.999,000   |
#   1,450,000,000  |              100,000.000,000   | if v32 < 1540M  (increment 10K)
#   1,450,000,001  |              100,000.010,000   |    v64 = (v32 - 1450M) * 10K + 100G
#   1,539,999,999  |              999,999.990,000   |
#   1,540,000,000  |            1,000,000.000,000   | if v32 < 1630M  (increment 100K)
#   1,540,000,001  |            1,000,000.100,000   |    v64 = (v32 - 1540M) * 100K + 1T
#   1,629,999,999  |            9,999,999.900,000   |
#   1,630,000,000  |           10,000,000.000,000   | if v32 < 1720M (increment 1M)
#   1,630,000,001  |           10,000,001.000,000   |    v64 = (v32 - 1630M) * 1M + 10T
#   1,719,999,999  |           99,999,999.000,000   |
#   1,720,000,000  |          100,000,000.000,000   | if v32 < 1810M  (increment 10M)
#   1,720,000,001  |          100,000,010.000,000   |    v64 = (v32 - 1720M) * 10M + 100T
#   1,809,999,999  |          999,999,990.000,000   |
#   1,810,000,000  |        1,000,000,000.000,000   | if v32 < 1900M  (increment 100M)
#   1,810,000,001  |        1,000,000,100.000,000   |    v64 = (v32 - 1810M) * 100M + 10^15
#   1,899,999,999  |        9,999,999,900.000,000   |
#   1,900,000,000  |       10,000,000,000.000,000   | if v32 < 1990M  (increment 1G)
#   1,900,000,001  |       10,000,001,000.000,000   |    v64 = (v32 - 1900M) * 1G + 10^16
#   1,989,999,999  |       99,999,999,000.000,000 
#   1,990,000,000  |      100,000,000,000.000,000   | if v32 < 2080M  (increment 10G)
#   1,990,000,001  |      100,000,010,000.000,000   |    v64 = (v32 - 1990M) * 10G + 10^17
#   2,079,999,999  |      999,999,990,000.000,000   |
#   2,080,000,000  |    1,000,000,000,000.000,000   | if v32 < (increment 100G)
#   2,080,000,001  |    1,000,000,100,000.000,000   |    v64 = (v32 - 2080M) * 100G + 10^18
#   2,147,483,646  |    7,748,364,600,000.000,000   | 
#   2,147,483,647  |    7,748,364,700,000.000,000   | (limiting positive value)
#  -2,147,483,648  |   -7,748,364,800,000.000,000   | (limiting negative value)

def spars32_from_int64(v64)
    if v64 > -1_000_000_000
        if v64 < 1_000_000_000
            return v64
        if v64 < 10_000_000_000
            return v64 / 25 + 960_000_000
        if v64 < 100_000_000_000
            return v64 / 1_000 + 1_350_000_000
        if v64 < 1_000_000_000_000
            return v64 / 10_000 + 1_440_000_000
        if v64 < 10_000_000_000_000
            return v64 / 100_000 + 1_530_000_000
        if v64 < 100_000_000_000_000
            return v64 / 1_000_000 + 1_620_000_000
        if v64 < 1_000_000_000_000_000
            return v64 / 10_000_000 + 1_710_000_000
        if v64 < 10_000_000_000_000_000
            return v64 / 100_000_000 + 1_800_000_000
        if v64 < 100_000_000_000_000_000
            return v64 / 1_000_000_000 + 1_890_000_000
        if v64 < 1_000_000_000_000_000_000
            return v64 / 10_000_000_000 + 1_980_000_000
        if v64 <= 7_748_364_700_000_000_000
            return v64 / 100_000_000_000 + 2_070_000_000
        return 2147483647
    else
        if v64 > -10_000_000_000
            return v64 / 25 + 960_000_000
        if v64 > -100_000_000_000
            return v64 / 1_000 + 1_350_000_000
        if v64 > -1_000_000_000_000
            return v64 / 10_000 + 1_440_000_000
        if v64 > -10_000_000_000_000
            return v64 / 100_000 + 1_530_000_000
        if v64 > -100_000_000_000_000
            return v64 / 1_000_000 + 1_620_000_000
        if v64 > -1_000_000_000_000_000
            return v64 / 10_000_000 + 1_710_000_000
        if v64 > -10_000_000_000_000_000
            return v64 / 100_000_000 + 1_800_000_000
        if v64 > -100_000_000_000_000_000
            return v64 / 1_000_000_000 + 1_890_000_000
        if v64 > -1_000_000_000_000_000_000
            return v64 / 10_000_000_000 + 1_980_000_000
        if v64 >= -7_748_364_800_000_000_000
            return v64 / 100_000_000_000 + 2_070_000_000
    return -2147483648


def int64_from_spars32(spars32)
    int64 = spars32

    return int64
