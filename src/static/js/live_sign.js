//Sign Handler

function updateTime() {  
    let localTime = new Date().toISOString();  
    fetch(`/get_schedule_info?sign_key=${signId}&local_time=${localTime}`)  
        .then(response => response.json())  
        .then(data => {  
            let openSign = document.querySelector('.sign-status');  
            let closingTime = document.querySelector('.sign-subscript');  
  
            openSign.textContent = data.state;  
            closingTime.textContent = data.state == 'OPEN' ? 'Closing in ' + data.change_time + ' hours' : 'Opening in ' + data.change_time + ' hours';  
        });  
  
    // Update every minute  
    setTimeout(updateTime, 60000);  
}  
  
updateTime();  

// Fulscren handlers

var fullscreenBtn = document.getElementById('fullscreenBtn');  
  
fullscreenBtn.addEventListener('click', function() {  
    var elem = document.getElementById('banner');  
    if (elem.requestFullscreen) {  
      elem.requestFullscreen();  
    } else if (elem.mozRequestFullScreen) { /* Firefox */  
      elem.mozRequestFullScreen();  
    } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */  
      elem.webkitRequestFullscreen();  
    } else if (elem.msRequestFullscreen) { /* IE/Edge */  
      elem.msRequestFullscreen();  
    }  
});  
  
document.addEventListener('fullscreenchange', function() {  
    if (document.fullscreenElement) {  
        fullscreenBtn.style.display = 'none';  
    } else {  
        fullscreenBtn.style.display = 'block';  
    }  
});  
  
document.addEventListener('mozfullscreenchange', function() { /* Firefox */  
    if (document.mozFullScreenElement) {  
        fullscreenBtn.style.display = 'none';  
    } else {  
        fullscreenBtn.style.display = 'block';  
    }  
});  
  
document.addEventListener('webkitfullscreenchange', function() { /* Chrome, Safari & Opera */  
    if (document.webkitFullscreenElement) {  
        fullscreenBtn.style.display = 'none';  
    } else {  
        fullscreenBtn.style.display = 'block';  
    }  
});  
  
document.addEventListener('MSFullscreenChange', function() { /* IE/Edge */  
    if (document.msFullscreenElement) {  
        fullscreenBtn.style.display = 'none';  
    } else {  
        fullscreenBtn.style.display = 'block';  
    }  
});  

