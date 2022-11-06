let handleId = 0; 
const h1 = document.getElementById("time")
 
function getTime(){
  const date = new Date()
  const hour = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();
  const time = `${hour<10?'0'+hour:hour}:${minutes<10?'0'+minutes:minutes}:${seconds<10?'0'+seconds:seconds}`
  h1.textContent = time;
}
 
getTime()