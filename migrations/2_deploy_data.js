const data = artifacts.require("data");

module.exports = function (deployer) {
  deployer.deploy(data);
};
