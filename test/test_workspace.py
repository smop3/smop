import unittest

workspace_ = locals()


def set_pets():
    global workspace_
    animals = ('dog', 'cat', 'fish', 'fox', 'monkey')
    for i in range(len(animals)):
        workspace_['pet_0%s' % i] = animals[i]


class TestWorkspace(unittest.TestCase):
    def test_p03(self):
        """Test read local variables defined in module."""
        set_pets()
        workspace_['pet_05'] = 'bird'
        s = ' '.join([pet_00, pet_02, pet_04, pet_01, pet_03, pet_05])
        print("\n", s)
        self.assertEquals(s, "dog fish monkey cat fox bird")


if __name__ == "__main__":
    unittest.main()
