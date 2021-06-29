# -*- coding: utf-8 -*-
#######
# actinia-core - an open source REST API for scalable, distributed, high
# performance processing of geographical data that uses GRASS GIS for
# computational tasks. For details, see https://actinia.mundialis.de/
#
# Copyright (c) 2016-2018 Sören Gebbert and mundialis GmbH & Co. KG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#######

"""
Raster layer resources
"""
from copy import deepcopy
from flask_restful_swagger_2 import Schema
from actinia_core.models.response_models import ProcessingResponseModel

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika"
__copyright__ = "Copyright 2016-2021, Sören Gebbert and mundialis GmbH & Co. KG"
__maintainer__ = "mundialis"


class RasterInfoModel(Schema):
    """Schema that contains raster map layer information
    """
    type = 'object'
    properties = {
        'cells': {'type': 'string'},
        'cols': {'type': 'string'},
        'comments': {'type': 'string'},
        'creator': {'type': 'string'},
        'database': {'type': 'string'},
        'datatype': {'type': 'string'},
        'maptype': {'type': 'string'},
        'east': {'type': 'string'},
        'date': {'type': 'string'},
        'description': {'type': 'string'},
        'ewres': {'type': 'string'},
        'max': {'type': 'string'},
        'min': {'type': 'string'},
        'ncats': {'type': 'string'},
        'nsres': {'type': 'string'},
        'location': {'type': 'string'},
        'map': {'type': 'string'},
        'mapset': {'type': 'string'},
        'rows': {'type': 'string'},
        'source1': {'type': 'string'},
        'north': {'type': 'string'},
        'source2': {'type': 'string'},
        'units': {'type': 'string'},
        'vdatum': {'type': 'string'},
        'south': {'type': 'string'},
        'timestamp': {'type': 'string'},
        'title': {'type': 'string'},
        'west': {'type': 'string'}
    }
    example = {
        "cells": "2025000",
        "cols": "1500",
        "comments": "\"r.proj input=\"ned03arcsec\" "
                    "location=\"northcarolina_latlong\" mapset=\"\\helena\" "
                    "output=\"elev_ned10m\" method=\"cubic\" resolution=10\"",
        "creator": "\"helena\"",
        "database": "/tmp/gisdbase_75bc0828",
        "datatype": "FCELL",
        "date": "\"Tue Nov  7 01:09:51 2006\"",
        "description": "\"generated by r.proj\"",
        "east": "645000",
        "ewres": "10",
        "location": "nc_spm_08",
        "map": "elevation",
        "mapset": "PERMANENT",
        "max": "156.3299",
        "min": "55.57879",
        "ncats": "255",
        "north": "228500",
        "nsres": "10",
        "rows": "1350",
        "source1": "\"\"",
        "source2": "\"\"",
        "south": "215000",
        "timestamp": "\"none\"",
        "title": "\"South-West Wake county: Elevation NED 10m\"",
        "units": "\"none\"",
        "vdatum": "\"none\"",
        "west": "630000"
    }


class RasterInfoResponseModel(ProcessingResponseModel):
    """Response schema for raster map layer information.
    """
    type = 'object'
    properties = deepcopy(ProcessingResponseModel.properties)
    properties["process_results"] = RasterInfoModel
    required = deepcopy(ProcessingResponseModel.required)
    # required.append("process_results")
    example = {
        "accept_datetime": "2018-05-02 10:44:11.764375",
        "accept_timestamp": 1525257851.7643716,
        "api_info": {
            "endpoint": "rasterlayerresource",
            "method": "GET",
            "path": "/locations/nc_spm_08/mapsets/PERMANENT/raster_layers/elevation",
            "request_url": "http://localhost:8080/locations/nc_spm_08/mapsets/"
                           "PERMANENT/raster_layers/elevation"
        },
        "datetime": "2018-05-02 10:44:11.897704",
        "http_code": 200,
        "message": "Processing successfully finished",
        "process_chain_list": [
            {
                "1": {
                    "flags": "gre",
                    "inputs": {
                        "map": "elevation@PERMANENT"
                    },
                    "module": "r.info"
                }
            }
        ],
        "process_log": [
            {
                "executable": "r.info",
                "parameter": [
                    "map=elevation@PERMANENT",
                    "-gre"
                ],
                "return_code": 0,
                "run_time": 0.050168514251708984,
                "stderr": [
                    ""
                ],
                "stdout": "..."}
        ],
        "process_results": {
            "cells": "2025000",
            "cols": "1500",
            "comments": "\"r.proj input=\"ned03arcsec\" "
                        "location=\"northcarolina_latlong\" mapset=\"\\helena\" "
                        "output=\"elev_ned10m\" method=\"cubic\" resolution=10\"",
            "creator": "\"helena\"",
            "database": "/actinia/workspace/temp_db/"
                        "gisdbase_5f1a5262c8bf4d4789348ffa2406ec3e",
            "datatype": "FCELL",
            "date": "\"Tue Nov  7 01:09:51 2006\"",
            "description": "\"generated by r.proj\"",
            "east": "645000",
            "ewres": "10",
            "location": "nc_spm_08",
            "map": "elevation",
            "mapset": "PERMANENT",
            "max": "156.3299",
            "min": "55.57879",
            "ncats": "255",
            "north": "228500",
            "nsres": "10",
            "rows": "1350",
            "source1": "\"\"",
            "source2": "\"\"",
            "south": "215000",
            "timestamp": "\"none\"",
            "title": "\"South-West Wake county: Elevation NED 10m\"",
            "units": "\"none\"",
            "vdatum": "\"none\"",
            "west": "630000"
        },
        "progress": {
            "num_of_steps": 1,
            "step": 1
        },
        "resource_id": "resource_id-0a3d6b2b-0962-4d01-8993-7997f15d1595",
        "status": "finished",
        "time_delta": 0.13338971138000488,
        "timestamp": 1525257851.8976946,
        "urls": {
            "resources": [],
            "status": "http://localhost:8080/resources/user/"
                      "resource_id-0a3d6b2b-0962-4d01-8993-7997f15d1595"
        },
        "user_id": "user"
    }
