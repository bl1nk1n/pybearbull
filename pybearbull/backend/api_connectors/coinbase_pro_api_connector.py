import requests
# Pagination
#   uses cursor pagination for all requests returning arrays
#   allows for fetching results before and after the current page of results
#   "before" and "after" cursors are available via response headers "CB-BEFORE"
#   and "CB-AFTER"
#   Parameters:
#       before  -   request page before (newer) this page id
#       after   -   request page after (older) this page id
#       limit   -   (default 100) number of results per request (max 100)
#   Example:
#       GET /orders?before=2&limit=30

# Timestamps: ISO 8601 with microseconds    (e.g. 2014-11-06T10:34:47.123456Z)

# Numbers are sent as strings to preserve precision, same should be done for
# requests to avoid truncation and precision errors.
# Integers are left alone

# IDs are UUID (can make request using UUID with and without dashes)

# Rate Limit
#   Public:
#       3 requests per second up to 6 requests per second in bursts per IP
#   Private:
#       5 requests per second up to 10 requests per second in bursts per 
#       profile ID

# TODO Private functions

class coinbase_pro_api_connector:
    _restful_api_endpoint = "https://api.pro.coinbase.com"
#    _status_codes = {200: "OK",
#                     400: "Bad Request - Invalid Request Format",
#                     401: "Unauthorized - Invalid API Key",
#                     403: "Forbidden - You do not have access to the requested resource",
#                     404: "Not Found",
#                     429: "Too Many Requests",
#                     500: "Internal Server Error - We had a problem with our server"}

    def get_products(self):
        """
        Gets a list of currency pairs for trading from the Conbase Pro API.

        Returns:
            JSON Object:    If no errors happened, a list of dictionaries is
                            returned: one for each currency pair.  Inside the 
                            dictionaries are the keys: id, base_currency, 
                            quote_currency, base_min_size, base_max_size, and 
                            quote_increment.

            None:           If errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        path = "/products"

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    def get_product_order_book(self, product, level=1):
        """
        Gets the product's current order book from the Coinbase Pro API.

        Parameters:
            product (str):  The product ID of the cryptocurrency exchange.

            level (int):    The verbosity that the result will be given in.
                            If specified, must be between 1 and 3.

        Returns:
            JSON Object:    If no errors happened, a dictionary is returned:
                            representing the product's order book.  Inside the 
                            dictionary are three keys: sequence, bids, and 
                            asks.  Both the bids' and asks' values are lists of
                            bids and asks. If the level was set to 1 (default),
                            then only the best bid and ask are returned.  If 
                            the level was set to 2, the top 50 bids and asks 
                            are returned (aggregated).  If the level was set to
                            3, the full order book is returned (not 
                            aggregated).  Each bid or ask entry contains: 
                            price, size, and num-orders.  When using level 3
                            the num-orders is exchanged for order_id (UUID).

            None:           If product is not a string, level is not an
                            integer, level is greater than 3, level is less
                            than 1 or errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        if (not isinstance(product, str) or not isinstance(level, int) or
                level > 3 or level < 1):
            return None

        path = "/products/" + product + "/book"
        if (level > 1):
            path += "?level=" + str(level)

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    def get_product_ticker(self, product):
        """
        Gets a snapshot of the product's last trade from the Coinbase Pro API.

        Parameters:
            product (str):  The product ID of the cryptocurrency exchange.

        Returns:
            JSON Object:    If no errors happened, a dictionary of ticker
                            information is returned.  Inside the dictionary are
                            the keys: trade_id, price, size, bid, ask, volume,
                            and time.

            None:           If product is not a string or errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        if (not isinstance(product, str)):
            return None

        path = "/products/" + product + "/ticker"

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    # buy indicates downtick; sell indicates uptick
    # this request is paginated...
    def get_trades(self, product):
        """
        Get a product's latest trades from the Coinbase Pro API.

        Parameters:
            product (str):  The product ID of the cryptocurrency exchange.

        Returns:
            JSON Object:    If no errors happened, a list of dictionaries is
                            returned: each of which is a recent trade.  Inside
                            the dictionaries are the keys: time, trade_id, 
                            price, size, and side.

                None:       If product is not a string or errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        if (not isinstance(product, str)):
            return None

        path = "/products/" + product + "/trades"

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    #custom rate limit of 1 request per second, 2 requests per second in
    # bursts per IP
    def get_historic_rates(self, product, granularity, start=None, end=None):
        """
        Get a product's historic rates from the Coinbase Pro API.

        Parameters:
            product (str):      The product ID of the cryptocurrency exchange.

            granularity (int):  The granularity in seconds of each aggregation
                                bucket.  Must be one of: 60, 300, 900, 3600,
                                21600, or 86400 (1m, 5m, 15m, 1h, 6h, or 1d).

            start (str):        The start time in ISO 8601 format.

            end (str):          The end time in ISO 8601 format.

        Returns:
            JSON Object:    If no errors happened, a list of lists is returned:
                            each of which a candle for an aggregation.  Inside 
                            the lists are values for the time, low, high, open,
                            close, and volume of each aggregation.

                None:       If product is not a string, granularity is not one
                            of the specified integers, the start time is not in
                            ISO 8601 format, the end time is not in ISO 8601
                            format, the number of candles between start and end
                            is over 300, or errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        if (not isinstance(product, str) or not isinstance(granularity, int) or
                (granularity not in [60, 300, 900, 3600, 21600, 86400])):
            return None

        if (start is None):
            end = None
        elif (end is None):
            start = None
        # else I need to check that they are both strings and in ISO 8601 format

        # need to check that the number of intervals between start and end with
        # the given granularity is less than 300 candles

        path = "/products/" + product + "/candles?granularity=" + str(granularity)
        if (start and end):
            path += "&start=" + str(start) + "&end=" + str(end)

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    def get_24h_stats(self, product):
        """
        Get a product's 24 hour statistics from the Coinbase Pro API.

        Parameters:
            product (str):  The product ID of the cryptocurrency exchange.

        Returns:
            JSON Object:    If no errors happened, a dictionary is returned:
                            representing a product's 24 hour statistics.
                            Inside the dictionary are the keys: open, high,
                            low, volume, last, and volume_30day.

                None:       If product is not a string or errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        if (not isinstance(product, str)):
            return None

        path = "/products/" + product + "/stats"

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    def get_currencies(self):
        """
        Get list of known currencies from the Coinbase Pro API.

        Returns:
            JSON Object:    If no errors happened, a list of dictionaries is
                            returned: each dictionary represents a known
                            currency.  Each dictionary contains the keys: id,
                            name, and min_size.

                None:       If errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        path = "/currencies"

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()

    def get_time(self):
        """
        Get the API server time for the Coinbase Pro API.

        Returns:
            JSON Object:    If no errors happened, a dictionary is returned
                            representing the current time on the API server.
                            The dictionary contains the keys: iso and epoch.

            None:           If errors happened.
        """
        # need to have custom exceptions and verbose printing here (add lib)
        path = "/time"

        r = requests.get(self._restful_api_endpoint + path)
        if (r.status_code != 200):
            return None

        return r.json()
