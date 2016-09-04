# -*- coding: utf-8 -*-
# Copyright 2016 Pierre Verkest <pverkest@anybox.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "web Json widget",
    "summary": "Json Widget for display json fields",
    "version": "10.0.1.0.0",
    "category": "framework",
    "website": "https://odoo-community.org/",
    "author": "Pierre Verkest <pverkest@anybox.fr>, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "web",
        "json",
    ],
    "data": [
        'views/webclient_templates.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
