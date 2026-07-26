import math


# ==========================================================
# STM32H723ZG + W9825G6KH-6 SDRAM timing calculator
# ==========================================================

# FMC kernel clock frequency
FMC_KERNEL_CLOCK_HZ = 200_000_000

# FMC SDRAM clock divider:
#   2 -> SDCLK = FMC kernel clock / 2
#   3 -> SDCLK = FMC kernel clock / 3
SDRAM_CLOCK_DIVIDER = 3


# ==========================================================
# W9825G6KH-6 geometry
# ==========================================================

NUMBER_OF_ROWS = 8192
NUMBER_OF_COLUMNS = 512
NUMBER_OF_INTERNAL_BANKS = 4
DATA_WIDTH_BITS = 16


# ==========================================================
# W9825G6KH-6 timing requirements
# ==========================================================

# Timings specified in nanoseconds
T_XSR_NS = 72
T_RAS_NS = 42
T_RC_NS = 60
T_RP_NS = 15
T_RCD_NS = 15

# Timings specified directly in SDRAM clock cycles
T_MRD_CYCLES = 2
T_WR_CYCLES = 2


# ==========================================================
# Refresh configuration
# ==========================================================

REFRESH_PERIOD_SECONDS = 64e-3
NUMBER_OF_REFRESH_ROWS = 8192

# STM32 FMC refresh-counter safety margin
FMC_REFRESH_MARGIN_CYCLES = 20


# ==========================================================
# SDRAM mode-register configuration
# ==========================================================

# Burst length 1
MODE_BURST_LENGTH = 0b000

# Sequential burst
MODE_BURST_TYPE = 0 << 3

# CAS latency 2
MODE_CAS_LATENCY = 0b010 << 4

# Standard operating mode
MODE_OPERATING_MODE = 0b00 << 7

# Single-location write burst
MODE_SINGLE_WRITE_BURST = 1 << 9


# ==========================================================
# Helper functions
# ==========================================================

def ns_to_cycles(timing_ns: float, clock_period_ns: float) -> int:
    """
    Convert a minimum timing requirement in nanoseconds to
    the required whole number of SDRAM clock cycles.
    """
    return math.ceil(timing_ns / clock_period_ns)


def cycles_to_ns(cycles: int, clock_period_ns: float) -> float:
    """
    Convert SDRAM clock cycles back to nanoseconds.
    """
    return cycles * clock_period_ns


# ==========================================================
# Clock calculations
# ==========================================================

sdram_clock_hz = FMC_KERNEL_CLOCK_HZ / SDRAM_CLOCK_DIVIDER

sdram_clock_mhz = sdram_clock_hz / 1_000_000

sdram_clock_period_ns = 1_000_000_000 / sdram_clock_hz


# ==========================================================
# Geometry calculations
# ==========================================================

row_address_bits = int(math.log2(NUMBER_OF_ROWS))

column_address_bits = int(math.log2(NUMBER_OF_COLUMNS))

