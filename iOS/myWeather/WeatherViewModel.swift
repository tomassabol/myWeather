//
//  WeatherViewModel.swift
//  myWeather
//
//  Created by Tomáš Sabol on 2/14/21.
//

import Foundation

private let defaultIcon = "cloud.sun.fill"
private let iconMap = [
    "Drizzle" : "cloud.drizzle.fill",
    "Thunderstorm" : "cloud.bolt.fill",
    "Rain" : "cloud.rain.fill",
    "Snow" : "cloud.snow.fill",
    "Clear" : "sun.max.fill",
    "Clouds" : "cloud.fill",
    "Few Clouds" : "cloud.sun.fill"
    
]


class WeatherViewModel: ObservableObject {
  @Published var cityName: String = "City Name"
  @Published var temperature: String = "--"
  @Published var weatherDescription: String = "--"
  @Published var weatherIcon: String = defaultIcon
  @Published var shouldShowLocationError: Bool = false

  public let weatherService: WeatherService

  init(weatherService: WeatherService) {
    self.weatherService = weatherService
  }

  func refresh() {
    weatherService.loadWeatherData { weather, error in
      DispatchQueue.main.async {
        if let _ = error {
          self.shouldShowLocationError = true
          return
        }

        self.shouldShowLocationError = false
        guard let weather = weather else { return }
        self.cityName = weather.city
        self.temperature = "\(weather.temperature)ºC"
        self.weatherDescription = weather.description.capitalized
        self.weatherIcon = iconMap[weather.iconName] ?? defaultIcon
      }
    }
  }
}

