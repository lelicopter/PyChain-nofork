import sha3
import hashlib
import json


class Block:
	"""
	Block object for encapsulating common block header actions
	as seen in Bitcoin.
	Also used as a block template"""
	
	def __init__(self):
		self.version = None 
		self.index = None
		
		self.prev_hash = None
		self.timestamp = None
		#should be a list of tx objects
		self.transactions = None
		self.total_value = None
		#relevant for mining, TODO
		self._stratum_string = None
		
		#merklebranch
		self._merklebranch = None
		#Coinbase transaction
		self.coinbase = None
		#proof
		self.proof = None
		
		
		#HASH#
		@property
		def prev_hash(self):
			return self.hashprev
			
		@property
		def prev_hash_hex(self):
			return hexlify(self.hashprev)
			
		#TIMESTAMP#
		@property
		def timestamp(self):
			return self.timestamp
		
		#VERSION#
		@property 
		def version(self):
			return self.version
		
		@property
		def fee_total(self):
			return sum([t.fees or 0 for t in self.transactions])

	
		#TOOD: implement method to jsonify blocks