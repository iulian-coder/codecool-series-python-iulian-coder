let buttonFavorit = document.getElementsByName('favorites');

for (episod of buttonFavorit) {
    episod.addEventListener('click', addFavoriteEpisode)
}


function addFavoriteEpisode(event) {
    // console.log(event)
    let userId = event.target.attributes[2].value;
    let episodeId = event.target.id;
    let data = {userId, episodeId};
    const option = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };
    fetch('http://127.0.0.1:5000/api/add-favorite', option).then(location.reload()).then(notification)
}

function notification() {
    alert('Episod to Favorite')

}