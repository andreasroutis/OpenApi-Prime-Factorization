# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.input_numbers import InputNumbers  # noqa: E501
from swagger_server.models.prime_factorization import PrimeFactorization  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_primes_post(self):
        """Test case for primes_post

        
        """
        body = InputNumbers()
        response = self.client.open(
            '/primes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
