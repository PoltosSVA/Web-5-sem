function startCountdown(){
    let countdownElement = document.getElementById('countdown');
    fetch(`http://127.0.0.1:8000/countdown/`)
        .then(response => response.json())
        .then(data =>{
            let remainingTime = data.remaining_time;
            function updateCountdown(){
            	if(remainingTime > 0){
            		let hours = Math.floor(remainingTime/3600);
            		let minutes = Math.floor((remainingTime%3600)/60);
            		let seconds = Math.floor(remainingTime%60);

            		countdownElement.innerHTML = `${hours}: ${minutes}: ${seconds}`;
            		remainingTime--;
            		setTimeout(updateCountdown,1000);
            	}
            	else{
            		countdownElement.innerHTML = 'Countdown over';
            	}
            }
            updateCountdown();
        });

}

startCountdown();