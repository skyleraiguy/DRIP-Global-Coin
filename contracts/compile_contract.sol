from solcx import compile_standard
import json

# Read the Solidity contract
with open('../contracts/DRIPGlobalCoin.sol', 'r') as file:
    drip_source_code = file.read()

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "DRIPGlobalCoin.sol": {
            "content": drip_source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        }
    }
}, solc_version='0.8.7')

# Write the compiled code to a JSON file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

print("Contract compiled successfully.")
