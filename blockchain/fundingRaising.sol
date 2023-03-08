// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.0 <0.9.0;

contract FundRaising {
    uint public constant MINIMUM_AMOUNT = 1e16;
    uint public fundRaisingCloses;  // 모금 종료 시각
    address public beneficiary;     // 모금 수령자

    constructor (uint _duration, address _beneficiary) {
        fundRaisingCloses = block.timestamp + _duration;
        beneficiary = _beneficiary;
    }

    address[] funders;

    function fund() public payable {
        require(msg.value > MINIMUM_AMOUNT, "MINIMUM AMOUND : 0.01 ether");
        require(block.timestamp < fundRaisingCloses, "FUND RAISING CLOSED");

        address funder = msg.sender;
        funders.push(funder);
    }

    function currentCollection() public view 
    // view를 통해 가스비를 제공하지 않고 사용할 수 있는 함수
    returns(uint256) {
        return address(this).balance; // 주소자가 가지고 있는 이더 양
    }

    modifier onlyBeneficiary() { // modifier를 통해서 자주 사용하는 함수를
    // 미리 지정해 놓을 수 있다.
        require(msg.sender == beneficiary);
        _; // 다시 함수로 돌아간다
    }

    modifier onlyAfterFundCloses() {
        require(block.timestamp > fundRaisingCloses);
        _;
    }

    function withdraw() public payable 
    onlyBeneficiary onlyAfterFundCloses {
        payable(msg.sender).transfer(address(this).balance);
    }

}