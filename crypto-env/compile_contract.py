import json
from solcx import compile_standard, install_solc

# Install the Solidity compiler version
install_solc('0.8.0')

# Read the Solidity source code
with open('DripGlobalCoin.sol', 'r') as file:
    drip_global_coin_source = file.read()

# Compile the contract
compiled_sol = compile_standard({
    'language': 'Solidity',
    'sources': {
        'DripGlobalCoin.sol': {
            'content': drip_global_coin_source
        }
    },
    'settings': {
        'outputSelection': {
            '*': {
                '*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
            }
        }
    }
})

# Save the compiled contract to a file
with open('compiled_drip_global_coin.json', 'w') as file:
    json.dump(compiled_sol, file)

# Extract ABI and bytecode
abi = compiled_sol['contracts']['DripGlobalCoin.sol']['DripGlobalCoin']['abi']
bytecode = compiled_sol['contracts']['DripGlobalCoin.sol']['DripGlobalCoin']['evm']['bytecode']['object']
