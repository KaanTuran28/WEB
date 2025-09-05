let currentMinutes = 0;

function startClock() {
    const clock = document.getElementById("clock");
    const background = document.getElementById("background");
    const overlay = document.getElementById("overlay");

    const interval = setInterval(() => {
        currentMinutes++;
        const displayMinutes = currentMinutes < 10 ? "0" + currentMinutes : currentMinutes;
        clock.innerText = `09:${displayMinutes}`;

        if (currentMinutes === 5) {
            clearInterval(interval);
            clock.style.display = 'none';
            background.style.opacity = 1;
            overlay.style.opacity = 1;
            showImages();
        }
    }, 1000);
}

function showImages() {
    const images = document.querySelectorAll('.image-box');
    let delay = 0;

    images.forEach((image, index) => {
        delay += 2;
        setTimeout(() => {
            image.style.opacity = 1;
            image.querySelector('img').style.transform = 'translateX(0)';
            image.querySelector('.caption').style.opacity = 1;
        }, delay * 1000);
    });
}

window.onload = startClock;