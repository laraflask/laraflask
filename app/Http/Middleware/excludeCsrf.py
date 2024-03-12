class ExcludeCSRFMiddleware:
    def __init__(self):

        # Define the routes to exclude from CSRF protection
        self.exclude_routes = [
            {
                'route' : '/post_method',
                'function' : 'web.post_method'
            }
        ]