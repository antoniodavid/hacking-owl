{
    "name": "Hacking Web Client",
    "summary": "Hacking Web Client",
    "version": "17.0.0.1",
    "category": "Website/Website",
    "website": "https://www.odoo.com",
    "author": "Antonio Ruban",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/templates.xml",
        "views/menus.xml"
    ],
    "assets": {
        "hacking_web.assets": [
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),

            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),

            # required for fa icons
            'web/static/src/libs/fontawesome/css/font-awesome.css',

            # include base files from framework
            ('include', 'web.assets_web'),

            'web/static/src/core/utils/functions.js',
            'web/static/src/core/browser/browser.js',
            'web/static/src/core/registry.js',
            'web/static/src/core/assets.js',

            # include my assets
            'hacking_web/static/src/webclient/**/*',
        ]
    }

}
