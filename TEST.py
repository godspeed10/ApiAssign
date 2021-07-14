try :
    from main import app
    import unittest
except Exception as e:
    print("Some Modules are missing {}".format(e))


class FLaskTest(unittest.TestCase):

    def test_index(self):
        ## check for response 200
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    ## check for data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'result' in response.data)

if __name__ == "__main__":
    unittest.main()