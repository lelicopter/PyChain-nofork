#PyChain

##What is PyChain?
PyChain is a project that aims to implement easy to use and easy to understand Payment Gateways for merchants and customers alike.

##Why is there a new repo?
PyChain was initially introduced to the community as a Bismuth fork, but we decided against that in a further decision because of the strongly different use cases of both projects.
Another reason for our decision was the advantage existing pools and miners from the Bismuth network could take on the community because of the nearly identical block headers.


##Technical data?
As of now, PyChain is set to use cubepow, a supposedly ASIC-resistant algorithm introduced to me by an early contributor, barrystyle.
The structure for our blocks is strongly inspired by [simplecrypto 's cryptokit](http://github.com/simplecrypto/cryptokit/blob/master/cryptokit/block.py#L96).
For dynamic difficulty adjusting, we'll most likely use Kimoto Gravity Wave. Supposedly there was a flaw to it, but that never got disclosed correctly.
As of now (6th October 2018) everything else is made from scratch.