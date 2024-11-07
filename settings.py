from tinkoff.invest import SecurityTradingStatus

allowed_trading_status = (
    SecurityTradingStatus.SECURITY_TRADING_STATUS_NORMAL_TRADING,
    SecurityTradingStatus.SECURITY_TRADING_STATUS_OPENING_PERIOD,
    SecurityTradingStatus.SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING,

)

time_of_repeat = 60

exclude_instruments = []