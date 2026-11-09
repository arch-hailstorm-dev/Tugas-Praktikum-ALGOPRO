def compound_interest(principal, rate, time):
    """Fungsi untuk menghitung nilai bunga majemuk."""
    future_value = principal * ((1 + rate) ** time)
    return future_value


def simple_interest(principal, rate, time):
    """Fungsi untuk menghitung nilai bunga majemuk."""
    future_value = principal * rate * time
    return future_value