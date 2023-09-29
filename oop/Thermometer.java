package oop;

public class Thermometer {

    Thermometer(){}

    public double convertCelsiusToFahrenheit(double celsiusTemperature) {
        double fahrenheitTemperature = ((celsiusTemperature / 5) * 9) + 32;
        return fahrenheitTemperature;
    }

    public double convertFahrenheitToCelsius(double fahrenheitTemperature) {
        double celsiusTemperature = ((fahrenheitTemperature - 32) / 9) * 5;
        return celsiusTemperature;
    }
}