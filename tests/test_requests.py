#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace requests_mv_integrations

import requests
import pytest
from requests.exceptions import (
    InvalidSchema,
    InvalidURL,
    MissingSchema,
)


class TestRequests:

    @pytest.mark.parametrize(
        'exception, url', (
            (MissingSchema, 'hiwpefhipowhefopw'),
            (InvalidSchema, 'localhost:3128'),
            (InvalidSchema, 'localhost.localdomain:3128/'),
            (InvalidSchema, '10.122.1.1:3128/'),
            (InvalidURL, 'http://'),
        ))
    def test_invalid_url(self, exception, url):
        with pytest.raises(exception):
            requests.get(url)

    @pytest.mark.parametrize('method', ('GET', 'HEAD'))
    def test_no_content_length(self, httpbin, method):
        req = requests.Request(method, httpbin(method.lower())).prepare()
        assert('Content-Length' not in req.headers)

    @pytest.mark.parametrize('method', ('POST', 'PUT', 'PATCH', 'OPTIONS'))
    def test_no_body_content_length(self, httpbin, method):
        req = requests.Request(method, httpbin(method.lower())).prepare()
        assert(req.headers['Content-Length'] == '0')

    @pytest.mark.parametrize('method', ('POST', 'PUT', 'PATCH', 'OPTIONS'))
    def test_empty_content_length(self, httpbin, method):
        req = requests.Request(method, httpbin(method.lower()), data='').prepare()
        assert(req.headers['Content-Length'] == '0')

    def test_chunked_upload_does_not_set_content_length_header(self, httpbin):
        """Ensure that requests with a generator body stream using
        Transfer-Encoding: chunked, not a Content-Length header.
        """
        data = (i for i in [b'a', b'b', b'c'])
        url = httpbin('post')
        r = requests.Request('POST', url, data=data)
        prepared_request = r.prepare()
        assert 'Transfer-Encoding' in prepared_request.headers
        assert 'Content-Length' not in prepared_request.headers

    def test_binary_put_httpbin(self, httpbin):
        url = httpbin('put')
        data = u"ööö".encode("utf-8")
        req = requests.Request('PUT', url, data=data)
        assert req
        prepared_request = req.prepare()
        assert prepared_request
        assert isinstance(prepared_request.body, bytes)