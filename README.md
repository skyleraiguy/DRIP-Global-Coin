# Drip Global Coin

Drip Global Coin (DGC) is a cryptocurrency designed for microtransactions and Pay-As-You-Go services. This project includes the smart contract for the token, Python scripts to interact with the Ethereum blockchain, and a custom C library to handle transactions.

## Project Structure

```
DripGlobalCoin/
├── .vscode/
│   └── settings.json
├── contracts/
│   └── DRIPGlobalCoin.sol
├── crypto-env/
│   ├── Include/
│   │   ├── drip_pay_lib.h
│   │   └── Python.h
│   ├── Lib/
│   ├── Scripts/
│   │   ├── compile_contract.py
│   │   ├── deploy_contract.py
│   │   ├── interact_contract.py
│   │   └── test_drippay.py
├── setup.py
├── Python.c
├── drip_pay_lib.c
├── pyvenv.cfg
└── README.md
```

## Prerequisites

- Python 3.8+
- Ganache (for local Ethereum blockchain development)
- Node.js and npm (for installing Truffle if needed)
- Solidity compiler (solc) or (py-solc-x)

## Installation

### Setting Up the Environment

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/skyleraiguy/DripGlobalCoin.git
   cd DripGlobalCoin
   ```

2. **Create a Virtual Environment**:
   ```sh
   python -m venv crypto-env
   source crypto-env/bin/activate   # On Windows use `crypto-env\Scripts\activate`
   ```

3. **Install Python Dependencies**:
   ```sh
   pip install web3 py-solc-x
   ```

4. **Install Node.js and Truffle (if not already installed)**:
   ```sh
   npm install -g truffle
   ```

### Compile and Deploy the Smart Contract

1. **Compile the Smart Contract**:
   ```sh
   python crypto-env/Scripts/compile_contract.py
   ```

2. **Deploy the Smart Contract**:
   - Update the `YOUR_INFURA_ENDPOINT` in `deploy_contract.py`.
   - Run the deployment script:
     ```sh
     python crypto-env/Scripts/deploy_contract.py
     ```

### Build the C Extension Module

1. **Build the C Extension**:
   ```sh
   python setup.py build_ext --inplace
   ```

## Usage

### Interacting with the Smart Contract

1. **Run the Interaction Script**:
   - Update the `YOUR_DEPLOYED_CONTRACT_ADDRESS` in `interact_contract.py`.
   - Run the script:
     ```sh
     python crypto-env/Scripts/interact_contract.py
     ```

### Testing the DripPay Library

1. **Run the Test Script**:
   ```sh
   python crypto-env/Scripts/test_drippay.py
   ```

## Files and Directories

- **`.vscode/settings.json`**: Configuration for VSCode.
- **`contracts/DRIPGlobalCoin.sol`**: Solidity smart contract for the Drip Global Coin.
- **`crypto-env/Include/drip_pay_lib.h`**: Header file for the custom C library.
- **`crypto-env/Include/Python.h`**: Header file for Python C API integration.
- **`crypto-env/Lib/`**: Directory for any additional libraries.
- **`crypto-env/Scripts/compile_contract.py`**: Script to compile the Solidity contract.
- **`crypto-env/Scripts/deploy_contract.py`**: Script to deploy the compiled contract to the Ethereum blockchain.
- **`crypto-env/Scripts/interact_contract.py`**: Script to interact with the deployed smart contract.
- **`crypto-env/Scripts/test_drippay.py`**: Script to test the `drippay` module.
- **`setup.py`**: Setup script to build the C extension module.
- **`Python.c`**: Implementation of the functions declared in `Python.h`.
- **`drip_pay_lib.c`**: Implementation of the core logic of the custom library.
- **`pyvenv.cfg`**: Configuration for the Python virtual environment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For more information, you can connect with Skyler Seegmiller on here on LinkedIn or X.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/skyler-seegmiller)
[![X](https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/SkylerSeeg)

```

This `README.md` file provides a comprehensive guide to setting up and using your Drip Global Coin project, including compiling and deploying the smart contract, building the C extension module, and running tests. Make sure to replace placeholders like `YOUR_INFURA_ENDPOINT` and `YOUR_DEPLOYED_CONTRACT_ADDRESS` with actual values relevant to your deployment.
