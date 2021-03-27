"""
Make an NFT from a Musk Tweet (or anything else you want)
This program is made for fun!!!
"""

"""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd


import uuid
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
FILE_NAME = str(uuid.uuid4()) + "_" + str(timestr) + ".txt"
ELON_TWEET = "https://twitter.com/elonmusk/status/1375652425814704128"

f = open(FILE_NAME, "a")

f.write("\n\n\n----NFT STARTS HERE----\n\n\n")

f.write(str(uuid.uuid1()) + "\n")

f.write(str(uuid.uuid3(uuid.NAMESPACE_DNS,
                       ELON_TWEET)) + "\n")

f.write(str(uuid.uuid4()) + "\n")

f.write(str(uuid.uuid5(uuid.NAMESPACE_DNS,
                       ELON_TWEET)) + "\n")

f.write("\n\n\n----NFT ENDS HERE----\n\n\n")

f.write("----NFT GENERATED BY https://github.com/tg12/nft-generator----\n\n\n")

f.write("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS")
f.write(" OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF")
f.write(" MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND")
f.write(" NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE")
f.write(" DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,")
f.write(" WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN")
f.write(" CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE")
f.write(" SOFTWARE.\n\n")

f.write("Bitcoin Cash (BCH)\t\t\tqpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk\n")
f.write("Ether (ETH)\t\t\t0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB\n")
f.write("Litecoin (LTC)\t\t\tLfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu\n")
f.write("Bitcoin (BTC)\t\t\t14Dm7L3ABPtumPDcj3REAvs4L6w9YFRnHK\n")