capacity_per_device_bytes = (
    NUMBER_OF_ROWS
    * NUMBER_OF_COLUMNS
    * NUMBER_OF_INTERNAL_BANKS
    * (DATA_WIDTH_BITS // 8)
)

capacity_per_device_mib = capacity_per_device_bytes / (1024 * 1024)

total_capacity_mib = capacity_per_device_mib * 2


# ==========================================================
# FMC timing calculations
# ==========================================================

load_to_active_delay = T_MRD_CYCLES

exit_self_refresh_delay = ns_to_cycles(
    T_XSR_NS,
    sdram_clock_period_ns,
)

self_refresh_time = ns_to_cycles(
    T_RAS_NS,
    sdram_clock_period_ns,
)

row_cycle_delay = ns_to_cycles(
    T_RC_NS,
    sdram_clock_period_ns,
)

write_recovery_time = T_WR_CYCLES

row_precharge_delay = ns_to_cycles(
    T_RP_NS,
    sdram_clock_period_ns,
)

row_to_column_delay = ns_to_cycles(
    T_RCD_NS,
    sdram_clock_period_ns,
)


# ==========================================================
# Effective timing calculations
# ==========================================================

effective_t_xsr_ns = cycles_to_ns(
    exit_self_refresh_delay,
    sdram_clock_period_ns,
)

effective_t_ras_ns = cycles_to_ns(
    self_refresh_time,
    sdram_clock_period_ns,
)

effective_t_rc_ns = cycles_to_ns(
    row_cycle_delay,
    sdram_clock_period_ns,
)

effective_t_wr_ns = cycles_to_ns(
    write_recovery_time,
    sdram_clock_period_ns,
)

effective_t_rp_ns = cycles_to_ns(
    row_precharge_delay,
    sdram_clock_period_ns,
)

effective_t_rcd_ns = cycles_to_ns(
    row_to_column_delay,
    sdram_clock_period_ns,
)


# ==========================================================
# Refresh counter calculation
# ==========================================================

refresh_interval_seconds = (
    REFRESH_PERIOD_SECONDS
    / NUMBER_OF_REFRESH_ROWS
)

refresh_interval_microseconds = (
    refresh_interval_seconds
    * 1_000_000
)

refresh_count = math.floor(
    refresh_interval_seconds
    * sdram_clock_hz
) - FMC_REFRESH_MARGIN_CYCLES


# ==========================================================
# SDRAM mode-register calculation
# ==========================================================

mode_register = (
    MODE_BURST_LENGTH
    | MODE_BURST_TYPE
    | MODE_CAS_LATENCY
    | MODE_OPERATING_MODE
    | MODE_SINGLE_WRITE_BURST
)


# ==========================================================
# STM32 FMC constraint checks
# ==========================================================

minimum_write_recovery = (
    self_refresh_time
    - row_to_column_delay
)

write_recovery_constraint_valid = (
    write_recovery_time
    >= minimum_write_recovery
)

timings_fit_hal_fields = all(
    1 <= value <= 16
    for value in (
        load_to_active_delay,
        exit_self_refresh_delay,
        self_refresh_time,
        row_cycle_delay,
        write_recovery_time,
        row_precharge_delay,
        row_to_column_delay,
    )
)


# ==========================================================
# Print results
# ==========================================================

print("=" * 60)
print("STM32H723ZG + W9825G6KH-6 SDRAM configuration")
print("=" * 60)

print()
print("Clock configuration")
print("-------------------")
print(f"FMC kernel clock:       {FMC_KERNEL_CLOCK_HZ / 1_000_000:.3f} MHz")
print(f"SDRAM clock divider:    {SDRAM_CLOCK_DIVIDER}")
print(f"SDRAM clock:            {sdram_clock_mhz:.3f} MHz")
print(f"SDRAM clock period:     {sdram_clock_period_ns:.3f} ns")

print()
print("SDRAM geometry")
print("--------------")
print(f"Row address bits:       {row_address_bits}")
print(f"Column address bits:    {column_address_bits}")
print(f"Internal banks:         {NUMBER_OF_INTERNAL_BANKS}")
print(f"Data width:             {DATA_WIDTH_BITS} bits")
print(f"Capacity per device:    {capacity_per_device_mib:.1f} MiB")
print(f"Capacity for 2 devices: {total_capacity_mib:.1f} MiB")

print()
print("CubeMX / HAL timing values")
print("--------------------------")
print(f"LoadToActiveDelay:      {load_to_active_delay}")
print(f"ExitSelfRefreshDelay:   {exit_self_refresh_delay}")
print(f"SelfRefreshTime:        {self_refresh_time}")
print(f"RowCycleDelay:          {row_cycle_delay}")
print(f"WriteRecoveryTime:      {write_recovery_time}")
print(f"RPDelay:                {row_precharge_delay}")
print(f"RCDDelay:               {row_to_column_delay}")

print()
print("Effective timing values")
print("-----------------------")
print(
    f"tXSR: {effective_t_xsr_ns:.3f} ns "
    f"(minimum {T_XSR_NS} ns)"
)
print(
    f"tRAS: {effective_t_ras_ns:.3f} ns "
    f"(minimum {T_RAS_NS} ns)"
)
print(
    f"tRC:  {effective_t_rc_ns:.3f} ns "
    f"(minimum {T_RC_NS} ns)"
)
print(
    f"tWR:  {effective_t_wr_ns:.3f} ns "
    f"({T_WR_CYCLES} clock cycles required)"
)
print(
    f"tRP:  {effective_t_rp_ns:.3f} ns "
    f"(minimum {T_RP_NS} ns)"
)
print(
    f"tRCD: {effective_t_rcd_ns:.3f} ns "
    f"(minimum {T_RCD_NS} ns)"
)

print()
print("Refresh configuration")
print("---------------------")
print(
    f"Refresh interval:      "
    f"{refresh_interval_microseconds:.4f} us"
)
print(f"Refresh counter:       {refresh_count}")

print()
print("Mode register")
print("-------------")
print(f"Mode-register value:   0x{mode_register:04X}")

print()
print("Constraint checks")
print("-----------------")
print(
    f"TWR >= TRAS - TRCD:    "
    f"{write_recovery_constraint_valid}"
)
print(
    f"Timing field ranges:   "
    f"{timings_fit_hal_fields}"
)

print()
print("Recommended FMC configuration")
print("-----------------------------")
print("ColumnBitsNumber       = FMC_SDRAM_COLUMN_BITS_NUM_9")
print("RowBitsNumber          = FMC_SDRAM_ROW_BITS_NUM_13")
print("MemoryDataWidth        = FMC_SDRAM_MEM_BUS_WIDTH_16")
print("InternalBankNumber     = FMC_SDRAM_INTERN_BANKS_NUM_4")
print("CASLatency             = FMC_SDRAM_CAS_LATENCY_2")
print("WriteProtection        = FMC_SDRAM_WRITE_PROTECTION_DISABLE")
print("SDClockPeriod          = FMC_SDRAM_CLOCK_PERIOD_2")
print("ReadBurst              = FMC_SDRAM_RBURST_ENABLE")
print("ReadPipeDelay          = FMC_SDRAM_RPIPE_DELAY_2")

print()
print("Generated C timing structure")
print("----------------------------")
print("FMC_SDRAM_TimingTypeDef timing = {")
print(f"    .LoadToActiveDelay    = {load_to_active_delay},")
print(f"    .ExitSelfRefreshDelay = {exit_self_refresh_delay},")
print(f"    .SelfRefreshTime      = {self_refresh_time},")
print(f"    .RowCycleDelay        = {row_cycle_delay},")
print(f"    .WriteRecoveryTime    = {write_recovery_time},")
print(f"    .RPDelay              = {row_precharge_delay},")
print(f"    .RCDDelay             = {row_to_column_delay},")
print("};")

print()
print("Generated C constants")
print("---------------------")
print(f"#define SDRAM_MODE_REGISTER 0x{mode_register:04X}U")
print(f"#define SDRAM_REFRESH_COUNT {refresh_count}U")
