// Example Hack Program - Cache Simulator Test
// This program reads and writes to various memory addresses
// to test the cache simulator behavior

// Initialize address 0x4000 with value 1
@16384
M=1

// Initialize address 0x4001 with value 2
@16385
M=2

// Initialize address 0x4002 with value 3
@16386
M=3

// Read from 0x4000
@16384
D=M

// Write to 0x4100
@16640
M=D

// Read from 0x4001
@16385
D=M

// Write to 0x4101
@16641
M=D

// Read from 0x4002
@16386
D=M

// Write to 0x4102
@16642
M=D

// Loop: Read from 0x4000-0x4002 again (for cache behavior test)
@16384
D=M

@16384
D=M

@16385
D=M

@16386
D=M
