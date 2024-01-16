

const chooseStar = (rate) => {
    const stars = document.querySelectorAll('.star--item');

    for (let i = 1; i <= 10; i++) {
        if (i <= rate) {
            stars[i-1].classList.add('active-star');
        } else {
            stars[i-1].classList.remove('active-star');
        }
    }
}


const sendRate = (e) => {
    e.preventDefault();

    const starCount = document.querySelectorAll('.active-star').length;
    const rateText = document.querySelector('#rateText').value;
    const movieId = document.querySelector('#movie_id').value;
    const userId = document.querySelector('#user_id').value;
    
    axios.post(
        'http://localhost:8000/rate/',
        {
            movie_id: movieId,
            text: rateText,
            count: starCount,
            user_id: userId,
        }
    ).then((data) => {
        console.log(data);
    }).catch((error) => {
        console.log(error);
    })

    window.location.reload();
}