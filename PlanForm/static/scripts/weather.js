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

    const container = document.createElement("div");
    container.classList.add("container-fluid");
    weatherDiv.appendChild(container);

    const row = document.createElement("div");
    row.classList.add("row");
    container.appendChild(row);

    const periods = data.properties.periods;

    const numHoursShown = 3;
    for (let p = 0; p < numHoursShown; p++){
        period = periods[p];
        //make div for col
        const col = document.createElement("div");
        col.classList.add("col-md-4");
        col.classList.add("justify-content-center");
        col.classList.add("text-center");
        col.classList.add("border");
        col.classList.add("border-top-0");
        col.classList.add("border-bottom-0");
        col.classList.add("border-dark");
        row.appendChild(col);

        // add time
        let start = period.startTime;
        let end = period.endTime;
        let pos = start.indexOf("T");
        start = start.charAt(pos+1) + start.charAt(pos+2);
        pos = end.indexOf("T");
        end = end.charAt(pos+1) + end.charAt(pos+2);

        if (start == 12)
            start += "p.m."
        else if (start == 0)
            start = 12 + "a.m."
        else if (start > 12)
            start = (start-12) + "p.m."
        else
            start += "a.m."

        if (end == 12)
            end += "p.m."
        else if (end == 0)
            end = 12 + "a.m."
        else if (end > 12)
            end = (end-12) + "p.m."
        else
            end += "a.m."
        
        const time = document.createElement("p");
        time.innerText = `${start} - ${end}`;
        col.appendChild(time);

        // add weather image
        const img = document.createElement("img");
        img["src"] = period.icon;
        img["alt"] = "weather icon"
        col.appendChild(img);

        // add temperature
        const temp = document.createElement("p");
        temp.innerText = `${period.temperature}\u00B0 ${period.temperatureUnit}`;
        col.appendChild(temp);

        // add forcast
        const forecast = document.createElement("p");
        forecast.innerText = `${period.shortForecast}`;
        col.appendChild(forecast);
    }

}

function validateJSON(response) {
    if (response.ok) {
        return response.json();
    } else {
        return Promise.reject(response);
    }
}