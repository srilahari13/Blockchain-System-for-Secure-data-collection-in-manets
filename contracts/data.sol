// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract data {
  
  uint[] _a; // array (dynamic) - arrays
  uint[] _b;
  uint[] _c;

  function insertData(uint a,uint b,uint c) public{
    _a.push(a);
    _b.push(b);
    _c.push(c);
  }

  function viewData() public view returns(uint[] memory,uint[] memory,uint[] memory) {
    return(_a,_b,_c);
  }
}
