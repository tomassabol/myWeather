window.addEventListener("load", () => {
  let long;
  let lat;
  let temperatureDescription = document.querySelector('.temperature-description');
  let temperatureDegree = document.querySelector('.temperature-degree');
  let locationTimezone = document.querySelector('.location-timezone');

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      long = position.coords.longitude;
      lat = position.coords.latitude;

      const api = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&exclude=minutely,hourly&appid=34b3a1dbb3c79e554d34663a5b83f925&units=metric`;

      fetch(api)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
            const weatherDescription = data.current.weather;

            // set DOM elements from the API
            // temp
            const { temp } = data.current;
            temperatureDegree.textContent = temp;

            // description
            const main =   weatherDescription[0]["main"];
            temperatureDescription.textContent = main;

            // location
            const timezone  = data.timezone;
            locationTimezone.textContent = timezone;
        });
    });
  }
});
