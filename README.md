# PyChain

PyChain is a project that aims to implement easy to use and easy to understand Payment Gateways for merchants and customers alike.

# Understanding PyChain

  - PyChain was initially introduced to the community as a [Bismuth](https://github.com/hclivess/Bismuth) fork, but we decided against that in a further decision because of the strongly different use cases of both projects.
  - PyChain aims to be ASIC resistant and will do that by implementing a memory-heavy PoW algorithm. This is to prevent potential attackers from executing a 51% attack or any similarly malicious activity.


# Technical:
  - As of now (30.10.2018), it's planned for PyChain to use Keccak384 from the SHA3 specification as a hashing algorithm. 
  - The structure for blocks is strongly inspirded by [simplecrypto 's cryptokit](http://github.com/simplecrypto/cryptokit/blob/master/cryptokit/block.py#L96)
  - For dynamic difficulty adjusting, PyChain will implement Kimoto Gravity Well which did perform well during tests.

