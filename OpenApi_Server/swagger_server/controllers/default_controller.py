import connexion
import six

from swagger_server.models.input_numbers import InputNumbers  # noqa: E501
from swagger_server.models.prime_factorization import PrimeFactorization  # noqa: E501
from swagger_server import util
from swagger_server.adapters.factorization import prime_factors


def primes_post(body=None):  # noqa: E501
    """primes_post

     # noqa: E501

    :param body: The numbers to be factorized
    :type body: dict | bytes

    :rtype: PrimeFactorization
    """
    if connexion.request.is_json:
        body = InputNumbers.from_dict(connexion.request.get_json()) # noqa: E501
        
        print(body.input_numbers)
    return PrimeFactorization.from_dict({
        "result": [{
            "input_number": n,
            "prime_factors": prime_factors(n)
        } for n in body.input_numbers]
    })