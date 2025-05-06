from rest_framework.test import APITestCase
from notesapp.models import NotesModel
from notesapp.test.TestUtils import TestUtils
class NotesAppAPIExceptionalTest(APITestCase):
    def test_exception(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary",True,"exception")
        print("TestException = Passed")
