//
//  myWeatherApp.swift
//  myWeather
//
//  Created by Tomáš Sabol on 2/14/21.
//

import SwiftUI

@main
struct WeatherApp: App {
  var body: some Scene {
    WindowGroup {
      let weatherService = WeatherService()
      WeatherView(viewModel: WeatherViewModel(weatherService: weatherService))
    }
  }
}
