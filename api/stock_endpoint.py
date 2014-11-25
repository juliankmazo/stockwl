"""Stock API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""

import endpoints
from protorpc import remote


stock_api = endpoints.api(
	name='stockApi', 
	version='v1', 
	description='API for the stock web scraper'
)