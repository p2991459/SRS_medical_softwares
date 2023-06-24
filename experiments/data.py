# import websocket
# import json
#
# def on_open(ws):
#     message = {"a": "subscribe", "v": [408065]}
#     ws.send(json.dumps(message))
#
# def on_message(ws, message):
#     try:
#         data = json.loads(message)
#         # Handle received data here
#         print(data)
#     except json.JSONDecodeError as e:
#         print(message)
#         print("Error parsing JSON:", e)
#
# def on_close(ws):
#     # WebSocket connection closed
#     print("WebSocket connection closed")
#
# def on_error(ws, error):
#     # WebSocket error occurred
#     print("WebSocket error:", error)
#
# websocket.enableTrace(True)
# ws = websocket.WebSocketApp("wss://ws.kite.trade?api_key=mhs56hck9idjv8nj&access_token=ogZkMOcMDR2moX3Cobn7rIQUT2rmznBl",
#                             on_open=on_open,
#                             on_message=on_message,
#                             on_close=on_close,
#                             on_error=on_error)
# ws.run_forever()


import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker("mhs56hck9idjv8nj", "ogZkMOcMDR2moX3Cobn7rIQUT2rmznBl")

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([408065])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [408065])

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()