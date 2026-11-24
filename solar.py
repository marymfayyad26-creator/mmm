def calculate_solar_capacity(daily_energy, sunlight_hours):
    efficiency = 0.80

    if sunlight_hours <= 0:
        return 0

    return daily_energy / (sunlight_hours * efficiency)


def calculate_panel_count(required_capacity, panel_watt):
    if panel_watt <= 0:
        return 0

    panel_capacity = panel_watt / 1000
    return int(required_capacity / panel_capacity + 0.999999)
