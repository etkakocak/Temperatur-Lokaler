function displayTime() {
  var currentTime = new Date();
  var hours = currentTime.getHours();
  var minutes = currentTime.getMinutes();
  var seconds = currentTime.getSeconds();
  var timeString = hours + ":" + minutes + ":" + seconds;
  document.getElementById("time").innerHTML = timeString;
}
setInterval(displayTime, 1000);

function displayDate() {
  var currentDate = new Date();
  var day = currentDate.getDate();
  var month = currentDate.getMonth();
  var year = currentDate.getFullYear();
  var monthNames = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"];
  var dateString = day + " " + monthNames[month] + " " + year;
  document.getElementById("date").innerHTML = dateString;
}
setInterval(displayDate, 1000);
