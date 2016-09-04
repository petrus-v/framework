# -*- coding: utf-8 -*-
from openerp.tests import common


class TestJsonField(common.TransactionCase):

    def test_browse_user(self):
        self.assertEqual(
            {
                "string": "value",
                "integer": 4,
                "string_array": [
                    "abc", "def"
                ],
                "object": {
                    "a": 1,
                    "b": 2,
                    "c": 3,
                }
            },
            self.env.ref('base.user_demo').more_data
        )
