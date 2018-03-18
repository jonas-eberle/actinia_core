# -*- coding: utf-8 -*-
from flask.json import loads as json_loads, dumps as json_dumps
import unittest
try:
    from .test_resource_base import ActiniaResourceTestCaseBase
except:
    from test_resource_base import ActiniaResourceTestCaseBase

__license__ = "GPLv3"
__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"


class ListRasterLayersTestCase(ActiniaResourceTestCaseBase):

    #################### LIST RASTER ##########################################

    def create_raster_layer(self, mapset_name, raster_name):
        # Remove potentially existing raster layer
        rv = self.server.delete('/locations/nc_spm_08/mapsets/%s/raster_layers/%s'%(mapset_name, raster_name),
                                headers=self.user_auth_header)
        # print(rv.data)
        # Create
        rv = self.server.post('/locations/nc_spm_08/mapsets/%s/raster_layers/%s'%(mapset_name, raster_name),
                              headers=self.user_auth_header,
                              data=json_dumps({"region":{"n":228500, "s":215000,
                                                         "e":645000,"w":630000,
                                                         "ewres": 50, "nsres": 50},
                                               "expression": "1"}),
                              content_type="application/json")
        # print(rv.data)
        self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

    def test_list_raster_layers(self):
        rv = self.server.get('/locations/nc_spm_08/mapsets/PERMANENT/raster_layers',
                             headers=self.user_auth_header)
        print(rv.data.decode())
        self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

        map_list = json_loads(rv.data)["process_results"]
        self.assertTrue("elevation" in map_list)
        self.assertTrue("aspect" in map_list)
        self.assertTrue("lsat7_2002_10" in map_list)
        self.assertTrue("slope" in map_list)

    def test_list_raster_layers_pattern(self):
        rv = self.server.get('/locations/nc_spm_08/mapsets/PERMANENT/raster_layers?pattern=lsat*',
                             headers=self.user_auth_header)
        print(rv.data.decode())
        self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

        map_list = json_loads(rv.data)["process_results"]
        self.assertFalse("elevation" in map_list)
        self.assertFalse("aspect" in map_list)
        self.assertTrue("lsat7_2002_10" in map_list)
        self.assertFalse("slope" in map_list)

    def test_list_raster_layers_empty_list(self):
        rv = self.server.get('/locations/nc_spm_08/mapsets/PERMANENT/raster_layers?pattern=NONE',
                             headers=self.user_auth_header)
        print(rv.data.decode())
        self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

        map_list = json_loads(rv.data)["process_results"]
        self.assertTrue(len(map_list) == 0)

    #################### DELETE RASTER ##########################################

    def test_remove_raster_layers_pattern(self):

        new_mapset = "raster_test_mapset"
        self.create_new_mapset(new_mapset)

        map_list = ["test_delete_layer_1", "test_delete_layer_2"]

        # Create raster layers
        for map_name in map_list:
            self.create_raster_layer(new_mapset, map_name)

        # Delete raster layers
        #rv = self.server.delete('/locations/nc_spm_08/mapsets/user1/raster_layers?pattern=test_delete_layer_*',
        #                     headers=self.user_auth_header)
        #print(rv.data)
        #self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        #self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

        # List raster layer
        rv = self.server.get('/locations/nc_spm_08/mapsets/%s/raster_layers?pattern=test_delete_layer_*'%new_mapset,
                             headers=self.user_auth_header)
        print(rv.data.decode())
        self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)
        # Check
        map_list_result = json_loads(rv.data)["process_results"]
        for map_name in map_list_result:
            self.assertTrue(map_name in map_list)

        # Delete raster layers
        for map_name in map_list:
            rv = self.server.delete('/locations/nc_spm_08/mapsets/%s/raster_layers/%s'%(new_mapset, map_name),
                                    headers=self.user_auth_header)
            print(rv.data.decode())

    def test_rename_raster_layers(self):

        new_mapset = "raster_test_mapset"
        self.create_new_mapset(new_mapset)

        map_list = ["test_rename_layer_1", "test_rename_layer_2"]
        new_map_list = ["test_rename_layer_1_new", "test_rename_layer_2_new"]
        rename_map_list = [("test_rename_layer_1", "test_rename_layer_1_new"),
                           ("test_rename_layer_2", "test_rename_layer_2_new")]

        # Create raster layers
        for map_name in map_list:
            self.create_raster_layer(new_mapset, map_name)

        # Rename raster layer
        rv = self.server.put('/locations/nc_spm_08/mapsets/%s/raster_layers'%new_mapset,
                             headers=self.user_auth_header,
                             data=json_dumps(rename_map_list),
                             content_type="application/json")
        print(rv.data.decode())
        self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

        # Rename raster layer
        rv = self.server.put('/locations/nc_spm_08/mapsets/%s/raster_layers'%new_mapset,
                             headers=self.user_auth_header,
                             data=json_dumps(rename_map_list),
                             content_type="application/json")
        print(rv.data.decode())
        self.assertEqual(rv.status_code, 400, "HTML status code is wrong %i"%rv.status_code)
        self.assertEqual(rv.mimetype, "application/json", "Wrong mimetype %s"%rv.mimetype)

        # Delete raster layers
        for map_name in new_map_list:
            rv = self.server.delete('/locations/nc_spm_08/mapsets/%s/raster_layers/%s'%(new_mapset, map_name),
                                    headers=self.user_auth_header)
            print(rv.data.decode())
            self.assertEqual(rv.status_code, 200, "HTML status code is wrong %i"%rv.status_code)


if __name__ == '__main__':
    unittest.main()
