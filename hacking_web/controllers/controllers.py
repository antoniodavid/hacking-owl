from odoo.http import request, route, Controller


class RootPage(Controller):
    @route(['/hacking_web/web'], type='http', auth='public')
    def root_page(self):
        """
        Renders the oxp demo page
        """
        context = {
            'session_info': request.env['ir.http'].get_frontend_session_info(),
            "hacking_web": {
                'name': "Hacking Web Client",
            }
        }
        response = request.render('hacking_web.index', context)
        return response
