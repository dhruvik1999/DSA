class Node:
	def __init__(self,org_root_hash=None):
		self.org_root_hash=org_root_hash
		self.prev_org_root_hash=None
		self.next_org_root_hash=None


class BlockChain:
	def __init__(self,Block_chain_name="DSA_BLOCK_CHAIN"):
		self.Block_chain_name=Block_chain_name
		self.global_hash=None
		self.fiirst_org=None
		self.last_org=None

	def add_org(self,org):
		#adding new node in blockchain for each orgenization
		pass

	def count_global_hash_value(self):
		pass

	def check_global_hash_value(self):
		pass

class Organization:
	def __init__(self,name):
		self.total_amount=None
		self.org_root_hash=None
		self.name=None

	def make_payment(self,reciver_name,ammount):
		# org1 --> org2 $500
		pass

	def recharge(self,sender_name,ammount):
		#org1 <-- Bank $5000
		pass

	def count_hash(self,name,ammount):
		#count hash value for new transection.
		pass

	def merge_local_hash(self):
		#merge and change the org_root_hash value.
		pass

	def validate_org(self):
		pass

	def validate_transection(self):
		pass

