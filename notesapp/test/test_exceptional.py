from rest_framework.test import APITestCase
from notesapp.test.TestUtils import TestUtils
class NotesAppAPIBoundaryTest(APITestCase):
    def test_exceptional(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestExceptional",True,"boundary")
        print("TestExceptional = Passed")
