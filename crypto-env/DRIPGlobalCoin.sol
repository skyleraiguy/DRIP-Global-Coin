// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract DripGlobalCoin is ERC20 {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000_000 * (10 ** 18); // 1 trillion tokens with 18 decimals

    constructor() ERC20("Drip Global Coin", "DGC") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }
}
