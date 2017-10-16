.. -*- mode: rst -*-

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |license|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions| |requires|

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/TuneLab/requests-mv-integrations.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/TuneLab/requests-mv-integrations

.. |coveralls| image:: https://coveralls.io/repos/github/TuneLab/requests-mv-integrations/badge.svg?branch=master
    :alt: Code Coverage Status
    :target: https://coveralls.io/github/TuneLab/requests-mv-integrations?branch=master

.. |requires| image:: https://requires.io/github/TuneLab/requests-mv-integrations/requirements.svg?branch=master
     :target: https://requires.io/github/TuneLab/requests-mv-integrations/requirements/?branch=master
     :alt: Requirements Status

.. |version| image:: https://img.shields.io/pypi/v/requests-mv-integrations.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/requests-mv-integrations

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/requests-mv-integrations.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/requests-mv-integrations

.. end-badges

requests-mv-integrations
========================

``requests-mv-integrations`` is a Python 3 module for TUNE Multiverse Libraries.

.. image:: ./images/request_mv_integrations.png
   :scale: 50 %
   :alt: UML requests-mv-integrations

Usage
-----

.. code-block:: python
    URL_TUNE_MAT_API_COUNTRIES = \
        'https://api.mobileapptracking.com/v2/countries/find.json'

    from requests_mv_integrations import (
        RequestMvIntegrationDownload,
    )
    request_download = RequestMvIntegrationDownload(logger_level=logging.DEBUG)

    result = \
        request_download.request(
            request_method='GET',
            request_url=URL_TUNE_MAT_API_COUNTRIES,
            request_params=None,
            request_retry=None,
            request_headers=HEADER_CONTENT_TYPE_APP_JSON,
            request_label="TMC Countries"
        )

    json_tune_mat_countries = result.json()

    pprint(json_tune_mat_countries)

Example
-------

.. code-block:: bash
    python3 examples/example_request.py
    {"asctime": "2017-10-13 12:02:53 -0700", "levelname": "INFO", "name": "__main__", "version": "00.05.04", "message": "Start"}
    {"asctime": "2017-10-13 12:02:53 -0700", "levelname": "DEBUG", "name": "requests_mv_integrations", "version": "00.05.04", "message": "TMC Countries: Start"}
    ...
    {"asctime": "2017-10-13 12:02:53 -0700", "levelname": "DEBUG", "name": "requests_mv_integrations", "version": "00.05.04", "message": "TMC Countries: Details", "request_data": "", "request_headers": {"Content-Type": "application/json", "User-Agent": "(requests-mv-integrations/00.05.04, Python/3.6.2)"}, "request_label": "TMC Countries", "request_method": "GET", "request_params": {}, "request_url": "https://api.mobileapptracking.com/v2/countries/find.json", "timeout": 60}
    {"asctime": "2017-10-13 12:02:53 -0700", "levelname": "DEBUG", "name": "requests_mv_integrations", "version": "00.05.04", "message": "TMC Countries: Curl", "request_curl": "curl --verbose -X GET -H 'Content-Type: application/json' -H 'User-Agent: (requests-mv-integrations/00.05.04, Python/3.6.2)' --connect-timeout 60 -L 'https://api.mobileapptracking.com/v2/countries/find.json'", "request_label": "TMC Countries", "request_method": "GET"}
    ...
    {
        'data': [
            {'id': 0, 'name': 'International (Generic)'},
            {'id': 4, 'name': 'Afghanistan'},
            {'id': 8, 'name': 'Albania'},
            {'id': 10, 'name': 'Antarctica'},
            {'id': 12, 'name': 'Algeria'},
            {'id': 16, 'name': 'American Samoa'},
            {'id': 20, 'name': 'Andorra'},
            {'id': 24, 'name': 'Angola'},
            {'id': 28, 'name': 'Antigua And Barbuda'},
            {'id': 31, 'name': 'Azerbaijan'},
        ],
        'response_size': '845',
        'status_code': 200,
    }

Dependencies
============

``requests-mv-integrations`` module is built upon Python 3 and is build upon
several custom modules that are held within .. _PyPI: https://pypi.python.org/pypi

.. code-block:: bash
    python3 -m pip uninstall -r requirements.txt
    python3 -m pip install --upgrade -r requirements.txt

TUNE Multiverse Custom Core Packages
------------------------------------

- .. _logging-mv-integrations: https://pypi.python.org/pypi/logging-mv-integrations

TUNE Multiverse Custom Support Packages
---------------------------------------

- .. _pyhttpstatus-utils: https://pypi.python.org/pypi/pyhttpstatus-utils
- .. _safe-cast: https://pypi.python.org/pypi/safe-cast

Support Packages
----------------

- .. _beautifulsoup4: https://pypi.python.org/pypi/beautifulsoup4
- .. _deepdiff: https://pypi.python.org/pypi/deepdiff
- .. _iron-cache: https://pypi.python.org/pypi/iron-cache
- .. _requests: https://pypi.python.org/pypi/requests


Acknowledgements
================

.. include:: AUTHORS.rst

Reporting Issues
================

We definitely want to hear your feedback.

Report issues using the `Github Issue Tracker`:
https://github.com/TuneLab/requests-mv-integrations/issues

HISTORY
=======

.. include:: HISTORY.rst
