#import requests

# restful api endpoint = https://api.pro.coinbase.com

# Status Codes:
#   200     -   OK
#   400     -   Bad Request: Invalid Request Format
#   401     -   Unauthorized: Invalid API Key
#   403     -   Forbidden: You do not have access to the requested resource
#   404     -   Not Found
#   429     -   Too Many Requests
#   500     -   Internal Server Error: We had a problem with our server

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

# Public functions:
#   products:
#       get products: get a list of currency pairs for trading
#                     base_min_size and base_max_size define order restrictions
#                     quote_increment is the min price and increment
#           GET /products
#           -------------
#           [
#               {
#                   "id": "BTC-USD",
#                   "base_currency": "BTC",
#                   "quote_currency": "USD",
#                   "base_min_size": "0.001",
#                   "base_max_size": "10000.00",
#                   "quote_increment": "0.01"
#               }
#           ]
#       get product order book: get a list of open orders for a product
#                               level param determines amount of detail
#                                   1 only best bid and ask (default)
#                                   2 top 50 bids and asks (aggregated)
#                                   3 full order book (not aggregated)
#           GET /products/<product_id>/book
#           -------------------------------
#           {
#               "sequence": "3",
#               "bids": [
#                   [ price, size, num-orders ],
#               ],
#               "asks": [
#                   [ price, size, num-orders ],
#               ]
#           }
#           GET /products/<product_id>/book?level=3
#           ---------------------------------------
#           {
#               "sequence": "3",
#               "bids": [
#                   [ price, size, order_id ],
#                   [ "295.96","0.05088265","3b0f1225-7f84-490b-a29f-0faef9de823a" ],
#                   ...
#               ],
#               "asks": [
#                   [ price, size, order_id ],
#                   [ "295.97","5.72036512","da863862-25f4-4868-ac41-005d11ab0a5f" ],
#                   ...
#               ]
#           }
#       get product ticker: snapshot of last trade (tick), best bid/ask, and 24h volume
#           GET /products/<product_id>/ticker
#           ---------------------------------
#           {
#             "trade_id": 4729088,
#             "price": "333.99",
#             "size": "0.193",
#             "bid": "333.98",
#             "ask": "333.99",
#             "volume": "5957.11914015",
#             "time": "2015-11-14T20:46:03.511254Z"
#           }
#       get trades: the latest trades for a product
#                   this request is paginated; buy indicates downtick; sell
#                   indicates uptick
#           GET /products/<product_id>/trades
#           ---------------------------------
#           [{
#               "time": "2014-11-07T22:19:28.578544Z",
#               "trade_id": 74,
#               "price": "10.00000000",
#               "size": "0.01000000",
#               "side": "buy"
#           }, {
#               "time": "2014-11-07T01:08:43.642366Z",
#               "trade_id": 73,
#               "price": "100.00000000",
#               "size": "0.01000000",
#               "side": "sell"
#           }]
#       get historic rates: returned in grouped buckets based on "granularity"
#                           custom rate limit of 1 request per second, 2 requests
#                           per second in bursts per IP
#                           if start or end is not provided, both ignored
#                           granularity must be {60, 300, 900, 3600, 21600, or 86400}
#                                                1m, 5m,  15m, 1h,   6h,       1d
#                           max response of 300 candles (if start and end will
#                           cause more, it will be rejected)
#               Parameters: start (ISO 8601)
#                           end (ISO 8601)
#                           granularity (in seconds)
#           GET /products/<product_id>/candles
#           ----------------------------------
#           [
#               [ time, low, high, open, close, volume ],
#               [ 1415398768, 0.32, 4.2, 0.35, 4.2, 12.3 ],
#               ...
#           ]
#       get 24h stats:  volume is in base currency, open high and low are in
#                       quote currency
#           GET /products/<product_id>/stats
#           --------------------------------
#           {
#               "open": "6745.61000000",
#               "high": "7292.11000000",
#               "low": "6650.00000000",
#               "volume": "26185.51325269",
#               "last": "6813.19000000",
#               "volume_30day": "1019451.11188405"
#           }
# currencies:
#   get currencies: list known currencies
#                   codes will conform to ISO 4217 whenever possible
#       GET /currencies
#       ---------------
#       [{
#           "id": "BTC",
#           "name": "Bitcoin",
#           "min_size": "0.00000001"
#       }, {
#           "id": "USD",
#           "name": "United States Dollar",
#           "min_size": "0.01000000"
#       }]
# time:
#   get the server time:
#       GET /time
#       ---------
#       {
#           "iso": "2015-01-07T23:47:25.201Z",
#           "epoch": 1420674445.201
#       }
