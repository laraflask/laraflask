class ExcludeCSRFMiddleware:
    def __init__(self):

        # Define the routes to exclude from CSRF protection
        self.exclude_routes = [
            {
                'route' : '/test/post_method',
                'function' : 'test.post_method'
            }
        ]