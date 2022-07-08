pragma solidity ^0.8.15;

contract Soln{
    bytes32 _name = bytes32("smarx");
    IFuzzyIdentityChallenge cahallengeContract = IFuzzyIdentityChallenge(0x6deac7236829467a34032dc80C119340bb451e3c);
    
    function solveChallange() public {
        cahallengeContract.authenticate();
    }
    
    function name() external view returns (bytes32){
        return _name;
    }
}

interface IFuzzyIdentityChallenge {
    function authenticate() external;
}