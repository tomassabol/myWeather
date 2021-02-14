//
//  ContentView.swift
//  Weather
//

import SwiftUI

struct WeatherView: View {

  @ObservedObject var viewModel: WeatherViewModel

  var body: some View {
    ZStack{
        LinearGradient(gradient:
                        Gradient(colors: [.blue, .white]),
                                   startPoint: .topLeading,
                                    endPoint: .bottomTrailing)
                        .edgesIgnoringSafeArea(.all)
        
        VStack {
            
            Spacer()
            
            Text(viewModel.cityName)
                        .font(.system(size: 40))
                        .bold()
                        .padding(.top, 60)
            
            Spacer()

            Image(systemName: viewModel.weatherIcon)
                .renderingMode(.original)
                .font(.system(size: 90))
                .padding()
                .shadow(color: .gray, radius: 10)
            
            Spacer()
            
            Text(viewModel.temperature)
              .font(.system(size: 70))
              .bold()
            
            Spacer()
            
            Text(viewModel.weatherDescription)
                .font(.system(size: 20))
                .bold()
                .padding(.bottom, 80)
                .foregroundColor(.black)
            HStack{
                                
                Spacer()
                                
                VStack{
                    Text("Monday")
                        .font(.system(size: 15))
                        .foregroundColor(.black)
                    Text("25°C")
                        .foregroundColor(.black)
                    }
                                
                Spacer()
                                
                VStack{
                    Text("Tuesday")
                        .font(.system(size: 15))
                        .foregroundColor(.black)
                    Text("25°C")
                        .foregroundColor(.black)
                    }
                                
                Spacer()
                                
                VStack{
                    Text("Wednesday")
                        .font(.system(size: 15))
                        .foregroundColor(.black)
                    Text("25°C")
                        .foregroundColor(.black)
                    }
                                
                Spacer()
                                
                VStack{
                    Text("Thursday")
                        .font(.system(size: 15))
                        .foregroundColor(.black)
                    Text("25°C")
                        .foregroundColor(.black)
                    }
                Spacer()
                }
            
            Spacer()
        }
        .alert(isPresented: $viewModel.shouldShowLocationError) {
          Alert(
            title: Text("Error"),
            message: Text("To see the weather, provide location access in Settings."),
            dismissButton: .default(Text("Open Settings")) {
              guard let settingsURL = URL(string: UIApplication.openSettingsURLString) else { return }
              UIApplication.shared.open(settingsURL)
            }
          )
        }
        .onAppear(perform: viewModel.refresh)
    }
  }
}


struct ContentView_Previews: PreviewProvider {
  static var previews: some View {
    WeatherView(viewModel: WeatherViewModel(weatherService: WeatherService()))
        .preferredColorScheme(.dark)
  }
}
