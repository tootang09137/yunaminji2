const heart = document.querySelector(".heart");
const animatioHeart = document.querySelector(".animation-heart");

heart.addEventListener('click', () => {
    animatioHeart.classList.add('animation-heart');
    heart.classList.add('fill-color');
});

animatioHeart.addEventListener('click', () =>
{
    animatioHeart.classList.remove('animation-heart');
    heart.classList.remove('heart');
});