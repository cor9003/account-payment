import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-account-payment",
    description="Meta package for oca-account-payment Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_due_list',
        'odoo12-addon-account_due_list_payment_mode',
        'odoo12-addon-account_move_line_auto_reconcile_hook',
        'odoo12-addon-account_payment_credit_card',
        'odoo12-addon-account_payment_return',
        'odoo12-addon-account_payment_return_import',
        'odoo12-addon-account_payment_return_import_iso20022',
        'odoo12-addon-account_payment_show_invoice',
        'odoo12-addon-account_payment_widget_amount',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
