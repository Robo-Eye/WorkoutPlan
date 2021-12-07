// listener for when document loads
window.addEventListener("DOMContentLoaded", function() {
    getLocation();
});

function getLocation(){
    const baseURL = "https://api.weather.gov/points/";
    const lat_long = document.getElementById("lat-long").value;

    fetch(`${baseURL}/${lat_long}`)
        .then(validateJSON)
        .then(getWeather)
        .catch(error => {
            console.log("Location Fetch Failed: ", error);
    });
}

function getWeather(data){
    const weatherURL = data.properties.forecastHourly;
    fetch(weatherURL)
        .then(validateJSON)
        .then(addWeather)
        .catch(error => {
            console.log("Weather Fetch Failed: ", error);
    });
}

function addWeather(data){
    const weatherDiv = document.getElementById("weather");

    const period = data.properties.periods[0];

    // add time
    const time = document.createElement("p");
    time.innerText = `Time: ${period.startTime} - ${period.endTime}`;
    weatherDiv.appendChild(time);

    // add weather image
    const img = document.createElement("img");
    img["src"] = period.icon;
    weatherDiv.appendChild(img);

    // add temperature
    const temp = document.createElement("p");
    temp.innerText = `Temperature: ${period.temperature}${period.temperatureUnit}`;
    weatherDiv.appendChild(temp);

    // add forcast
    const forecast = document.createElement("p");
    forecast.innerText = `Forecast: ${period.shortForecast}`;
    weatherDiv.appendChild(forecast);

}

function validateJSON(response) {
    if (response.ok) {
        return response.json();
    } else {
        return Promise.reject(response);
    }
}