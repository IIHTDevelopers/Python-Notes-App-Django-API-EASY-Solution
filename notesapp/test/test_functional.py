from rest_framework.test import APITestCase
from notesapp.models import NotesModel
from notesapp.test.TestUtils import TestUtils
class NotesAppAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NotesModel.objects.create(id=101,title="Python",description="Python is an easy programming language",author="Guido Van Rossum",status="Completed")
    def test_get_request_for_all_records(self):
        url='http://127.0.0.1:8000/notes_crud/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForAllRecords", True, "functional")
            print("TestGetRequestForAllRecords = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForAllRecords", False, "functional")
            print("TestGetRequestForAllRecords = Failed")
    def test_get_request_for_single_record(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForSingleRecord", True, "functional")
            print("TestGetRequestForSingleRecord = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForSingleRecord", False, "functional")
            print("TestGetRequestForSingleRecord = Failed")

    def test_post_request(self):
        url='http://127.0.0.1:8000/notes_crud/'
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language',
            'status':'completed'
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequest", True, "functional")
            print("TestPostRequest = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequest", False, "functional")
            print("TestPostRequest = Failed")

    def test_patch_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        data={
                'status':'completed'
            }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestPatchRequest", True, "functional")
            print("TestPatchRequest = Passed")
        else:
            test_obj.yakshaAssert("TestPatchRequest", False, "functional")
            print("TestPatchRequest = Failed")

    def test_delete_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteRequest", True, "functional")
            print("TestDeleteRequest = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequest", False, "functional")
            print("TestDeleteRequest = Failed")
