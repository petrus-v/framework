# -*- coding: utf-8 -*-
# Copyright 2016 Pierre Verkest <pverkest@anybox.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Json test",
    "summary": "Test json moodule that is a support for postgresql jsonb data",
    "version": "10.0.1.0.0",
    "category": "framework",
    "website": "https://odoo-community.org/",
    "author": "Pierre Verkest <pverkest@anybox.fr>, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "json",
        "web_widget_json",
    ],
    "data": [
    ],
    "demo": [
        'demo/res_users_demo.xml',
        'demo/res_users_view.xml',
    ],
    "qweb": [
    ]
}
