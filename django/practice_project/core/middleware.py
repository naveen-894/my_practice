# myapp/middleware.py

import logging

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        # Log the request method and path
        self.logger.info(f"Request method: {request.method}, Path: {request.path}")
        request.api_logs = ['lkjhgjkl']
        # Call the next middleware or view
        response = self.get_response(request)
        print(request.api_logs, '__call__ ')
        # Return the response
        return response

    def process_exception(self, request, exception):
        # Log the exception
        request.api_logs.append(exception)
        self.logger.error(f"Exception occurred: {exception}")
