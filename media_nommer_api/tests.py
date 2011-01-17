import unittest
from media_nommer_api import connect
from media_nommer_api.testing_utils import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

class JobSubmitTests(unittest.TestCase):
    def setUp(self):
        self.connection = connect('http://localhost:8001')
        self.source_path = 's3://%s:%s@%s/%s' % (
            AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY,
            'nommer_in',
            'asf_to_mpeg-1.mpeg'
        )
        self.dest_path = 's3://%s:%s@%s/%s' % (
            AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY,
            'nommer_out',
            'roving_web'
        )

    def test_job_submit(self):
        preset = 'iphone'
        job_opts = {'some_option': 'some_val'}
        print "COMEBACK", self.connection.job_submit(self.source_path,
                                                     self.dest_path,
                                                     preset,
                                                     job_opts)
