import unittest

class DataResidencyManager:
	def __init__(self, policies):
		self.policies = policies

	def apply_policy(self, data, user_id):
		for policy in self.policies:
			if policy.matches(data, user_id):
				return policy.apply(data)
		return data

class DataResidencyPolicy:
	def matches(self, data, user_id):
		pass

	def apply(self, data):
		pass

class USDataResidencyPolicy(DataResidencyPolicy):
	def matches(self, data, user_id):
		return user_id.startswith('US_')

	def apply(self, data):
		data['residency'] = 'US'
		return data

class EUDataResidencyPolicy(DataResidencyPolicy):
	def matches(self, data, user_id):
		return user_id.startswith('EU_')

	def apply(self, data):
		data['residency'] = 'EU'
		return data

class TestDataResidencyManager(unittest.TestCase):
	def setUp(self):
		self.us_policy = USDataResidencyPolicy()
		self.eu_policy = EUDataResidencyPolicy()
		self.manager = DataResidencyManager([self.us_policy, self.eu_policy])

	def test_apply_us_policy(self):
		data = {'name': 'Abak', 'email': 'abak@example.com'}
		user_id = 'US_123'
		result = self.manager.apply_policy(data, user_id)
		self.assertEqual(result['residency'], 'US')

	def test_apply_eu_policy(self):
		data = {'name': 'Aida', 'email': 'aida@example.com'}
		user_id = 'EU_456'
		result = self.manager.apply_policy(data, user_id)
		self.assertEqual(result['residency'], 'EU')

	def test_no_policy_matches(self):
		data = {'name': 'Global', 'email': 'global@example.com'}
		user_id = 'GL_789'
		result = self.manager.apply_policy(data, user_id)
		self.assertEqual(result, data)

if __name__ == '__main__':
	unittest.main()
