#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace requests_mv_integrations

import pytest
import os
import sys
import gzip
import shutil

TMP_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + '/tmp'

from .resources.mockserver import run_server
from requests_mv_integrations import (
    RequestMvIntegrationUpload,
)
from requests_mv_integrations.exceptions import (
    TuneRequestBaseError,
)

__all__ = [run_server]

current_path = os.path.dirname(os.path.realpath(__file__))
test_config_path = "%s/tests/resources/uploadtestfile.json" % os.path.dirname(current_path)
test_url = "http://localhost:8998/upload.json"


@pytest.fixture
def request_object():
    print("creating object")
    obj = RequestMvIntegrationUpload()
    return obj

@pytest.fixture
def test_file_path():
    current_path = os.path.dirname(os.path.realpath(__file__))
    return "%s/tests/resources/uploadtestfile.json" % os.path.dirname(current_path)

@pytest.fixture
def test_file_size():
    633


class TestRequestMvIntegrationUpload:
    @pytest.mark.parametrize(
        'url, file_path, file_size, message', (("url", "path", 1, 'FileNotFound'), ("url", test_config_path, 1, 'Invalid URL'),)
    )
    def test_request_upload_json_fail(self, request_object, url, file_path, file_size, message):
        with pytest.raises(TuneRequestBaseError) as info:
            request_object.request_upload_json_file(
                upload_request_url=url,
                upload_data_file_path=file_path,
                upload_data_file_size=file_size,
                is_upload_gzip=None,
                request_label="test_request_upload_json_fail",
            )

        assert message in str(info.value)

    def test_request_upload_json_pass(self, httpbin, request_object, test_file_path):
        url = httpbin('put')

        response = request_object.request_upload_json_file(
            upload_request_url=url,
            upload_data_file_path=test_file_path,
            upload_data_file_size=os.path.getsize(test_file_path),
            is_upload_gzip=False,
            request_label='test_request_upload_json_pass',
        )
        assert response
        assert response.status_code == 200
        assert 'application/json' in response.headers["Content-Type"]

    def test_request_upload_gzip_pass(self, httpbin, request_object, test_file_path, test_file_size):
        url = httpbin('put')

        test_gzip_path = f"{test_file_path}.gz"
        os.remove(test_gzip_path) if os.path.exists(test_gzip_path) else None

        with open(test_file_path, 'rb') as f_in:
            with gzip.open(test_gzip_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        response = request_object.request_upload_json_file(
            upload_request_url=url,
            upload_data_file_path=test_gzip_path,
            upload_data_file_size=os.path.getsize(test_gzip_path),
            is_upload_gzip=True,
            request_label='test_request_upload_gzip_pass',
        )
        assert response
        assert response.status_code == 200

    @pytest.mark.parametrize('url, message, data', (("url", "Invalid URL", "data"),))
    def test_request_upload_data_fail(self, request_object, url, message, data):
        with pytest.raises(TuneRequestBaseError) as info:
            request_object.request_upload_data(
                url,
                data,
                upload_data_size=1,
                request_label='test_request_upload_data_fail',
            )
        assert message in str(info.value)

    def test_request_upload_data_pass(self, httpbin, request_object):
        url = httpbin('put')
        data = "hello, world!"
        data_size = sys.getsizeof(data)
        response = request_object.request_upload_data(
            upload_request_url=url,
            upload_data=data,
            upload_data_size=data_size,
            build_request_curl=True,
            request_label='test_request_upload_data_pass',
        )
        assert response
        assert response.status_code == 200
        assert 'application/json' in response.headers["Content-Type"]

    def test_request_upload_data_timeout_pass(self, httpbin, request_object):
        url = httpbin('put')
        data = "hello, world!"
        data_size = sys.getsizeof(data)
        response = request_object.request_upload_data(
            url,
            data,
            upload_data_size=data_size,
            request_label='test_request_upload_data_timeout_pass',
            upload_timeout=100,
        )
        assert response
        assert response.status_code == 200
        assert 'application/json' in response.headers["Content-Type"]
