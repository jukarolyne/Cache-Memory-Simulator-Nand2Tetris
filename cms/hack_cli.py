#!/usr/bin/env python3
"""
Hack Converter CLI - Standalone tool to convert Hack code to memory sequences

Usage:
    python hack_cli.py <input_file.asm>
    python hack_cli.py <input_file.asm> -o <output_file.txt>
    python hack_cli.py --stdin
"""

import sys
import argparse
from pathlib import Path

# Import the converter from web_backend
sys.path.insert(0, str(Path(__file__).parent))
from web_backend import convert_hack_to_sequence

def main():
    parser = argparse.ArgumentParser(
        description="Convert Hack assembly code to memory access sequences"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Input Hack assembly file (.asm)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read from stdin instead of file"
    )
    
    args = parser.parse_args()
    
    # Read input
    if args.stdin or not args.input:
        print("Reading from stdin (Ctrl+D to finish):", file=sys.stderr)
        hack_code = sys.stdin.read()
    else:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        
        with open(input_path, 'r') as f:
            hack_code = f.read()
    
    # Convert
    success, sequences, error = convert_hack_to_sequence(hack_code)
    
    if not success:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    
    # Generate output
    output_text = "\n".join(sequences)
    
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w') as f:
            f.write(output_text)
        print(f" Converted {len(sequences)} sequences", file=sys.stderr)
        print(f" Output written to: {output_path}", file=sys.stderr)
    else:
        # Print to stdout
        print(output_text)
        print(f"\n# {len(sequences)} sequences generated", file=sys.stderr)

if __name__ == "__main__":
    main()
